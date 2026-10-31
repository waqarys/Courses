"""Python-for-Kids layout: lessons/01_Hello_World/YouTube.md + render/ outputs (branch python-kids-fast-pipeline)."""
import os, shutil, subprocess
from pathlib import Path
import pytest, yaml
from ytup import cli, metadata as md

DEMO = Path(os.environ.get("YTUP_TEST_PYDEMO", "/workspace/py_kids_demo"))
LESSON = Path(os.environ.get("YTUP_TEST_PYLESSON", "/tmp/pykids/lessons/01_Hello_World"))
HERE = Path(__file__).resolve().parent.parent
pytestmark = pytest.mark.skipif(not ((DEMO / "01_Hello_World_full.mp4").is_file() and (LESSON / "YouTube.md").is_file()),
                                reason="no python-kids sample")


def lessons(tmp_path):
    v = tmp_path / "lessons" / "01_Hello_World"; (v / "render").mkdir(parents=True)
    for f in ("YouTube.md", "Intro_Outro.md"):
        shutil.copy(LESSON / f, v / f)
    for f in DEMO.glob("01_Hello_World_*"):
        os.symlink(f, v / "render" / f.name)
    return tmp_path / "lessons"


def layout():
    return yaml.safe_load((HERE / "config.example.yaml").read_text(encoding="utf-8"))["layouts"]["python_kids"]


def test_files_and_metadata(tmp_path):
    it = md.discover(lessons(tmp_path), layout())[0]
    assert it.key == "01_Hello_World"
    for role, fname in {"full_video": "_full.mp4", "short_video": "_short.mp4", "captions": "_full.srt",
                        "chapters": "_chapters.txt", "thumbnail": "_thumb.jpg"}.items():
        assert it.get(role) and it.get(role).name == "01_Hello_World" + fname, role
    m = md.build_long(it, {"max_tags": 14, "max_hashtags": 3})
    assert m["title"].startswith("Hello, World | Python for Kids")
    d = m["description"]
    assert d.startswith("Hello, Happy Learners! Welcome to Python for Kids.")
    assert "paste render" not in d and "0:00 Intro" in d and "0:49 Let's code: Hello, World!" in d
    assert d.index("0:00 Intro") < d.index("📚 Playlist")
    assert d.rstrip().splitlines()[-1] == "#Python #PythonForKids #CodingForKids"
    assert m["playlists"][0].startswith("Python for Kids – Full Course")
    assert m["chapter_problems"] == []
    s = md.build_short(it, m, "https://youtu.be/T1", {"max_hashtags": 3})
    assert "Full lesson: https://youtu.be/T1" in s["description"] and "#Shorts" in s["description"]


def test_cli_dry_run(tmp_path):
    root = lessons(tmp_path)
    cfg = yaml.safe_load((HERE / "config.example.yaml").read_text(encoding="utf-8"))
    cfg["channels"]["build"]["series_root"] = str(root)
    cfg["state_file"] = str(tmp_path / "uploaded.json")
    (tmp_path / "config.yaml").write_text(yaml.safe_dump(cfg, allow_unicode=True), encoding="utf-8")
    out = subprocess.run(["python", str(HERE / "yt_upload.py"), "--config", str(tmp_path / "config.yaml"), "upload",
                          str(root / "01_Hello_World"), "--channel", "build", "--dry-run"],
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
    assert "01_Hello_World_full.mp4" in out and "01_Hello_World_short.mp4" in out
    assert "Playlist      : Python for Kids" in out and "17:00" in out
    assert not (tmp_path / "uploaded.json").exists()       # dry-run writes nothing
