"""Run:  python -m pytest tests -q
Uses real render outputs when available (YTUP_TEST_FLAT, YTUP_TEST_REPO env vars or the box paths)
and a small synthetic folder otherwise."""
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from ytup import metadata as md
from ytup.schedule import next_free_slot, short_time, rfc3339_utc, parse_at
from ytup.state import State

FLAT = Path(os.environ.get("YTUP_TEST_FLAT", "/workspace/hl_upload"))
REPO = Path(os.environ.get("YTUP_TEST_REPO", "/tmp/hsc/Grade2/Science-Olympiad"))
need_flat = pytest.mark.skipif(not (FLAT / "02_Plants_YouTube.md").is_file(), reason="no flat sample")
need_repo = pytest.mark.skipif(not (REPO / "02_Plants" / "YouTube.md").is_file(), reason="no repo sample")
IST = ZoneInfo("Asia/Kolkata")
SCHED = {"timezone": "Asia/Kolkata", "days": "daily", "times": ["07:00"], "short_offset_minutes": 60,
         "min_lead_minutes": 60}
OPTS = {"max_tags": 14, "max_hashtags": 3}


@need_repo
def test_parse_youtube_md_repo():
    for v in ("01_Intro", "02_Plants"):
        y = md.parse_youtube_md(REPO / v / "YouTube.md")
        assert 20 < len(y["title"]) <= 100
        assert "Chapters" in y["description"] and "0:00" in y["description"]
        assert len(y["tags"]) >= 8 and all("," not in t for t in y["tags"])
        assert y["playlists"][0].startswith("Class 2 Science Olympiad")
        assert y["hashtags"] and all(h.startswith("#") for h in y["hashtags"])


@need_repo
def test_intro_text():
    t = md.parse_intro_text(REPO / "01_Intro" / "Intro_Outro.md")
    assert t.startswith("Hello, Happy Learners!") and "five smart tips" in t


@need_flat
def test_chapters_and_srt():
    ch = md.parse_chapters(FLAT / "02_Plants_full_chapters.txt")
    assert ch[0].startswith("0:00") and len(ch) >= 3
    assert md.validate_chapters(ch) == []
    cues = md.parse_srt(FLAT / "02_Plants_full.srt")
    assert len(cues) > 5 and "-->" not in cues[0][2]
    assert md.validate_chapters(["0:05 a", "0:08 b"])   # problems reported


@need_flat
def test_flat_layout_build():
    items = md.discover(FLAT)
    keys = [i.key for i in items]
    assert keys[:2] == ["01_Intro", "02_Plants"]
    it = items[1]
    for r in ("full_video", "short_video", "thumbnail", "captions", "chapters", "description_override"):
        assert it.get(r), r
    m = md.build_long(it, OPTS)
    assert m["title"].startswith("Plants for Kids")
    assert "1:04 Parts of a plant" in m["description"]
    assert len(m["description"].splitlines()[-1].split()) <= 3
    assert len(m["tags"]) <= 14 and "<" not in m["description"]
    s = md.build_short(it, m, "https://youtu.be/XYZ", OPTS)
    assert "Full lesson: https://youtu.be/XYZ" in s["description"]
    assert "#Shorts" in s["description"] and s["title"].lower().endswith("#shorts")
    assert s["title"].startswith("Do plants eat food?")


@need_repo
@need_flat
def test_folder_layout_with_render_dir(tmp_path):
    """Repo layout: 02_Plants/YouTube.md + render/02_Plants_full.mp4 ... (no override -> built description)."""
    v = tmp_path / "02_Plants"; (v / "render").mkdir(parents=True)
    shutil.copy(REPO / "02_Plants" / "YouTube.md", v / "YouTube.md")
    shutil.copy(REPO / "02_Plants" / "Intro_Outro.md", v / "Intro_Outro.md")
    for suf in ("_full_chapters.txt", "_full.srt", "_thumb.jpg"):
        shutil.copy(FLAT / f"02_Plants{suf}", v / "render" / f"02_Plants{suf}")
    (v / "render" / "02_Plants_full.mp4").write_bytes(b"x"); (v / "render" / "02_Plants_short.mp4").write_bytes(b"x")
    it = md.discover(tmp_path)[0]
    assert it.key == "02_Plants" and it.get("full_video").parent.name == "render"
    assert it.get("description_override") is None
    m = md.build_long(it, OPTS)
    assert m["description"].startswith("Hello, Happy Learners!")         # intro text first
    assert "1:04 Parts of a plant" in m["description"]                    # real render chapters
    assert "1:00 Parts" not in m["description"]                           # planned chapters replaced
    assert m["description"].rstrip().splitlines()[-1].count("#") == 3     # 3 hashtags
    s = md.build_short(it, m, "https://youtu.be/ABC", OPTS)
    assert "Full lesson: https://youtu.be/ABC" in s["description"] and "#Shorts" in s["description"]


def test_slots_basic():
    now = datetime(2026, 10, 31, 23, 30, tzinfo=IST)
    s1 = next_free_slot(SCHED, [], now)
    assert s1 == datetime(2026, 11, 1, 7, 0, tzinfo=IST)
    s2 = next_free_slot(SCHED, [s1], now)
    assert s2 == datetime(2026, 11, 2, 7, 0, tzinfo=IST)
    assert short_time(s1, SCHED) == datetime(2026, 11, 1, 8, 0, tzinfo=IST)
    assert rfc3339_utc(s1) == "2026-11-01T01:30:00.000Z"


def test_slots_lead_time_and_days():
    now = datetime(2026, 11, 1, 6, 30, tzinfo=IST)          # 07:00 is <60 min away -> next day
    assert next_free_slot(SCHED, [], now).day == 2
    sch = {**SCHED, "days": ["sat", "tue"], "times": ["17:00", "07:00"]}
    s = next_free_slot(sch, [], datetime(2026, 10, 31, 8, 0, tzinfo=IST))   # Sat 08:00
    assert (s.weekday(), s.hour) == (5, 17)
    s = next_free_slot(sch, [s], datetime(2026, 10, 31, 8, 0, tzinfo=IST))
    assert (s.weekday(), s.hour, s.day) == (1, 7, 3)


def test_parse_at():
    assert parse_at("2026-11-02 07:00", "Asia/Kolkata") == datetime(2026, 11, 2, 7, 0, tzinfo=IST)


def test_state_roundtrip(tmp_path):
    st = State(tmp_path / "u.json")
    e = st.entry("happy", "02_Plants")
    e["long"] = {"id": "x", "publishAt": "2026-11-01T01:30:00.000Z", "complete": True}
    e["short"] = {"id": "y", "complete": True}
    st.save()
    st2 = State(tmp_path / "u.json")
    assert st2.is_done("happy", "02_Plants")
    assert not st2.is_done("build", "02_Plants")
    assert st2.taken_slots("happy")[0] == datetime(2026, 11, 1, 1, 30, tzinfo=timezone.utc)
    s = next_free_slot(SCHED, st2.taken_slots("happy"), datetime(2026, 10, 31, 23, 0, tzinfo=IST))
    assert s.day == 2


def test_tag_limits():
    tags = [f"tag number {i}" for i in range(40)] + ["Tag Number 1"]
    out = md.fit_tags(tags, 14)
    assert len(out) == 14 and sum(len(t) + 3 for t in out) < 500
