#!/usr/bin/env python3
"""Render silent 1080p install videos from the first three lessons.

Each slide holds for HOLD_SECONDS so a teacher can talk, and pause in OBS
if they need longer. There is a silent audio track so OBS imports cleanly.
No narration is burned in.
"""
from __future__ import annotations

import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "slides" / "slides.source.md"
OUT = ROOT / "videos"
FRAMES = ROOT / "videos" / "_frames"

W, H = 1920, 1080
HOLD = 28  # seconds per slide
BG = (11, 31, 51)
YELLOW = (255, 210, 63)
WHITE = (244, 247, 251)
MUTED = (197, 210, 224)
MINT = (46, 196, 182)
PANEL = (7, 20, 34)

FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words = text.split()
    if not words:
        return []
    lines: list[str] = []
    cur = words[0]
    for word in words[1:]:
        trial = f"{cur} {word}"
        if draw.textlength(trial, font=face) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def parse_lessons(text: str) -> list[dict]:
    lessons: list[dict] = []
    lesson = None
    slide = None
    in_code = False
    code: list[str] = []

    def flush_slide() -> None:
        nonlocal slide, in_code, code
        if lesson is None or slide is None:
            return
        if in_code:
            slide["code"] = "\n".join(code).strip("\n")
        lesson["slides"].append(slide)
        slide = None
        in_code = False
        code = []

    def flush_lesson() -> None:
        nonlocal lesson
        flush_slide()
        if lesson and lesson["slides"]:
            lessons.append(lesson)
        lesson = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if in_code and line.strip() != "```":
            code.append(line)
            continue
        if line.strip() == "```" and slide is not None:
            if not in_code:
                in_code = True
                code = []
            else:
                slide["code"] = "\n".join(code).strip("\n")
                in_code = False
                code = []
            continue
        if line.startswith("# "):
            flush_lesson()
            num, _, title = line[2:].partition("|")
            lesson = {"id": num.strip(), "title": title.strip(), "slides": []}
            slide = None
        elif line.startswith("## "):
            flush_slide()
            slide = {"title": line[3:].strip(), "kicker": "", "points": [], "code": ""}
        elif line.startswith("@ ") and slide is not None:
            slide["kicker"] = line[2:].strip()
        elif line.startswith("- ") and slide is not None:
            slide["points"].append(line[2:].strip())
    flush_lesson()
    return lessons


def render_slide(slide: dict, lesson: dict, index: int, total: int, path: Path) -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, 10), fill=MINT)

    kicker_face = font(FONT, 28)
    title_face = font(FONT, 68)
    body_face = font(FONT_REG, 40)
    code_face = font(MONO, 34)
    foot_face = font(FONT_REG, 26)

    y = 70
    kicker = slide["kicker"] or f"Lesson {lesson['id']}"
    draw.text((90, y), kicker.upper(), font=kicker_face, fill=MINT)
    y += 52

    max_w = W - 180
    title_lines = wrap(draw, slide["title"], title_face, max_w)[:3]
    for line in title_lines:
        draw.text((90, y), line, font=title_face, fill=YELLOW)
        y += 80
    y += 16

    code = slide.get("code") or ""
    points = slide["points"]
    if code and points and len(code.splitlines()) > 4:
        body_face = font(FONT_REG, 32)
        code_face = font(MONO, 30)

    for point in points:
        bullet_lines = wrap(draw, point, body_face, max_w - 50)
        for i, line in enumerate(bullet_lines):
            if i == 0:
                draw.ellipse((96, y + 16, 116, y + 36), fill=MINT)
            draw.text((140, y), line, font=body_face, fill=WHITE)
            y += 52
        y += 8

    if code:
        lines = code.splitlines() or [""]
        line_h = 44
        pad = 28
        block_h = pad * 2 + line_h * len(lines)
        if y + block_h > H - 90:
            code_face = font(MONO, 28)
            line_h = 38
            block_h = pad * 2 + line_h * len(lines)
        top = min(y + 10, H - 80 - block_h)
        draw.rounded_rectangle((90, top, W - 90, top + block_h), radius=18, fill=PANEL, outline=MINT, width=3)
        cy = top + pad
        for line in lines:
            draw.text((118, cy), line if line else " ", font=code_face, fill=(232, 255, 248))
            cy += line_h

    footer = f"Python for Kids   ·   {lesson['id']}  {lesson['title']}   ·   {index} / {total}"
    draw.line((90, H - 62, W - 90, H - 62), fill=(255, 255, 255), width=1)
    draw.text((90, H - 50), footer, font=foot_face, fill=MUTED)
    img.save(path, "PNG")


def encode(frames: list[Path], mp4: Path, cue: Path, slides: list[dict]) -> None:
    listing = FRAMES / f"{mp4.stem}.ffconcat"
    lines = ["ffconcat version 1.0"]
    for frame in frames:
        lines.append(f"file '{frame}'")
        lines.append(f"duration {HOLD}")
    lines.append(f"file '{frames[-1]}'")
    listing.write_text("\n".join(lines) + "\n", encoding="utf-8")

    cue_lines = [f"# {mp4.name}", f"# Each picture holds for {HOLD} seconds. Pause in OBS if you need longer.", ""]
    for i, slide in enumerate(slides):
        t = i * HOLD
        cue_lines.append(f"{t // 60:02d}:{t % 60:02d}  {slide['title']}")
    cue.write_text("\n".join(cue_lines) + "\n", encoding="utf-8")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", str(listing),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-vf", "fps=30,format=yuv420p",
        "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-crf", "26",
        "-c:a", "aac", "-b:a", "48k",
        "-shortest", "-movflags", "+faststart",
        str(mp4),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main() -> None:
    wanted = {"01", "02", "03"}
    lessons = [ls for ls in parse_lessons(SLIDES.read_text(encoding="utf-8")) if ls["id"] in wanted]
    if len(lessons) != 3:
        raise SystemExit(f"expected lessons 01-03, got {[ls['id'] for ls in lessons]}")
    OUT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    names = {
        "01": "01-install-windows.mp4",
        "02": "02-install-mac.mp4",
        "03": "03-install-chromebook.mp4",
    }
    for lesson in lessons:
        frames = []
        total = len(lesson["slides"])
        for i, slide in enumerate(lesson["slides"], start=1):
            frame = FRAMES / f"{lesson['id']}-{i:02d}.png"
            render_slide(slide, lesson, i, total, frame)
            frames.append(frame)
        mp4 = OUT / names[lesson["id"]]
        encode(frames, mp4, OUT / f"{mp4.stem}.cue.txt", lesson["slides"])
        print(mp4.name, mp4.stat().st_size)


if __name__ == "__main__":
    main()
