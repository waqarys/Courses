#!/usr/bin/env python3
"""prep_module.py — turn a module folder into recording + upload outputs (Python 3.8+, stdlib only).

Usage (from build-your-first-llm/):
  python tools/prep_module.py 05                 # one module (number or folder name)
  python tools/prep_module.py --all              # every module
  python tools/prep_module.py 05 --durations D:/ZeroToLLM/M05/takes
        # read real clip lengths (needs ffprobe on PATH, ships with ffmpeg) and rewrite chapter times

Writes build/<module>/ :
  teleprompter.txt   plain beats, one per paragraph (paste into any teleprompter app)
  teleprompter.html  open in a browser on a second screen: big text, auto-scroll (Space = pause, ↑/↓ speed, M = mirror)
  shot_list.md       segment table: OBS scene, target length, take filename, checkbox
  snippets/          copy of the module snippets + PASTE_ORDER.txt
  upload.json        title, description, tags, playlist, chapters — hand this to Grok Bot for a Private upload
  description.txt    the description alone (copy-paste into YouTube Studio)
"""
import argparse, html, json, pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODS = ROOT / "modules"
SEG_RE = re.compile(r"^## S(\d+) · (\w+) · (.+?) \(≈([\d.]+) ?(s|min)\)", re.M)
SCENE = {"CAM": "1 CAM (webcam full)", "SLIDES": "2 SLIDES (slides + cam circle)", "IDE": "3 IDE (IntelliJ + cam circle)"}

def find(mod):
    for d in sorted(MODS.iterdir()):
        if d.is_dir() and (d.name == mod or d.name.startswith(f"{int(mod):02d}_" if mod.isdigit() else mod)):
            return d
    sys.exit(f"module {mod!r} not found in {MODS}")

def parse_script(text):
    segs, cur = [], None
    for line in text.splitlines():
        m = SEG_RE.match(line)
        if m:
            n, kind, name, val, unit = m.groups()
            cur = {"n": int(n), "scene": kind, "name": name, "secs": float(val) * (60 if unit == "min" else 1), "beats": []}
            segs.append(cur)
        elif cur and line.startswith("- "):
            cur["beats"].append(line[2:].strip())
    return segs

def fmt(t):
    t = int(round(t)); return f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}" if t >= 3600 else f"{t // 60}:{t % 60:02d}"

def clip_durations(folder, mnum):
    out = {}
    for f in sorted(pathlib.Path(folder).glob(f"M{mnum}_S*")):
        m = re.match(rf"M{mnum}_S(\d+)", f.stem)
        try:
            d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                               capture_output=True, text=True, check=True).stdout.strip()
            out[int(m.group(1))] = out.get(int(m.group(1)), 0) + float(d)
        except (OSError, subprocess.CalledProcessError, ValueError):
            print(f"  ! ffprobe failed on {f.name}")
    return out

def parse_youtube(text):
    g = lambda pat: (re.search(pat, text, re.S) or [None, ""])[1].strip()
    desc = g(r"## Description\n(.*?)\n## Tags")
    return {"title": g(r"\*\*Title[^*]*:\*\* (.+?)\n"), "description": desc,
            "tags": [t.strip() for t in g(r"## Tags\n(.+?)\n").split(",") if t.strip()]}

def build(d, durations_dir=None, intro_secs=8):
    mnum = d.name[:2]
    out = ROOT / "build" / d.name
    out.mkdir(parents=True, exist_ok=True)
    segs = parse_script((d / "script.md").read_text(encoding="utf-8"))
    real = clip_durations(durations_dir, mnum) if durations_dir else {}

    tp = [f"M{mnum}  {d.name[3:].replace('-', ' ').upper()}\n"]
    for s in segs:
        tp.append(f"\n=== S{s['n']:02d} · {s['scene']} · {s['name']} ===\n")
        tp += [b + "\n" for b in s["beats"]]
    (out / "teleprompter.txt").write_text("\n".join(tp), encoding="utf-8")

    body = "".join(f"<h2>S{s['n']:02d} · {s['scene']} · {html.escape(s['name'])}</h2>"
                   + "".join(f"<p>{html.escape(b)}</p>" for b in s["beats"]) for s in segs)
    (out / "teleprompter.html").write_text(f"""<!doctype html><meta charset=utf-8><title>M{mnum} teleprompter</title>
<style>body{{background:#000;color:#fff;font:56px/1.35 Segoe UI,Arial;margin:0 12%;}}h2{{color:#22D3EE;font-size:36px;margin-top:3em}}
p{{margin:0 0 1.1em}}#hud{{position:fixed;top:8px;right:12px;font-size:18px;color:#888}}.mirror{{transform:scaleX(-1)}}</style>
<div id=hud>Space pause · ↑↓ speed · M mirror · R top</div><div id=t>{body}<p style="height:80vh"></p></div>
<script>let v=1.2,run=false;function f(){{if(run)scrollBy(0,v);requestAnimationFrame(f)}}f();
onkeydown=e=>{{if(e.code=='Space'){{run=!run;e.preventDefault()}}if(e.key=='ArrowUp')v+=.3;if(e.key=='ArrowDown')v=Math.max(.3,v-.3);
if(e.key=='m')document.getElementById('t').classList.toggle('mirror');if(e.key=='r')scrollTo(0,0)}}</script>""", encoding="utf-8")

    rows = ["| ✓ | Seg | OBS scene | Topic | Target | Take file | Beats |", "|---|---|---|---|---|---|---|"]
    for s in segs:
        rows.append(f"| ☐ | S{s['n']:02d} | {SCENE.get(s['scene'], s['scene'])} | {s['name']} | {fmt(s['secs'])} | "
                    f"`M{mnum}_S{s['n']:02d}_{s['scene']}.mkv` | {len(s['beats'])} |")
    total = sum(real.get(s["n"], s["secs"]) for s in segs)
    (out / "shot_list.md").write_text(f"# M{mnum} shot list — target {fmt(total)}\n\n" + "\n".join(rows) +
        "\n\nRules: one take per segment · 3 s silence before/after · re-read a fumbled beat after a 2 s pause (CapCut removes the gap)."
        "\nIDE segments: open `snippets/PASTE_ORDER.txt` beside IntelliJ.\n", encoding="utf-8")

    sn = out / "snippets"
    if sn.exists(): shutil.rmtree(sn)
    src = d / "snippets"
    if src.exists():
        shutil.copytree(src, sn)
        files = sorted(p.name for p in sn.glob("*.py"))
        (sn / "PASTE_ORDER.txt").write_text("\n".join(f"{i}. {f}" for i, f in enumerate(files, 1)) +
            "\n\nSee ../../../modules/" + d.name + "/livecode.md for what to type live.\n", encoding="utf-8")

    meta = parse_youtube((d / "youtube.md").read_text(encoding="utf-8"))
    t, chapters = intro_secs, ["0:00 Intro"]
    for s in segs:
        if s["name"].lower() != "hook" and not (s["n"] == 1):
            chapters.append(f"{fmt(t)} {s['name']}")
        t += real.get(s["n"], s["secs"])
    desc = re.sub(r"Chapters\n(?:\d+:\d\d.*\n?)+", "Chapters\n" + "\n".join(chapters) + "\n", meta["description"] + "\n")
    meta.update({"description": desc.strip(), "chapters": chapters, "visibility": "private",
                 "playlist": "Zero to LLM — Build Your Own Language Model", "category": "Education",
                 "made_for_kids": False, "video_file": f"M{mnum}_final.mp4", "thumbnail": f"M{mnum}_thumb.png",
                 "captions": "YouTube auto-captions, or upload CapCut's exported SRT", "chapter_source": "clips" if real else "script estimate"})
    (out / "upload.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "description.txt").write_text(desc.strip() + "\n", encoding="utf-8")
    print(f"✔ {d.name}: {len(segs)} segments, ~{fmt(total)} → {out.relative_to(ROOT)}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("module", nargs="?"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--durations", help="folder with recorded takes named M05_S03_*.mkv/mp4")
    ap.add_argument("--intro", type=float, default=8, help="seconds of intro sting before S01 (default 8)")
    a = ap.parse_args()
    if a.all:
        for d in sorted(p for p in MODS.iterdir() if p.is_dir()):
            build(d, a.durations, a.intro)
    elif a.module:
        build(find(a.module), a.durations, a.intro)
    else:
        ap.print_help()
