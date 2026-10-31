"""Thin wrapper over the YouTube Data API v3 with resumable uploads and retries."""
from __future__ import annotations

import http.client
import random
import socket
import time
from pathlib import Path

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",     # videos.insert
    "https://www.googleapis.com/auth/youtube",            # playlists, thumbnails, videos.list mine
    "https://www.googleapis.com/auth/youtube.force-ssl",  # captions.insert
]
RETRY_STATUS = {500, 502, 503, 504}
RETRY_EXC = (http.client.HTTPException, socket.error, ConnectionError, TimeoutError)
CHUNK = 8 * 1024 * 1024

# Quota unit costs (developers.google.com/youtube/v3/determine_quota_cost)
COST = {"videos.insert": 1600, "thumbnails.set": 50, "captions.insert": 400,
        "playlistItems.insert": 50, "playlists.insert": 50, "playlists.list": 1,
        "videos.list": 1, "videos.update": 50, "channels.list": 1, "playlistItems.list": 1}


class QuotaExceeded(Exception):
    pass


def _reason(err) -> str:
    try:
        import json
        d = json.loads(err.content.decode())
        return d["error"]["errors"][0].get("reason", "")
    except Exception:
        return ""


def get_credentials(client_secret: Path, token_file: Path, open_browser=True):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.exceptions import RefreshError

    creds = None
    if token_file.is_file():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            token_file.write_text(creds.to_json(), encoding="utf-8")
            return creds
        except RefreshError:
            print("  Saved sign-in has expired (testing-mode tokens last 7 days). Signing in again...")
    if not client_secret.is_file():
        raise SystemExit(f"client_secret.json not found at {client_secret}. See SETUP_GOOGLE.md step 5.")
    flow = InstalledAppFlow.from_client_secrets_file(str(client_secret), SCOPES)
    print("  A Google sign-in page will open. Pick your Google account, then PICK THE CHANNEL\n"
          "  (brand account) this profile is for, and allow access.")
    creds = flow.run_local_server(port=0, open_browser=open_browser, prompt="consent",
                                  authorization_prompt_message="  If no browser opened, open this URL: {url}")
    token_file.parent.mkdir(parents=True, exist_ok=True)
    token_file.write_text(creds.to_json(), encoding="utf-8")
    return creds


class YouTube:
    def __init__(self, creds, state=None):
        from googleapiclient.discovery import build
        self.yt = build("youtube", "v3", credentials=creds, cache_discovery=False)
        self.state = state

    # -------- helpers
    def _exec(self, req, method):
        from googleapiclient.errors import HttpError
        for attempt in range(6):
            try:
                res = req.execute()
                if self.state:
                    self.state.add_units(COST.get(method, 1))
                return res
            except HttpError as e:
                r = _reason(e)
                if e.resp.status == 403 and r in ("quotaExceeded", "dailyLimitExceeded", "uploadLimitExceeded",
                                                   "rateLimitExceeded"):
                    raise QuotaExceeded(r)
                if e.resp.status in RETRY_STATUS and attempt < 5:
                    self._sleep(attempt, f"{method} HTTP {e.resp.status}")
                    continue
                raise
            except RETRY_EXC as e:
                if attempt < 5:
                    self._sleep(attempt, f"{method} {e!r}")
                    continue
                raise

    @staticmethod
    def _sleep(attempt, why):
        wait = min(64, 2 ** attempt) + random.random()
        print(f"    retry in {wait:.0f}s ({why})")
        time.sleep(wait)

    def _resumable(self, req, label, method):
        from googleapiclient.errors import HttpError
        response, errors, last = None, 0, -1
        while response is None:
            try:
                status, response = req.next_chunk()
                if status:
                    pct = int(status.progress() * 100)
                    if pct // 10 != last // 10:
                        print(f"    {label}: {pct}%"); last = pct
                errors = 0
            except HttpError as e:
                r = _reason(e)
                if e.resp.status == 403 and r in ("quotaExceeded", "uploadLimitExceeded", "dailyLimitExceeded"):
                    raise QuotaExceeded(r)
                if e.resp.status not in RETRY_STATUS or errors >= 10:
                    raise
                errors += 1; self._sleep(errors, f"HTTP {e.resp.status}")
            except RETRY_EXC as e:
                if errors >= 10:
                    raise
                errors += 1; self._sleep(errors, repr(e))
        if self.state:
            self.state.add_units(COST.get(method, 1))
        return response

    # -------- API calls
    def channel(self):
        r = self._exec(self.yt.channels().list(part="snippet,contentDetails,status", mine=True), "channels.list")
        return r["items"][0] if r.get("items") else None

    def insert_video(self, path: Path, body: dict, notify=True):
        from googleapiclient.http import MediaFileUpload
        media = MediaFileUpload(str(path), chunksize=CHUNK, resumable=True, mimetype="video/*")
        req = self.yt.videos().insert(part="snippet,status", body=body, media_body=media,
                                      notifySubscribers=notify)
        return self._resumable(req, path.name, "videos.insert")

    def set_thumbnail(self, video_id, path: Path):
        from googleapiclient.http import MediaFileUpload
        mt = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        return self._exec(self.yt.thumbnails().set(videoId=video_id, media_body=MediaFileUpload(str(path), mimetype=mt)),
                          "thumbnails.set")

    def insert_captions(self, video_id, path: Path, language="en-IN", name="English (India)"):
        from googleapiclient.http import MediaFileUpload
        body = {"snippet": {"videoId": video_id, "language": language, "name": name, "isDraft": False}}
        return self._exec(self.yt.captions().insert(part="snippet", body=body, sync=False,
                          media_body=MediaFileUpload(str(path), mimetype="application/octet-stream")),
                          "captions.insert")

    def find_or_create_playlist(self, title_or_id: str, privacy="public", create=True):
        if title_or_id.startswith(("PL", "UU", "OL")) and " " not in title_or_id:
            return title_or_id
        token = None
        while True:
            r = self._exec(self.yt.playlists().list(part="snippet", mine=True, maxResults=50, pageToken=token),
                           "playlists.list")
            for p in r.get("items", []):
                if p["snippet"]["title"].strip().lower() == title_or_id.strip().lower():
                    return p["id"]
            token = r.get("nextPageToken")
            if not token:
                break
        if not create:
            return None
        body = {"snippet": {"title": title_or_id[:150]}, "status": {"privacyStatus": privacy}}
        return self._exec(self.yt.playlists().insert(part="snippet,status", body=body), "playlists.insert")["id"]

    def add_to_playlist(self, playlist_id, video_id):
        body = {"snippet": {"playlistId": playlist_id, "resourceId": {"kind": "youtube#video", "videoId": video_id}}}
        return self._exec(self.yt.playlistItems().insert(part="snippet", body=body), "playlistItems.insert")

    def video_status(self, video_id):
        r = self._exec(self.yt.videos().list(part="status,snippet", id=video_id), "videos.list")
        return r["items"][0] if r.get("items") else None

    def update_description(self, video_id, snippet: dict):
        return self._exec(self.yt.videos().update(part="snippet", body={"id": video_id, "snippet": snippet}),
                          "videos.update")

    def scheduled_videos(self, max_pages=2):
        """Recent uploads that are private with a publishAt in the future (cheap: ~1 unit per 50)."""
        ch = self.channel()
        uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]
        ids, token = [], None
        for _ in range(max_pages):
            r = self._exec(self.yt.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=50,
                                                        pageToken=token), "playlistItems.list")
            ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
            token = r.get("nextPageToken")
            if not token:
                break
        out = []
        for i in range(0, len(ids), 50):
            r = self._exec(self.yt.videos().list(part="status,snippet", id=",".join(ids[i:i + 50])), "videos.list")
            for v in r.get("items", []):
                if v["status"].get("publishAt"):
                    out.append(v)
        return out
