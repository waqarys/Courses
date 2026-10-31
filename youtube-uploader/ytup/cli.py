"""Command line: auth / upload / queue / status.  Run `python yt_upload.py -h`."""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from . import metadata as md
from .schedule import next_free_slot, short_time, parse_at, rfc3339_utc, from_rfc3339
from .state import State

HERE = Path(__file__).resolve().parent.parent
COST = {"videos.insert": 1600, "thumbnails.set": 50, "captions.insert": 400, "playlistItems.insert": 50,
        "playlists.list": 1, "videos.list": 1}

DEFAULTS = {
    "client_secret": "secrets/client_secret.json",
    "state_file": "uploaded.json",
    "schedule": {"timezone": "Asia/Kolkata", "days": "daily", "times": ["07:00"],
                 "short_offset_minutes": 60, "min_lead_minutes": 60, "check_channel": True},
    "metadata": {"max_tags": 14, "max_hashtags": 3, "intro_in_description": True, "extra_tags": []},
    "upload": {"mode": "schedule", "upload_short": True, "captions": True, "thumbnail": True,
               "notify_subscribers": True, "contains_synthetic_media": False,
               "playlist_privacy": "public", "create_playlist": True},
    "quota": {"daily_units": 10000, "safety_margin": 200},
    "layouts": {},
}


def deep_merge(a, b):
    out = dict(a)
    for k, v in (b or {}).items():
        out[k] = deep_merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def load_config(path: Path) -> dict:
    import yaml
    if not path.is_file():
        raise SystemExit(f"Config not found: {path}\nCopy config.example.yaml to config.yaml first.")
    cfg = deep_merge(DEFAULTS, yaml.safe_load(path.read_text(encoding="utf-8")) or {})
    base = path.resolve().parent
    cfg["_base"] = base
    return cfg


def rel(cfg, p) -> Path:
    p = Path(str(p).replace("\\", "/")) if not Path(p).is_absolute() else Path(p)
    if not p.is_absolute():
        p = cfg["_base"] / p
    return p


def channel_cfg(cfg, name):
    chans = cfg.get("channels", {})
    if name not in chans:
        raise SystemExit(f"Unknown channel '{name}'. Configured: {', '.join(chans) or 'none'}")
    ch = dict(chans[name])
    ch["schedule"] = deep_merge(cfg["schedule"], ch.get("schedule", {}))
    ch["metadata"] = deep_merge(cfg["metadata"], ch.get("metadata", {}))
    ch["upload"] = deep_merge(cfg["upload"], ch.get("upload", {}))
    ch["layout"] = cfg["layouts"].get(ch.get("layout", ""), {})
    ch.setdefault("token", f"secrets/token_{name}.json")
    ch.setdefault("category", 27)
    ch.setdefault("language", "en-IN")
    ch.setdefault("caption_name", "English (India)")
    ch.setdefault("made_for_kids", False)
    return ch


def item_cost(item, ch, has_playlist=True) -> int:
    u = ch["upload"]
    c = COST["videos.insert"] + COST["videos.list"]
    if u["thumbnail"] and item.get("thumbnail"): c += COST["thumbnails.set"]
    if u["captions"] and item.get("captions"): c += COST["captions.insert"]
    if has_playlist: c += COST["playlistItems.insert"] + COST["playlists.list"]
    if u["upload_short"] and item.get("short_video"): c += COST["videos.insert"]
    return c


def fmt_local(dt, tz):
    return dt.astimezone(ZoneInfo(tz)).strftime("%a %d %b %Y %H:%M") + f" ({tz})"


def video_body(meta, ch, privacy, publish_at=None, short=False):
    body = {
        "snippet": {"title": meta["title"], "description": meta["description"], "tags": meta["tags"],
                    "categoryId": str(ch["category"]), "defaultLanguage": ch["language"],
                    "defaultAudioLanguage": ch["language"]},
        "status": {"privacyStatus": privacy, "selfDeclaredMadeForKids": bool(ch["made_for_kids"]),
                   "embeddable": True, "license": "youtube",
                   "containsSyntheticMedia": bool(ch["upload"]["contains_synthetic_media"])},
    }
    if publish_at:
        body["status"]["privacyStatus"] = "private"      # publishAt only works on private videos
        body["status"]["publishAt"] = rfc3339_utc(publish_at)
    return body


class Runner:
    def __init__(self, cfg, channel, dry_run=False, open_browser=True):
        self.cfg, self.name, self.dry = cfg, channel, dry_run
        self.ch = channel_cfg(cfg, channel)
        self.state = State(rel(cfg, cfg["state_file"]))
        self.api = None
        self.open_browser = open_browser
        self._remote_taken = None
        self._planned = []

    def connect(self):
        if self.api or self.dry:
            return self.api
        from .api import YouTube, get_credentials
        creds = get_credentials(rel(self.cfg, self.cfg["client_secret"]), rel(self.cfg, self.ch["token"]),
                                self.open_browser)
        self.api = YouTube(creds, self.state)
        me = self.api.channel()
        want = self.ch.get("channel_id")
        title = me["snippet"]["title"] if me else "?"
        if want and me and me["id"] != want:
            raise SystemExit(f"Signed in as channel '{title}' ({me['id']}) but config expects {want}.\n"
                             f"Delete {self.ch['token']} and run `auth --channel {self.name}` again, picking the right channel.")
        print(f"  Channel: {title}")
        return self.api

    def remaining_units(self):
        q = self.cfg["quota"]
        return int(q["daily_units"]) - self.state.units_used_today() - int(q["safety_margin"])

    def taken(self):
        taken = self.state.taken_slots(self.name)
        if self.ch["schedule"].get("check_channel") and not self.dry:
            if self._remote_taken is None:
                try:
                    self._remote_taken = [from_rfc3339(v["status"]["publishAt"]) for v in self.connect().scheduled_videos()]
                except Exception as e:      # never block an upload on this check
                    print(f"  (couldn't read scheduled videos from the channel: {e})"); self._remote_taken = []
            taken += self._remote_taken
        return taken + self._planned

    def pick_time(self, at=None, now=False):
        u = self.ch["upload"]; s = self.ch["schedule"]
        if now or u["mode"] == "public":
            return "public", None
        if at:
            return "private", parse_at(at, s["timezone"])
        if u["mode"] == "private":
            return "private-only", None
        return "private", next_free_slot(s, self.taken())

    # ------------------------------------------------------------ one video
    def upload(self, item: md.VideoItem, at=None, now=False, skip_short=False) -> bool:
        ch, u, s = self.ch, self.ch["upload"], self.ch["schedule"]
        tz = s["timezone"]
        e = self.state.get(self.name, item.key) or {}
        if self.state.is_done(self.name, item.key, u["upload_short"] and not skip_short and bool(item.get("short_video"))):
            print(f"= {item.key}: already uploaded ({e['long'].get('url')}) - skipping")
            return True
        missing = [r for r in ("youtube_md", "full_video") if not item.get(r)]
        if missing:
            print(f"! {item.key}: missing {', '.join(missing)} in {item.folder} - skipping"); return False
        meta = md.build_long(item, ch["metadata"])
        playlist = ch.get("playlist") or (meta["playlists"][0] if meta["playlists"] else None)
        cost = item_cost(item, ch, bool(playlist))
        print(f"\n> {item.key}  (estimated quota {cost} units, ~{self.remaining_units()} left today)")
        if "long" in e and e["long"].get("id"):
            privacy, slot = e["long"].get("privacy", "private"), (from_rfc3339(e["long"]["publishAt"]) if e["long"].get("publishAt") else None)
        else:
            privacy, slot = self.pick_time(at, now)
            if slot:
                self._planned.append(slot)
        when = fmt_local(slot, tz) if slot else ("PUBLIC NOW" if privacy == "public" else "PRIVATE (publish later in Studio)")
        if self.dry:
            self.print_plan(item, meta, playlist, when, slot, privacy)
            return True
        if cost > self.remaining_units():
            print(f"  Not enough quota left today ({self.remaining_units()} < {cost}). Stopping; run again after "
                  f"quota resets (12:30 PM IST / midnight Pacific).")
            raise QuotaStop()
        api = self.connect()
        e = self.state.entry(self.name, item.key)
        L = e.setdefault("long", {})
        real_priv = "private" if privacy == "private-only" else privacy
        # 1. long video
        if not L.get("id"):
            body = video_body(meta, ch, real_priv, slot)
            print(f"  Uploading long video ({item.get('full_video').stat().st_size/1e6:.0f} MB) -> {when}")
            res = api.insert_video(item.get("full_video"), body, u["notify_subscribers"])
            L.update(id=res["id"], url=f"https://youtu.be/{res['id']}", privacy=real_priv,
                     publishAt=body["status"].get("publishAt"), title=meta["title"],
                     uploaded=datetime.now(timezone.utc).isoformat(timespec="seconds"))
            self.state.save()
            print(f"  Uploaded: {L['url']}")
        vid = L["id"]
        # 2. thumbnail / captions / playlist - each retried on the next run if it fails
        self.step(L, "thumbnail", u["thumbnail"] and item.get("thumbnail"),
                  lambda: api.set_thumbnail(vid, item.get("thumbnail")))
        self.step(L, "captions", u["captions"] and item.get("captions"),
                  lambda: api.insert_captions(vid, item.get("captions"), ch["language"], ch["caption_name"]))
        if playlist:
            def _pl():
                pid = api.find_or_create_playlist(playlist, u["playlist_privacy"], u["create_playlist"])
                if not pid:
                    raise RuntimeError(f"playlist '{playlist}' not found")
                api.add_to_playlist(pid, vid); L["playlist_id"] = pid
            self.step(L, "playlist", True, _pl)
        self.check_locked(vid, L, real_priv, slot)
        L["complete"] = all(L.get(k) != "error" for k in ("thumbnail", "captions", "playlist"))
        self.state.save()
        # 3. Short
        if u["upload_short"] and not skip_short and item.get("short_video"):
            S = e.setdefault("short", {})
            if not S.get("id"):
                smeta = md.build_short(item, meta, L["url"], ch["metadata"])
                s_slot = short_time(slot, s) if slot else None
                body = video_body(smeta, ch, real_priv, s_slot, short=True)
                print(f"  Uploading Short -> {fmt_local(s_slot, tz) if s_slot else when}")
                res = api.insert_video(item.get("short_video"), body, u["notify_subscribers"])
                S.update(id=res["id"], url=f"https://youtube.com/shorts/{res['id']}", title=smeta["title"],
                         publishAt=body["status"].get("publishAt"), privacy=real_priv)
                self.state.save()
                print(f"  Short: {S['url']}")
            if ch.get("shorts_playlist"):
                self.step(S, "playlist", True, lambda: api.add_to_playlist(
                    api.find_or_create_playlist(ch["shorts_playlist"], u["playlist_privacy"], u["create_playlist"]), S["id"]))
            S["complete"] = S.get("playlist") != "error"
        elif not item.get("short_video") or skip_short or not u["upload_short"]:
            e.setdefault("short", {})["skipped"] = True
        self.state.save()
        print(f"  Done: {item.key}  long={L['url']}" + (f"  short={e['short'].get('url')}" if e.get('short', {}).get('url') else ""))
        return True

    def step(self, rec, name, wanted, fn):
        if not wanted or rec.get(name) == "ok":
            return
        try:
            fn(); rec[name] = "ok"; print(f"  {name}: ok")
        except QuotaStop:
            raise
        except Exception as ex:
            from .api import QuotaExceeded
            if isinstance(ex, QuotaExceeded):
                self.state.save(); raise QuotaStop() from ex
            rec[name] = "error"; rec[f"{name}_error"] = str(ex)[:300]
            print(f"  {name}: FAILED ({str(ex)[:200]}) - will retry next run")
        self.state.save()

    def check_locked(self, vid, rec, privacy, slot):
        try:
            v = self.api.video_status(vid)
        except Exception:
            return
        st = (v or {}).get("status", {})
        rec["uploadStatus"] = st.get("uploadStatus")
        if st.get("uploadStatus") == "rejected":
            print(f"  !! YouTube rejected the upload: {st.get('rejectionReason')}")
        wanted_public = privacy == "public" or slot is not None
        if wanted_public and st.get("privacyStatus") == "private" and not st.get("publishAt"):
            rec["locked_private"] = True
            print("  !! Video is LOCKED PRIVATE by YouTube (unverified API project). Open YouTube Studio ->\n"
                  "     Content -> this video -> Visibility -> Schedule/Public. See README 'Private-locked uploads'.")

    def print_plan(self, item, meta, playlist, when, slot, privacy):
        ch = self.ch
        print(f"  Channel       : {self.name} ({ch.get('name', '')})")
        print(f"  Publish       : {when}")
        if slot and item.get("short_video") and ch["upload"]["upload_short"]:
            print(f"  Short publish : {fmt_local(short_time(slot, ch['schedule']), ch['schedule']['timezone'])}")
        print(f"  Made for kids : {ch['made_for_kids']}   Category: {ch['category']}   Language: {ch['language']}")
        print(f"  Playlist      : {playlist}")
        for r in ("full_video", "short_video", "thumbnail", "captions", "chapters", "description_override",
                  "short_description_override"):
            print(f"  {r:<14}: {item.get(r) or '-'}")
        if meta["chapter_problems"]:
            print(f"  !! chapters   : {'; '.join(meta['chapter_problems'])}")
        print(f"  Title ({len(meta['title'])}) : {meta['title']}")
        print(f"  Tags ({len(meta['tags'])})   : {', '.join(meta['tags'])}")
        print("  ---- description ----\n" + "\n".join("  | " + l for l in meta["description"].splitlines()))
        if item.get("short_video"):
            sm = md.build_short(item, meta, None, ch["metadata"])
            print(f"  ---- Short: {sm['title']} ----\n" + "\n".join("  | " + l for l in sm["description"].splitlines()))


class QuotaStop(Exception):
    pass


try:
    from .api import QuotaExceeded
    QUOTA_ERRORS = (QuotaStop, QuotaExceeded)
except Exception:  # google libs missing -> dry-run still works
    QUOTA_ERRORS = (QuotaStop,)


# ---------------------------------------------------------------- commands
def cmd_auth(cfg, a):
    r = Runner(cfg, a.channel, open_browser=not a.no_browser)
    r.connect()
    me = r.api.channel()
    print(f"OK. Profile '{a.channel}' -> channel '{me['snippet']['title']}' id {me['id']}\n"
          f"Tip: put  channel_id: {me['id']}  under channels.{a.channel} in config.yaml so uploads can never go "
          f"to the wrong channel.")


def items_for(path, name, layout):
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"Not found: {p}")
    if name:
        return [md.resolve_item(p, name=name, layout=layout)]
    if p.is_dir() and ((p / "YouTube.md").is_file()):
        return [md.resolve_item(p, layout=layout)]
    found = md.discover(p, layout)
    if not found:
        raise SystemExit(f"No YouTube.md / *_YouTube.md found in {p}")
    return found


def cmd_upload(cfg, a):
    r = Runner(cfg, a.channel, a.dry_run, not a.no_browser)
    its = items_for(a.folder, a.name, r.ch["layout"])
    if len(its) > 1:
        raise SystemExit(f"{a.folder} holds {len(its)} videos; use --name NN_Topic or the `queue` command.")
    try:
        r.upload(its[0], at=a.at, now=a.now, skip_short=a.no_short)
    except QUOTA_ERRORS:
        r.state.save()
        print("Stopped: YouTube daily quota used up. Run the same command again tomorrow - it continues where it stopped.")
        return 2
    return 0


def cmd_queue(cfg, a):
    r = Runner(cfg, a.channel, a.dry_run, not a.no_browser)
    root = a.dir or r.ch.get("series_root")
    if not root:
        raise SystemExit("Give a folder, or set series_root for this channel in config.yaml")
    its = items_for(root, None, r.ch["layout"])
    want_short = r.ch["upload"]["upload_short"]
    todo = [i for i in its if i.get("full_video") and not r.state.is_done(r.name, i.key, want_short and bool(i.get("short_video")))]
    not_ready = [i.key for i in its if not i.get("full_video")]
    print(f"{len(its)} videos found, {len(todo)} ready and not uploaded"
          + (f"; not rendered yet: {', '.join(not_ready)}" if not_ready else ""))
    if a.limit:
        todo = todo[: a.limit]
    for it in todo:
        try:
            r.upload(it)
        except QUOTA_ERRORS:
            r.state.save()
            print("Stopped for today because of quota. The rest will go next run."); return 2
    return 0


def cmd_status(cfg, a):
    st = State(rel(cfg, cfg["state_file"]))
    tz = cfg["schedule"]["timezone"]
    rows = [v for v in st.data["videos"].values() if not a.channel or v.get("channel") == a.channel]
    if not rows:
        print("Nothing uploaded yet (uploaded.json is empty).")
    for v in sorted(rows, key=lambda v: (v["channel"], v["video"])):
        L, S = v.get("long", {}), v.get("short", {})
        when = fmt_local(from_rfc3339(L["publishAt"]), tz) if L.get("publishAt") else L.get("privacy", "-")
        flags = [k for k in ("thumbnail", "captions", "playlist") if L.get(k) == "error"]
        print(f"{v['channel']:<7} {v['video']:<28} {when:<36} {L.get('url', '-'):<30} "
              f"short={S.get('url', 'skipped' if S.get('skipped') else '-')}"
              + (f"  RETRY:{','.join(flags)}" if flags else "") + ("  LOCKED-PRIVATE" if L.get("locked_private") else ""))
    print(f"Quota used today (this project, Pacific day): ~{st.units_used_today()} units")
    if a.channel:
        ch = channel_cfg(cfg, a.channel)
        print("Next free slot (local record):", fmt_local(next_free_slot(ch["schedule"], st.taken_slots(a.channel)), tz))
        if a.remote:
            r = Runner(cfg, a.channel)
            for v in r.connect().scheduled_videos():
                print(f"  scheduled on YouTube: {fmt_local(from_rfc3339(v['status']['publishAt']), tz)}  "
                      f"https://youtu.be/{v['id']}  {v['snippet']['title']}")
    return 0


def cmd_mark(cfg, a):
    """Record a video you uploaded by hand (Studio) so `queue` never uploads it twice."""
    st = State(rel(cfg, cfg["state_file"]))
    channel_cfg(cfg, a.channel)
    e = st.entry(a.channel, a.name)
    L = e.setdefault("long", {})
    L.update(id=a.long_id, url=f"https://youtu.be/{a.long_id}", complete=True, manual=True)
    if a.publish_at:
        L["publishAt"] = rfc3339_utc(parse_at(a.publish_at, cfg["schedule"]["timezone"]))
    if a.short_id:
        e["short"] = {"id": a.short_id, "url": f"https://youtube.com/shorts/{a.short_id}", "complete": True, "manual": True}
    else:
        e.setdefault("short", {})["skipped"] = True
    st.save()
    print(f"Marked {a.channel}:{a.name} as uploaded ({L['url']}).")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="yt_upload", description="Upload rendered lessons to YouTube.")
    p.add_argument("--config", default=str(HERE / "config.yaml"))
    sub = p.add_subparsers(dest="cmd", required=True)
    pa = sub.add_parser("auth", help="one-time sign-in for a channel profile")
    pa.add_argument("--channel", required=True)
    pa.add_argument("--no-browser", action="store_true")
    pu = sub.add_parser("upload", help="upload one video folder (long + Short + thumbnail + captions + playlist)")
    pu.add_argument("folder"); pu.add_argument("--channel", required=True)
    pu.add_argument("--name", help="video name in a flat folder, e.g. 02_Plants")
    pu.add_argument("--at", help='publish time, e.g. "2026-11-02 07:00" (config timezone)')
    pu.add_argument("--now", action="store_true", help="publish public immediately")
    pu.add_argument("--no-short", action="store_true")
    pu.add_argument("--dry-run", action="store_true"); pu.add_argument("--no-browser", action="store_true")
    pq = sub.add_parser("queue", help="upload every rendered video in a folder that isn't uploaded yet")
    pq.add_argument("dir", nargs="?"); pq.add_argument("--channel", required=True)
    pq.add_argument("--limit", type=int, default=0, help="max videos this run (0 = as many as quota allows)")
    pq.add_argument("--dry-run", action="store_true"); pq.add_argument("--no-browser", action="store_true")
    ps = sub.add_parser("status", help="what's uploaded / scheduled")
    ps.add_argument("--channel"); ps.add_argument("--remote", action="store_true", help="also ask YouTube")
    pm = sub.add_parser("mark", help="record a video already uploaded by hand")
    pm.add_argument("name", help="video name, e.g. 02_Plants"); pm.add_argument("--channel", required=True)
    pm.add_argument("--long-id", required=True); pm.add_argument("--short-id")
    pm.add_argument("--publish-at", help='e.g. "2026-11-01 07:00" if it is scheduled')
    a = p.parse_args(argv)
    cfg = load_config(Path(a.config))
    try:
        return {"auth": cmd_auth, "upload": cmd_upload, "queue": cmd_queue, "status": cmd_status, "mark": cmd_mark}[a.cmd](cfg, a) or 0
    except KeyboardInterrupt:
        print("\nStopped. Re-run the same command to continue where it left off."); return 130


if __name__ == "__main__":
    sys.exit(main())
