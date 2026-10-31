"""Find a video's files and build its YouTube metadata from the render pipeline outputs.

Two layouts are supported:
  * folder layout (repo):  <series>/02_Plants/YouTube.md, Intro_Outro.md, render/02_Plants_full.mp4 ...
  * flat layout (staging): <dir>/02_Plants_YouTube.md, 02_Plants_full.mp4, 02_desc.txt, 02s_desc.txt ...
File name patterns come from the layout block in config.yaml ({name} = folder name e.g. 02_Plants,
{num} = leading number e.g. 02).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_LAYOUT = {
    "render_dirs": ["render", "."],
    "youtube_md": ["YouTube.md", "{name}_YouTube.md", "build/YouTube.md"],
    "intro_outro_md": ["Intro_Outro.md", "{name}_Intro_Outro.md"],
    "full_video": ["{name}_full.mp4", "{name}.mp4"],
    "short_video": ["{name}_short.mp4"],
    "captions": ["{name}_full.srt", "{name}.srt"],
    "chapters": ["{name}_full_chapters.txt", "{name}_chapters.txt"],
    "thumbnail": ["{name}_thumb.jpg", "{name}_thumb.png", "thumbnail.jpg", "thumbnail.png"],
    # optional hand-written overrides (used as-is when present)
    "description_override": ["{num}_desc.txt", "{name}_desc.txt", "description.txt"],
    "short_description_override": ["{num}s_desc.txt", "{name}_short_desc.txt", "short_description.txt"],
    "short_title_override": ["{name}_short_title.txt", "short_title.txt"],
}

TIME_RE = re.compile(r"^\s*(\d{1,2}:)?\d{1,2}:\d{2}\s+\S")


@dataclass
class VideoItem:
    key: str                 # e.g. 02_Plants
    folder: Path             # where the item lives
    files: dict = field(default_factory=dict)   # role -> Path or None

    def get(self, role):
        return self.files.get(role)


def _num(name: str) -> str:
    m = re.match(r"(\d+)", name)
    return m.group(1) if m else name


def _find(base: Path, dirs, patterns, name):
    for d in dirs:
        for p in patterns:
            f = (base / d / p.format(name=name, num=_num(name))).resolve()
            if f.is_file():
                return f
    return None


def resolve_item(path: Path, name: str | None = None, layout: dict | None = None) -> VideoItem:
    """path = a video folder (folder layout) or a staging dir + name (flat layout)."""
    lay = {**DEFAULT_LAYOUT, **(layout or {})}
    path = Path(path)
    name = name or path.name
    dirs_md = ["."]
    dirs_media = lay["render_dirs"]
    files = {
        "youtube_md": _find(path, dirs_md, lay["youtube_md"], name),
        "intro_outro_md": _find(path, dirs_md, lay["intro_outro_md"], name),
        "full_video": _find(path, dirs_media, lay["full_video"], name),
        "short_video": _find(path, dirs_media, lay["short_video"], name),
        "captions": _find(path, dirs_media, lay["captions"], name),
        "chapters": _find(path, dirs_media, lay["chapters"], name),
        "thumbnail": _find(path, dirs_media, lay["thumbnail"], name),
        "description_override": _find(path, ["."] + dirs_media, lay["description_override"], name),
        "short_description_override": _find(path, ["."] + dirs_media, lay["short_description_override"], name),
        "short_title_override": _find(path, ["."] + dirs_media, lay["short_title_override"], name),
    }
    return VideoItem(key=name, folder=path, files=files)


def discover(root: Path, layout: dict | None = None) -> list[VideoItem]:
    """All video items under root: subfolders with a YouTube.md, or flat NN_Name_YouTube.md files."""
    root = Path(root)
    items: dict[str, VideoItem] = {}
    if (root / "YouTube.md").is_file():
        it = resolve_item(root, layout=layout)
        return [it]
    for sub in sorted(p for p in root.iterdir() if p.is_dir()):
        if (sub / "YouTube.md").is_file() or any(sub.glob("*_YouTube.md")):
            it = resolve_item(sub, layout=layout)
            items[it.key] = it
    for md in sorted(root.glob("*_YouTube.md")):
        name = md.name[: -len("_YouTube.md")]
        items.setdefault(name, resolve_item(root, name=name, layout=layout))
    return sorted(items.values(), key=lambda i: i.key)


# ---------------------------------------------------------------- parsing
def md_sections(text: str) -> dict[str, str]:
    """'## Heading (anything)' -> body text. Heading key is lower-cased, parenthesis removed."""
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if cur is not None:
                out[cur] = "\n".join(buf).strip()
            cur = re.sub(r"\s*\(.*?\)", "", m.group(1)).strip().lower()
            buf = []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf).strip()
    return out


def _unfence(s: str) -> str:
    m = re.search(r"```[a-z]*\n(.*?)\n```", s, re.S)
    return (m.group(1) if m else s).strip()


def parse_youtube_md(path: Path) -> dict:
    sec = md_sections(Path(path).read_text(encoding="utf-8"))
    title = next((l.strip() for l in sec.get("title", "").splitlines() if l.strip()), "")
    desc = _unfence(sec.get("description", ""))
    tags_raw = sec.get("tags", "")
    tags = [t.strip().strip("`") for t in re.split(r"[,\n]", tags_raw) if t.strip() and not t.strip().startswith("#")]
    tags = [re.sub(r"^[-*]\s*", "", t) for t in tags]
    playlists = [re.sub(r"^[-*]\s*", "", l).strip() for l in sec.get("playlist", "").splitlines() if l.strip().startswith(("-", "*"))]
    if not playlists:   # e.g. "📚 Playlist: Python for Kids – Full Course (...)" inside the description
        m = re.search(r"Playlist:\s*(.+)", desc)
        if m:
            playlists = [m.group(1).strip()]
    hashtags = re.findall(r"#\w+", desc.splitlines()[-1]) if desc else []
    short_title = next((l.strip() for l in sec.get("short title", "").splitlines() if l.strip()), "")
    return {"title": title, "description": desc, "tags": tags, "playlists": playlists,
            "hashtags": hashtags, "short_title": short_title}


def parse_intro_text(path: Path | None) -> str:
    """The quoted '> ...' lines under '## INTRO' in Intro_Outro.md."""
    if not path:
        return ""
    sec = md_sections(Path(path).read_text(encoding="utf-8"))
    body = sec.get("intro", "")
    quote = [l.lstrip("> ").strip() for l in body.splitlines() if l.startswith(">")]
    return " ".join(q for q in quote if q)


def parse_chapters(path: Path | None) -> list[str]:
    if not path:
        return []
    return [l.strip() for l in Path(path).read_text(encoding="utf-8").splitlines() if TIME_RE.match(l)]


def validate_chapters(lines: list[str]) -> list[str]:
    """YouTube rules: first at 0:00, >=3 chapters, each >=10 s. Returns problems (empty = ok)."""
    probs = []
    secs = []
    for l in lines:
        t = l.split()[0].split(":")
        secs.append(sum(int(x) * 60 ** i for i, x in enumerate(reversed(t))))
    if not secs:
        return ["no chapters"]
    if secs[0] != 0:
        probs.append("first chapter must start at 0:00")
    if len(secs) < 3:
        probs.append("need at least 3 chapters")
    for a, b in zip(secs, secs[1:]):
        if b - a < 10:
            probs.append(f"chapter at {b//60}:{b%60:02d} is <10 s after previous")
    return probs


def parse_srt(path: Path) -> list[tuple[str, str, str]]:
    """Light SRT validation/parsing: list of (start, end, text)."""
    txt = Path(path).read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    cues = []
    for block in re.split(r"\n\s*\n", txt.strip()):
        lines = block.strip().split("\n")
        if len(lines) >= 2 and "-->" in lines[1]:
            a, b = [x.strip() for x in lines[1].split("-->")]
            cues.append((a, b, " ".join(lines[2:]).strip()))
    return cues


# ---------------------------------------------------------------- building
def _clean(s: str) -> str:
    return s.replace("<", "‹").replace(">", "›")   # YouTube rejects < and > in title/description


def replace_chapters(desc: str, chapters: list[str]) -> str:
    """Swap the timestamp lines in a description for the real render chapters."""
    if not chapters:
        return desc
    lines = desc.splitlines()
    idx = [i for i, l in enumerate(lines) if TIME_RE.match(l)]
    ph = [i for i, l in enumerate(lines) if re.match(r"^\W*chapters\b", l.strip(), re.I)]
    if not idx and ph:   # placeholder line, e.g. "⏱️ Chapters: paste render/<lesson>_chapters.txt here"
        i = ph[0]
        head = lines[i].split(":")[0].strip() if ":" in lines[i] else lines[i].strip()
        return "\n".join(lines[:i] + [head] + chapters + lines[i + 1:])
    if not idx:
        return desc + "\n\n⏱️ Chapters\n" + "\n".join(chapters)
    return "\n".join(lines[: idx[0]] + chapters + lines[idx[-1] + 1:])


def limit_hashtags(desc: str, n: int) -> str:
    lines = desc.rstrip().splitlines()
    if lines and lines[-1].strip().startswith("#"):
        tags = re.findall(r"#\w+", lines[-1])[:n]
        lines[-1] = " ".join(tags)
    return "\n".join(lines)


def fit_tags(tags: list[str], max_tags: int, max_chars: int = 480) -> list[str]:
    out, total, seen = [], 0, set()
    for t in tags:
        t = _clean(t).strip()
        if not t or t.lower() in seen:
            continue
        cost = len(t) + (2 if " " in t else 0) + 1      # YouTube counts quotes around multi-word tags
        if len(out) >= max_tags or total + cost > max_chars:
            break
        out.append(t); seen.add(t.lower()); total += cost
    return out


def build_long(item: VideoItem, opts: dict) -> dict:
    """opts: max_tags, max_hashtags, extra_tags, intro_in_description."""
    ymd = item.get("youtube_md")
    if not ymd:
        raise FileNotFoundError(f"{item.key}: YouTube.md not found in {item.folder}")
    y = parse_youtube_md(ymd)
    chapters = parse_chapters(item.get("chapters"))
    if item.get("description_override"):
        desc = item.get("description_override").read_text(encoding="utf-8").strip()
    else:
        desc = replace_chapters(y["description"], chapters)
        intro = parse_intro_text(item.get("intro_outro_md")) if opts.get("intro_in_description", True) else ""
        if intro and intro not in desc:
            desc = intro + "\n\n" + desc
    desc = limit_hashtags(desc, opts.get("max_hashtags", 3))
    tags = fit_tags(y["tags"] + list(opts.get("extra_tags", [])), opts.get("max_tags", 14))
    title = _clean(y["title"])[:100]
    return {"title": title, "description": _clean(desc)[:4900], "tags": tags,
            "playlists": y["playlists"], "hashtags": y["hashtags"], "short_title": y["short_title"],
            "chapters": chapters, "chapter_problems": validate_chapters(chapters) if chapters else []}


def _first_question(path: Path) -> str:
    """'Do plants eat food? 🌱 A quick...' -> 'Do plants eat food? 🌱' (good Short title)."""
    m = re.match(r"\s*([^.!?\n]{8,70}[?!])((?:\s*[^\w\s#\"'(]{1,2})*)", Path(path).read_text(encoding="utf-8"))
    return (m.group(1) + m.group(2)).strip() if m else ""


def build_short(item: VideoItem, long_meta: dict, full_url: str | None, opts: dict) -> dict:
    tmpl = opts.get("short_template",
                    "{hook}\n\nFull lesson: {full_url}\n\n#Shorts {hashtags}")
    if item.get("short_title_override"):
        title = item.get("short_title_override").read_text(encoding="utf-8").strip()
    elif long_meta.get("short_title"):
        title = long_meta["short_title"]
    elif item.get("short_description_override") and _first_question(item.get("short_description_override")):
        title = _first_question(item.get("short_description_override"))
    else:
        base = long_meta["title"].split("|")[0].split("–")[0].strip()
        title = f"{base} #shorts"
    url_line = f"Full lesson: {full_url}" if full_url else "Full lesson: (link added after the long video uploads)"
    if item.get("short_description_override"):
        body = item.get("short_description_override").read_text(encoding="utf-8").strip()
        lines = body.splitlines()
        if lines and lines[-1].strip().startswith("#"):
            desc = "\n".join(lines[:-1]).rstrip() + f"\n\n{url_line}\n\n" + lines[-1].strip()
        else:
            desc = body + f"\n\n{url_line}"
        if "#shorts" not in desc.lower():
            desc += "\n#Shorts"
    else:
        hook = long_meta["description"].split("\n\n")[0]
        hashtags = " ".join(h for h in long_meta["hashtags"][: opts.get("max_hashtags", 3) - 1])
        desc = tmpl.format(hook=hook, full_url=full_url or "(pending)", hashtags=hashtags,
                           title=long_meta["title"])
        if not full_url:
            desc = desc.replace("Full lesson: (pending)", url_line)
    if "#shorts" not in title.lower() and len(title) <= 90:
        title += " #shorts"
    return {"title": _clean(title)[:100], "description": _clean(desc)[:4900],
            "tags": long_meta["tags"][:10] + ["shorts"]}
