#!/usr/bin/env python3
"""Build a fullscreen OBS slide deck from slides.source.md.

Every slide is a real <section> in the file. JavaScript only shows one
at a time. Tall slides shrink to fit the screen instead of being clipped.
"""
from pathlib import Path
import html

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
    elif line.startswith("@ ") and slide is not None:
        slide["kicker"] = line[2:].strip()
    elif line.startswith("- ") and slide is not None:
        slide["points"].append(line[2:].strip())

flush_lesson()

for les in lessons:
    for sl in les["slides"]:
        sl.pop("_in_code", None)
        sl.setdefault("code", "")

total = sum(len(les["slides"]) for les in lessons)
parts = []
n = 0
for les in lessons:
    for sl in les["slides"]:
        kicker = html.escape(sl["kicker"] or f"Lesson {les['id']}")
        title = html.escape(sl["title"])
        points = "\n".join(f"      <li>{html.escape(p)}</li>" for p in sl["points"])
        code_html = f"\n    <pre>{html.escape(sl['code'])}</pre>" if sl["code"] else ""
        active = " active" if n == 0 else ""
        parts.append(
            f"""<section class="slide{active}" id="s{n}" data-lesson="{html.escape(les['id'])}" data-lesson-title="{html.escape(les['title'])}">
  <div class="inner">
    <div class="kicker">{kicker}</div>
    <h1>{title}</h1>
    <ul>
{points}
    </ul>{code_html}
  </div>
</section>"""
        )
        n += 1

menu_buttons = []
for les in lessons:
    menu_buttons.append(
        f'<button type="button" data-jump="{html.escape(les["id"])}">{html.escape(les["id"])}   {html.escape(les["title"])}</button>'
    )

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Python for Kids — {total} slides</title>
<style>
  :root {{
    --bg: #0b1f33;
    --ink: #f4f7fb;
    --muted: #c5d2e0;
    --yellow: #ffd23f;
    --mint: #2ec4b6;
    --panel: #071422;
    --line: rgba(255,255,255,.12);
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; height: 100%; background: var(--bg); color: var(--ink);
    font-family: "Trebuchet MS", "Segoe UI", sans-serif; overflow: hidden; }}
  .slide {{ display: none; height: calc(100% - 64px); padding: 4.2vh 6vw 0; }}
  .slide.active {{ display: block; }}
  .inner {{ transform-origin: top left; }}
  .kicker {{ color: var(--mint); font-weight: 700; letter-spacing: .14em;
    text-transform: uppercase; font-size: clamp(16px, 1.6vw, 28px); margin-bottom: 1.2vh; }}
  h1 {{ color: var(--yellow); font-size: clamp(34px, 3.8vw, 68px); line-height: 1.08;
    margin: 0 0 2.4vh; font-weight: 800; max-width: 22ch; }}
  ul {{ margin: 0; padding: 0; list-style: none; }}
  li {{ font-size: clamp(22px, 2.15vw, 36px); line-height: 1.28; margin: 0 0 1.15vh;
    padding-left: 1.15em; position: relative; max-width: 42ch; }}
  li::before {{ content: ""; position: absolute; left: 0; top: .48em;
    width: .42em; height: .42em; border-radius: 50%; background: var(--mint); }}
  .slide:has(pre) h1 {{ font-size: clamp(28px, 2.8vw, 52px); margin-bottom: 1.4vh; max-width: 28ch; }}
  .slide:has(pre) li {{ font-size: clamp(18px, 1.55vw, 28px); max-width: 52ch; }}
  pre {{ margin: 1.2vh 0 0; background: var(--panel); color: #e8fff8;
    border-radius: 18px; padding: 1.5vh 1.5vw; font-family: Consolas, "Courier New", monospace;
    font-size: clamp(16px, 1.45vw, 28px); line-height: 1.32; white-space: pre-wrap;
    border: 3px solid rgba(46,196,182,.45); }}
  footer {{ position: fixed; left: 6vw; right: 6vw; bottom: 0; height: 64px; display: flex;
    align-items: center; justify-content: space-between; gap: 16px; color: var(--muted);
    font-size: clamp(14px, 1.3vw, 22px); border-top: 1px solid var(--line); background: var(--bg); z-index: 4; }}
  #bar {{ position: fixed; left: 0; right: 0; top: 0; height: 8px; background: #071422; z-index: 6; }}
  #bar > div {{ height: 100%; background: var(--mint); width: 0; }}
  #hitL, #hitR {{ position: fixed; top: 8px; bottom: 64px; z-index: 5; background: transparent; border: 0; padding: 0; }}
  #hitL {{ left: 0; width: 10%; cursor: w-resize; }}
  #hitR {{ right: 0; width: 16%; cursor: e-resize; }}
  #menu {{ position: fixed; inset: 0; background: rgba(7,16,28,.96); display: none;
    padding: 6vh 8vw; overflow: auto; z-index: 8; }}
  #menu.open {{ display: block; }}
  #menu h2 {{ color: var(--yellow); margin-top: 0; font-size: 42px; }}
  #menu button {{ display: block; width: min(820px, 100%); text-align: left;
    background: transparent; color: var(--ink); border: 0; border-bottom: 1px solid var(--line);
    font: inherit; font-size: 28px; padding: 14px 0; cursor: pointer; }}
  #menu button:hover, #menu button:focus {{ color: var(--yellow); }}
  .help {{ color: var(--muted); font-size: 20px; }}
</style>
<noscript>
<style>
  html, body {{ overflow: auto; height: auto; }}
  .slide {{ display: block !important; height: auto; min-height: 100vh; page-break-after: always; }}
  #hitL, #hitR, #menu, #bar {{ display: none !important; }}
</style>
</noscript>
</head>
<body>
<div id="bar"><div id="fill"></div></div>
{chr(10).join(parts)}
<button id="hitL" type="button" aria-label="Previous slide"></button>
<button id="hitR" type="button" aria-label="Next slide"></button>
<footer>
  <span id="lessonLabel"></span>
  <span id="countLabel"></span>
</footer>
<div id="menu">
  <h2>All {len(lessons)} lessons, {total} slides</h2>
  <p class="help">Click a lesson. Right arrow, space, or the right edge goes forward. L or Esc closes this list. F is fullscreen.</p>
  {''.join(menu_buttons)}
</div>
<script>
const slides = [...document.querySelectorAll(".slide")];
let i = Math.max(0, slides.findIndex(s => s.classList.contains("active")));
const menu = document.getElementById("menu");

function fit() {{
  const inner = document.querySelector(".slide.active .inner");
  if (!inner) return;
  inner.style.transform = "none";
  const avail = window.innerHeight - 64 - 8;
  const needed = inner.getBoundingClientRect().height;
  const scale = Math.min(1, avail / Math.max(needed, 1));
  inner.style.transformOrigin = "top left";
  inner.style.transform = scale < 0.995 ? "scale(" + scale + ")" : "none";
}}

function show(n) {{
  i = Math.min(slides.length - 1, Math.max(0, n));
  slides.forEach((s, idx) => s.classList.toggle("active", idx === i));
  const s = slides[i];
  document.getElementById("lessonLabel").textContent =
    s.dataset.lesson + "  " + s.dataset.lessonTitle;
  document.getElementById("countLabel").textContent =
    (i + 1) + " / " + slides.length + "     →";
  document.getElementById("fill").style.width = ((i + 1) / slides.length * 100) + "%";
  try {{ history.replaceState(null, "", "#" + s.dataset.lesson); }} catch (e) {{}}
  fit();
}}

function jumpLesson(id) {{
  const n = slides.findIndex(s => s.dataset.lesson === id);
  if (n >= 0) show(n);
  menu.classList.remove("open");
}}

document.getElementById("hitR").onclick = () => show(i + 1);
document.getElementById("hitL").onclick = () => show(i - 1);
document.querySelectorAll("#menu button[data-jump]").forEach(b => {{
  b.onclick = () => jumpLesson(b.dataset.jump);
}});

document.addEventListener("keydown", (e) => {{
  if (e.key === "ArrowRight" || e.key === "PageDown" || e.key === " ") {{ e.preventDefault(); show(i + 1); }}
  else if (e.key === "ArrowLeft" || e.key === "PageUp" || e.key === "Backspace") {{ e.preventDefault(); show(i - 1); }}
  else if (e.key === "Home") show(0);
  else if (e.key === "End") show(slides.length - 1);
  else if (e.key === "l" || e.key === "L") menu.classList.toggle("open");
  else if (e.key === "Escape") menu.classList.remove("open");
  else if (e.key === "f" || e.key === "F") {{
    if (!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  }}
}});
window.addEventListener("resize", fit);

const start = (location.hash || "").replace("#", "");
if (start && slides.some(s => s.dataset.lesson === start)) jumpLesson(start);
else show(i);
</script>
</body>
</html>
"""

(ROOT / "slides.html").write_text(page, encoding="utf-8")
print(f"lessons={len(lessons)} slides={total} bytes={(ROOT / 'slides.html').stat().st_size}")
