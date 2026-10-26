#!/usr/bin/env python3
"""Build the kid-facing OBS deck from slides.source.md.

Every lesson gets a picture. Every code slide is drawn as a file you will
type in Thonny (or Colab on a Chromebook). Tall slides shrink to fit.
"""
from pathlib import Path
import html

ROOT = Path(__file__).parent
src = (ROOT / "slides.source.md").read_text(encoding="utf-8")

FILES = {
    "01": "hello_windows.py",
    "02": "hello_mac.py",
    "03": "hello_chromebook.py",
    "04": "idea.py",
    "05": "hello.py",
    "06": "variables.py",
    "07": "names.py",
    "08": "strings.py",
    "09": "numbers.py",
    "10": "time_stamp.py",
    "11": "booleans.py",
    "12": "maths.py",
    "13": "comments.py",
    "14": "pancake_recipe.py",
    "15": "wellbeing.py",
    "16": "lists.py",
    "17": "inventory.py",
    "18": "grids.py",
    "19": "dictionary.py",
    "20": "records.py",
    "21": "sequence.py",
    "22": "choices.py",
    "23": "nested.py",
    "24": "while_loop.py",
    "25": "for_loop.py",
    "26": "guess_the_number.py",
}

# Shown on the opening slide when that slide does not already have code.
TEASERS = {
    "03": 'print("Hello, Chromebook")',
    "04": 'print("I can learn Python")',
    "05": 'print("Hello, World!")',
    "06": 'player_name = "Jimmy"\nplayer_score = 0',
    "07": 'player_name = "Alex"\ncurrent_score = 100',
    "08": 'name = "Alex"\nprint("Hello,", name)',
    "09": 'score = 10 + 5\nprint(score)',
    "10": "from time import time\nprint(time())",
    "11": "lives = 3\nprint(lives > 0)",
    "12": "print(3 + 5 * 2)",
    "13": "# Starting score for a new player\nscore = 50",
    "14": "STANDARD_SERVINGS = 4\nflour_cups = 2.5",
    "15": "feel_positive = 4\nprint(feel_positive)",
    "16": "scores = [85, 92, 78]\nprint(scores[0])",
    "17": 'inventory = ["map", "rope", "torch"]\ninventory.append("key")',
    "18": "numbers = [10, 20, 30, 40, 50]\nprint(numbers[-1])",
    "19": 'student = {"name": "Jimmy", "age": 15}\nprint(student["name"])',
    "20": "position = (10, 20)\nx, y = position",
    "21": 'score = 0\nprint("Score starts at", score)',
    "22": 'player_health = 100\nif player_health > 0:\n    print("Player is alive")',
    "23": 'player_action = "JUMP"',
    "24": "resources = 5\nwhile resources > 0:\n    resources = resources - 1",
    "25": 'for i in range(5):\n    print("Lap", i)',
    "26": "import random\nanswer = random.randint(1, 100)",
}

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
        slide = {"title": line[3:].strip(), "points": [], "kicker": "", "code": ""}
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
    opener = les["slides"][0]
    if not opener["code"] and les["id"] in TEASERS:
        opener["code"] = TEASERS[les["id"]]
        opener["teaser"] = True


def file_hint(lesson_id, slide):
    blob = f"{slide['title']} {slide['kicker']}".lower()
    if "mistake" in blob:
        return "Wrong on purpose. Type it, run it, then fix it."
    if lesson_id == "03":
        return "Type this in the Colab cell"
    if lesson_id == "00":
        return "Teacher notes"
    return "Type this in Thonny, then press Run"


def code_block(lesson_id, slide):
    if not slide.get("code"):
        return ""
    name = FILES.get(lesson_id, "notes.py")
    lines = "".join(
        f"<span>{html.escape(line) if line else ' '}</span>"
        for line in slide["code"].split("\n")
    )
    return (
        '<div class="file">'
        '<div class="filebar"><span class="dots"><i></i><i></i><i></i></span>'
        f'<span class="fname">{html.escape(name)}</span>'
        f'<span class="hint">{html.escape(file_hint(lesson_id, slide))}</span></div>'
        f"<pre><code>{lines}</code></pre></div>"
    )


def image_uri(lesson_id):
    path = ROOT / "img" / f"{lesson_id}.jpg"
    if not path.exists():
        return ""
    return f"img/{lesson_id}.jpg"


parts = []
n = 0
total = sum(len(les["slides"]) for les in lessons)
code_slides = 0
for les in lessons:
    uri = image_uri(les["id"])
    alt = html.escape(les["title"])
    picture = f'<img class="art" alt="{alt}" src="{uri}" />' if uri else ""
    for sl in les["slides"]:
        kicker = html.escape(sl["kicker"] or f"Lesson {les['id']}")
        title = html.escape(sl["title"])
        points = "\n".join(f"        <li>{html.escape(p)}</li>" for p in sl["points"])
        block = code_block(les["id"], sl)
        if block:
            code_slides += 1
        active = " active" if n == 0 else ""
        parts.append(
            f"""<section class="slide{active}" id="s{n}" data-lesson="{html.escape(les['id'])}" data-lesson-title="{html.escape(les['title'])}">
  <div class="inner">
    <div class="top">
      <div class="copy">
        <div class="kicker">{kicker}</div>
        <h1>{title}</h1>
        <ul>
{points}
        </ul>
      </div>
      {picture}
    </div>
    {block}
  </div>
</section>"""
        )
        n += 1

menu_buttons = [
    f'<button type="button" data-jump="{html.escape(les["id"])}">{html.escape(les["id"])}   {html.escape(les["title"])}</button>'
    for les in lessons
]

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
    --coral: #ff8a5b;
    --panel: #071422;
    --line: rgba(255,255,255,.12);
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; height: 100%; background:
    radial-gradient(900px 420px at 100% -10%, rgba(46,196,182,.18), transparent 60%),
    radial-gradient(700px 380px at -10% 110%, rgba(255,138,91,.14), transparent 55%),
    var(--bg);
    color: var(--ink); font-family: "Trebuchet MS", "Segoe UI", sans-serif; overflow: hidden; }}
  .slide {{ display: none; height: calc(100% - 64px); padding: 3.2vh 4.5vw 0; }}
  .slide.active {{ display: block; }}
  .inner {{ transform-origin: top left; }}
  .top {{ display: flex; gap: 2.2vw; align-items: flex-start; }}
  .copy {{ flex: 1; min-width: 0; }}
  .art {{ width: min(44vh, 480px); height: min(44vh, 480px); object-fit: cover; flex: none;
    border-radius: 32px; border: 5px solid var(--yellow);
    box-shadow: 0 14px 0 rgba(255,210,63,.2); }}
  .slide:has(.file) .art {{ width: min(20vh, 210px); height: min(20vh, 210px); border-radius: 22px; }}
  .kicker {{ color: var(--mint); font-weight: 800; letter-spacing: .12em;
    text-transform: uppercase; font-size: clamp(15px, 1.45vw, 24px); margin-bottom: 1vh; }}
  h1 {{ color: var(--yellow); font-size: clamp(32px, 3.5vw, 64px); line-height: 1.05;
    margin: 0 0 1.6vh; font-weight: 800; max-width: 18ch; }}
  ul {{ margin: 0; padding: 0; list-style: none; }}
  li {{ font-size: clamp(20px, 1.9vw, 32px); line-height: 1.25; margin: 0 0 0.9vh;
    padding-left: 1.15em; position: relative; max-width: 36ch; }}
  li::before {{ content: ""; position: absolute; left: 0; top: .45em;
    width: .45em; height: .45em; border-radius: 50%; background: var(--coral); }}
  .file {{ margin-top: 1.4vh; background: var(--panel); border-radius: 18px;
    border: 3px solid rgba(255,210,63,.55); overflow: hidden; }}
  .filebar {{ display: flex; align-items: center; gap: 12px; background: #14324c;
    padding: 0.7vh 1vw; }}
  .dots i {{ display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-right: 6px; }}
  .dots i:nth-child(1) {{ background: #ff5f57; }}
  .dots i:nth-child(2) {{ background: #ffd23f; }}
  .dots i:nth-child(3) {{ background: #3DDC97; }}
  .fname {{ color: var(--yellow); font-family: Consolas, "Courier New", monospace;
    font-weight: 700; font-size: clamp(16px, 1.4vw, 24px); }}
  .hint {{ margin-left: auto; color: var(--mint); font-weight: 700;
    font-size: clamp(14px, 1.2vw, 20px); }}
  pre {{ margin: 0; padding: 1.1vh 1.2vw 1.3vh; color: #e8fff8;
    font-family: Consolas, "Courier New", monospace;
    font-size: clamp(16px, 1.45vw, 28px); line-height: 1.32; }}
  pre code {{ counter-reset: ln; }}
  pre code span {{ display: block; white-space: pre-wrap; }}
  pre code span::before {{ counter-increment: ln; content: counter(ln);
    display: inline-block; width: 2.2em; margin-right: 0.75em; text-align: right; color: #6d8ea8; }}
  footer {{ position: fixed; left: 4.5vw; right: 4.5vw; bottom: 0; height: 64px; display: flex;
    align-items: center; justify-content: space-between; gap: 16px; color: var(--muted);
    font-size: clamp(14px, 1.3vw, 22px); border-top: 1px solid var(--line); z-index: 4; }}
  #bar {{ position: fixed; left: 0; right: 0; top: 0; height: 8px; background: #071422; z-index: 6; }}
  #bar > div {{ height: 100%; background: linear-gradient(90deg, var(--mint), var(--yellow)); width: 0; }}
  #hitL, #hitR {{ position: fixed; top: 8px; bottom: 64px; z-index: 5; background: transparent; border: 0; padding: 0; }}
  #hitL {{ left: 0; width: 8%; cursor: w-resize; }}
  #hitR {{ right: 0; width: 12%; cursor: e-resize; }}
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
  <p class="help">Click a lesson. Right arrow, space, or the right edge goes forward. L or Esc closes this list. F is fullscreen. Code on the slide is what you type in Thonny.</p>
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
  const avail = window.innerHeight - 64 - 10;
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
  try {{ history.replaceState(null, "", "#" + s.dataset.lesson); }} catch (err) {{}}
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
document.querySelectorAll("img").forEach(img => img.addEventListener("load", fit));

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
window.showSlide = show;

const start = (location.hash || "").replace("#", "");
if (start && slides.some(s => s.dataset.lesson === start)) jumpLesson(start);
else show(i);
</script>
</body>
</html>
"""

out = ROOT / "slides.html"
out.write_text(page, encoding="utf-8")
print(
    f"lessons={len(lessons)} slides={total} code_slides={code_slides} "
    f"bytes={out.stat().st_size}"
)
