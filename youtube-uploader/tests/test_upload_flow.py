"""Upload flow against a fake YouTube API (no network, no credentials)."""
import os
from pathlib import Path

import pytest

from ytup import cli, metadata as md

FLAT = Path(os.environ.get("YTUP_TEST_FLAT", "/workspace/hl_upload"))
pytestmark = pytest.mark.skipif(not (FLAT / "02_Plants_YouTube.md").is_file(), reason="no flat sample")


class FakeAPI:
    def __init__(self):
        self.calls, self.n = [], 0
    def channel(self): return {"id": "UC1", "snippet": {"title": "Happy Learners ICSE"}}
    def insert_video(self, path, body, notify=True):
        self.n += 1; self.calls.append(("insert", path.name, body)); return {"id": f"vid{self.n}"}
    def set_thumbnail(self, vid, p): self.calls.append(("thumb", vid))
    def insert_captions(self, vid, p, lang, name): self.calls.append(("captions", vid, lang))
    def find_or_create_playlist(self, t, privacy, create): return "PL123"
    def add_to_playlist(self, pid, vid): self.calls.append(("playlist", pid, vid))
    def video_status(self, vid): return {"status": {"privacyStatus": "private", "publishAt": "x", "uploadStatus": "uploaded"}}
    def scheduled_videos(self): return []


def make_runner(tmp_path):
    cfg = cli.deep_merge(cli.DEFAULTS, {"channels": {"happy": {"made_for_kids": True,
                         "playlist": "Class 2 Science Olympiad (NSO/ISO) – Full Course"}}})
    cfg["_base"] = tmp_path
    r = cli.Runner(cfg, "happy")
    r.api = FakeAPI()
    return r


def test_upload_and_idempotent(tmp_path):
    r = make_runner(tmp_path)
    it = md.resolve_item(FLAT, name="02_Plants")
    r.upload(it)
    kinds = [c[0] for c in r.api.calls]
    assert kinds == ["insert", "thumb", "captions", "playlist", "insert"]
    long_body, short_body = r.api.calls[0][2], r.api.calls[4][2]
    assert long_body["status"]["privacyStatus"] == "private" and long_body["status"]["publishAt"].endswith("Z")
    assert long_body["status"]["selfDeclaredMadeForKids"] is True
    assert long_body["snippet"]["categoryId"] == "27" and long_body["snippet"]["defaultLanguage"] == "en-IN"
    assert "Full lesson: https://youtu.be/vid1" in short_body["snippet"]["description"]
    assert short_body["status"]["publishAt"] > long_body["status"]["publishAt"]
    # second run does nothing
    r.api.calls.clear(); r.upload(it); assert r.api.calls == []
    # next video gets the next day
    it1 = md.resolve_item(FLAT, name="01_Intro")
    r.upload(it1)
    b = r.api.calls[0][2]
    assert b["status"]["publishAt"] != long_body["status"]["publishAt"]


def test_now_is_public(tmp_path):
    r = make_runner(tmp_path)
    r.upload(md.resolve_item(FLAT, name="01_Intro"), now=True)
    b = r.api.calls[0][2]
    assert b["status"]["privacyStatus"] == "public" and "publishAt" not in b["status"]


def test_failed_step_retried(tmp_path):
    r = make_runner(tmp_path)
    def boom(*a): raise RuntimeError("captions broke")
    r.api.insert_captions = boom
    it = md.resolve_item(FLAT, name="01_Intro")
    r.upload(it)
    e = r.state.get("happy", "01_Intro")
    assert e["long"]["captions"] == "error" and not e["long"]["complete"]
    r.api = FakeAPI(); r.upload(it)
    assert [c[0] for c in r.api.calls] == ["captions"]     # only the failed step, no re-upload
    assert r.state.get("happy", "01_Intro")["long"]["complete"]


def test_quota_stop(tmp_path):
    r = make_runner(tmp_path)
    r.state.add_units(9000)
    with pytest.raises(cli.QuotaStop):
        r.upload(md.resolve_item(FLAT, name="01_Intro"))
    assert r.api.calls == []
