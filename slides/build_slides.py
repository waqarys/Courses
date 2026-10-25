#!/usr/bin/env python3
"""Build a fullscreen OBS slide deck from a simple slide source."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).parent
src = (ROOT / "slides.source.md").read_text(encoding="utf-8")

lessons = []
lesson = None
slide = None
code = None

def flush_slide():
    global slide, code
    if lesson is None or slide is None:
        return
    if code is not None:
        slide["code"] = "\n".join(code).strip("\n")
    slide.pop("_in_code", None)
    if slide["title"] or slide["points"] or slide.get("code"):
        lesson["slides"].append(slide)
    slide = None
    code = None

def flush_lesson():
    global lesson
    flush_slide()
    if lesson and lesson["slides"]:
        lessons.append(lesson)
    lesson = None

for raw in src.splitlines():
    line = raw.rstrip()
    in_code = slide is not None and slide.get("_in_code")
    if in_code and line.strip() != "```":
        code.append(line)
        continue
    if line.strip() == "```" and slide is not None:
        if not slide.get("_in_code"):
            slide["_in_code"] = True
            code = []
        else:
            slide["code"] = "\n".join(code).strip("\n")
            slide["_in_code"] = False
            code = None
        continue
    if line.startswith("# "):
        flush_lesson()
        num, _, title = line[2:].partition("|")
        lesson = {"id": num.strip(), "title": title.strip(), "slides": []}
        slide = None
        code = None
    elif line.startswith("## "):
        flush_slide()
        slide = {"title": line[3:].strip(), "points": [], "kicker": ""}
        code = None
    elif line.startswith("@ "):
        if slide is not None:
            slide["kicker"] = line[2:].strip()
    elif line.startswith("- ") and slide is not None:
        slide["points"].append(line[2:].strip())

flush_lesson()

# clean internal flags
for les in lessons:
    for sl in les["slides"]:
        sl.pop("_in_code", None)
        sl.setdefault("code", "")

payload = json.dumps(lessons, ensure_ascii=False)

page = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Python for Kids — OBS slides</title>
<style>
  :root {
    --bg: #0b1f33;
    --ink: #f4f7fb;
    --muted: #c5d2e0;
    --yellow: #ffd23f;
    --mint: #2ec4b6;
    --panel: #071422;
    --line: rgba(255,255,255,.12);
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; background: var(--bg); color: var(--ink);
    font-family: "Trebuchet MS", "Segoe UI", sans-serif; overflow: hidden; }
  #stage { height: 100%; display: flex; flex-direction: column; padding: 5.5vh 6vw 8vh; }
  .kicker { color: var(--mint); font-weight: 700; letter-spacing: .14em;
    text-transform: uppercase; font-size: clamp(16px, 1.6vw, 28px); margin-bottom: 1.2vh; }
  h1 { color: var(--yellow); font-size: clamp(40px, 4.6vw, 84px); line-height: 1.05;
    margin: 0 0 3vh; font-weight: 800; max-width: 18ch; }
  ul { margin: 0; padding: 0; list-style: none; }
  li { font-size: clamp(26px, 2.5vw, 44px); line-height: 1.28; margin: 0 0 1.4vh;
    padding-left: 1.1em; position: relative; max-width: 22ch; }
  li::before { content: ""; position: absolute; left: 0; top: .55em;
    width: .42em; height: .42em; border-radius: 50%; background: var(--mint); }
  #stage:has(pre:not([hidden])) h1 { font-size: clamp(32px, 3.2vw, 58px); margin-bottom: 1.6vh; }
  #stage:has(pre:not([hidden])) li { font-size: clamp(20px, 1.7vw, 30px); max-width: 36ch; }
  pre { margin: 1vh 0 0; background: var(--panel); color: #e8fff8;
    border-radius: 18px; padding: 1.6vh 1.6vw; font-family: Consolas, "Courier New", monospace;
    font-size: clamp(18px, 1.65vw, 30px); line-height: 1.32; white-space: pre-wrap;
    border: 3px solid rgba(46,196,182,.45); max-width: 100%; }
  footer { position: fixed; left: 6vw; right: 6vw; bottom: 2.2vh; display: flex;
    justify-content: space-between; gap: 16px; color: var(--muted);
    font-size: clamp(14px, 1.3vw, 22px); border-top: 1px solid var(--line); padding-top: 1.2vh; }
  #bar { position: fixed; left: 0; right: 0; top: 0; height: 8px; background: #071422; }
  #bar > div { height: 100%; background: var(--mint); width: 0; }
  #menu { position: fixed; inset: 0; background: rgba(7,16,28,.94); display: none;
    padding: 6vh 8vw; overflow: auto; }
  #menu.open { display: block; }
  #menu h2 { color: var(--yellow); margin-top: 0; font-size: 42px; }
  #menu button { display: block; width: min(820px, 100%); text-align: left;
    background: transparent; color: var(--ink); border: 0; border-bottom: 1px solid var(--line);
    font: inherit; font-size: 28px; padding: 14px 0; cursor: pointer; }
  #menu button:hover, #menu button:focus { color: var(--yellow); }
  .help { color: var(--muted); font-size: 20px; }
</style>
</head>
<body>
<div id="bar"><div id="fill"></div></div>
<div id="stage">
  <div class="kicker" id="kicker"></div>
  <h1 id="title"></h1>
  <ul id="points"></ul>
  <pre id="code" hidden></pre>
</div>
<footer>
  <span id="lessonLabel"></span>
  <span id="countLabel"></span>
</footer>
<div id="menu">
  <h2>Jump to a lesson</h2>
  <p class="help">Click one. Press L or Esc to close. Right arrow advances a slide. F is fullscreen.</p>
  <div id="menuList"></div>
</div>
<script>
const LESSONS = __PAYLOAD__;
let li = 0, si = 0;
const flat = [];
LESSONS.forEach((lesson, i) => lesson.slides.forEach((_, j) => flat.push([i, j])));

function render() {
  const lesson = LESSONS[li];
  const slide = lesson.slides[si];
  document.getElementById("kicker").textContent = slide.kicker || ("Lesson " + lesson.id);
  document.getElementById("title").textContent = slide.title;
  const ul = document.getElementById("points");
  ul.innerHTML = "";
  (slide.points || []).forEach(p => {
    const el = document.createElement("li");
    el.textContent = p;
    ul.appendChild(el);
  });
  const pre = document.getElementById("code");
  if (slide.code) { pre.hidden = false; pre.textContent = slide.code; }
  else { pre.hidden = true; pre.textContent = ""; }
  document.getElementById("lessonLabel").textContent = lesson.id + "  " + lesson.title;
  const idx = flat.findIndex(([a,b]) => a === li && b === si);
  document.getElementById("countLabel").textContent = (idx + 1) + " / " + flat.length;
  document.getElementById("fill").style.width = ((idx + 1) / flat.length * 100) + "%";
  history.replaceState(null, "", "#" + lesson.id);
}

function goDelta(d) {
  const idx = flat.findIndex(([a,b]) => a === li && b === si);
  const n = Math.min(flat.length - 1, Math.max(0, idx + d));
  [li, si] = flat[n];
  render();
}

function jumpLesson(id) {
  const i = LESSONS.findIndex(l => l.id === id);
  if (i < 0) return;
  li = i; si = 0; render();
  document.getElementById("menu").classList.remove("open");
}

const menu = document.getElementById("menu");
const menuList = document.getElementById("menuList");
LESSONS.forEach(lesson => {
  const b = document.createElement("button");
  b.textContent = lesson.id + "   " + lesson.title;
  b.onclick = () => jumpLesson(lesson.id);
  menuList.appendChild(b);
});

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight" || e.key === "PageDown" || e.key === " ") { e.preventDefault(); goDelta(1); }
  else if (e.key === "ArrowLeft" || e.key === "PageUp" || e.key === "Backspace") { e.preventDefault(); goDelta(-1); }
  else if (e.key === "Home") { li = 0; si = 0; render(); }
  else if (e.key === "l" || e.key === "L") menu.classList.toggle("open");
  else if (e.key === "Escape") menu.classList.remove("open");
  else if (e.key === "f" || e.key === "F") {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  }
});

const start = (location.hash || "").replace("#", "");
if (LESSONS.some(l => l.id === start)) jumpLesson(start);
else render();
</script>
</body>
</html>
"""

page = page.replace("__PAYLOAD__", payload)
(ROOT / "slides.html").write_text(page, encoding="utf-8")
print(f"lessons={len(lessons)} slides={sum(len(l['slides']) for l in lessons)} bytes={ (ROOT/'slides.html').stat().st_size }")
