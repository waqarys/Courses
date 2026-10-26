#!/usr/bin/env python3
"""Silent Windows install video: new slides, live download pages, cmd, Thonny.

Durations match videos/01-install-windows-VOICE.md so a voice recording
lines up at 0:00 in CapCut.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "slides" / "slides.html"
OUT = ROOT / "videos"
FRAMES = OUT / "_frames-windows"
W, H = 1920, 1080

FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"
MONO_B = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"

NAVY = (11, 31, 51)
YELLOW = (255, 210, 63)
MINT = (46, 196, 182)
WHITE = (244, 247, 251)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def browser_frame(shot: Path, url: str, dest: Path, caption: str) -> None:
    canvas = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(canvas)
    x, y, bw, bh = 70, 36, 1780, 930
    draw.rounded_rectangle((x, y, x + bw, y + bh), 18, fill=(255, 255, 255))
    for i, color in enumerate(((255, 95, 87), (255, 189, 46), (40, 200, 64))):
        draw.ellipse((x + 22 + i * 26, y + 16, x + 40 + i * 26, y + 34), fill=color)
    draw.rounded_rectangle((x + 120, y + 12, x + bw - 24, y + 40), 10, fill=(236, 239, 244))
    draw.text((x + 140, y + 14), url, font=font(REG, 22), fill=(50, 60, 72))
    image = Image.open(shot).convert("RGB")
    avail_w, avail_h = bw - 16, bh - 64
    scale = avail_w / image.width
    image = image.resize((avail_w, int(image.height * scale)), Image.Resampling.LANCZOS)
    if image.height > avail_h:
        image = image.crop((0, 0, image.width, avail_h))
    canvas.paste(image, (x + 8, y + 52))
    draw.text((70, 990), caption, font=font(FONT, 32), fill=YELLOW)
    canvas.save(dest)


def command_prompt(dest: Path) -> None:
    canvas = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(canvas)
    draw.text((70, 28), "Command Prompt  ·  after Python is installed", font=font(FONT, 32), fill=YELLOW)
    x, y, bw, bh = 140, 100, 1640, 860
    draw.rounded_rectangle((x, y, x + bw, y + 48), 10, fill=(28, 28, 28))
    draw.rectangle((x, y + 24, x + bw, y + bh), fill=(12, 12, 12))
    draw.text((x + 18, y + 8), "Command Prompt", font=font(REG, 22), fill=(220, 220, 220))
    lines = [
        "Microsoft Windows [Version 10.0.26200]",
        "(c) Microsoft Corporation. All rights reserved.",
        "",
        "C:\\Users\\Student>python --version",
        "Python 3.15.2",
        "",
        "C:\\Users\\Student>",
    ]
    face = font(MONO, 36)
    ty = y + 80
    for line in lines:
        draw.text((x + 36, ty), line, font=face, fill=(230, 230, 230))
        ty += 52
    canvas.save(dest)


def thonny_window(dest: Path) -> None:
    canvas = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(canvas)
    draw.text((70, 24), "Thonny  ·  green Run  ·  hello_windows.py", font=font(FONT, 32), fill=YELLOW)
    x, y, bw, bh = 120, 90, 1680, 900
    draw.rounded_rectangle((x, y, x + bw, y + bh), 12, fill=(232, 234, 237))
    draw.rectangle((x, y, x + bw, y + 46), fill=(214, 218, 224))
    draw.text((x + 16, y + 8), "Thonny", font=font(FONT, 24), fill=(30, 36, 44))
    menus = "File    Edit    View    Run    Tools    Help"
    draw.text((x + 16, y + 56), menus, font=font(REG, 22), fill=(40, 46, 54))
    # run button
    draw.ellipse((x + 20, y + 100, x + 58, y + 138), fill=(46, 160, 67))
    draw.polygon([(x + 34, y + 110), (x + 34, y + 128), (x + 48, y + 119)], fill=(255, 255, 255))
    draw.text((x + 70, y + 106), "Run", font=font(FONT, 22), fill=(30, 36, 44))
    # editor
    ex, ey, ew, eh = x + 16, y + 156, bw - 32, 430
    draw.rectangle((ex, ey, ex + ew, ey + eh), fill=(255, 255, 255), outline=(180, 186, 194))
    draw.rectangle((ex, ey, ex + 64, ey + eh), fill=(245, 246, 248))
    draw.text((ex + 18, ey + 18), "1", font=font(MONO, 32), fill=(140, 148, 158))
    draw.text((ex + 84, ey + 18), 'print("Hello from Windows")', font=font(MONO, 34), fill=(20, 24, 32))
    # shell
    sx, sy, sw, sh = ex, ey + eh + 16, ew, 250
    draw.rectangle((sx, sy, sx + sw, sy + 28), fill=(226, 230, 235))
    draw.text((sx + 12, sy + 2), "Shell", font=font(FONT, 20), fill=(40, 46, 54))
    shell = [
        (">>> %Run hello_windows.py", (90, 70, 160)),
        ("Hello from Windows", (20, 24, 32)),
        (">>>", (90, 70, 160)),
    ]
    yy = sy + 48
    for text, color in shell:
        draw.text((sx + 16, yy), text, font=font(MONO, 32), fill=color)
        yy += 48
    canvas.save(dest)


def shoot_slides(dest: Path) -> dict[int, Path]:
    url = SLIDES.resolve().as_uri()
    paths = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H})
        page.goto(url)
        page.wait_for_timeout(200)
        for index in (5, 6, 7, 8, 9, 10, 11):
            page.evaluate("(n) => showSlide(n)", index)
            page.wait_for_timeout(80)
            path = dest / f"slide-{index}.png"
            page.screenshot(path=str(path))
            paths[index] = path
        browser.close()
    return paths


def shoot_sites(dest: Path) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://www.python.org/downloads/", wait_until="networkidle", timeout=60000)
        page.screenshot(path=str(dest / "python-site.png"))
        page.goto("https://thonny.org/", wait_until="networkidle", timeout=60000)
        page.screenshot(path=str(dest / "thonny-site.png"))
        browser.close()


def encode(scenes: list[tuple[Path, int]], mp4: Path) -> None:
    listing = FRAMES / "windows.ffconcat"
    lines = ["ffconcat version 1.0"]
    for frame, seconds in scenes:
        lines.append(f"file '{frame}'")
        lines.append(f"duration {seconds}")
    lines.append(f"file '{scenes[-1][0]}'")
    listing.write_text("\n".join(lines) + "\n", encoding="utf-8")
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", str(listing),
            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
            "-vf", "fps=30,format=yuv420p",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-crf", "20",
            "-c:a", "aac", "-b:a", "48k",
            "-shortest", "-movflags", "+faststart",
            str(mp4),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )


def stamp(seconds: int) -> str:
    return f"{seconds // 60}:{seconds % 60:02d}"


def main() -> None:
    FRAMES.mkdir(parents=True, exist_ok=True)
    slides = shoot_slides(FRAMES)
    shoot_sites(FRAMES)
    browser_frame(
        FRAMES / "python-site.png",
        "https://www.python.org/downloads/",
        FRAMES / "page-python.png",
        "Live page. Click the yellow button: Download Python 3.15.2",
    )
    browser_frame(
        FRAMES / "thonny-site.png",
        "https://thonny.org/",
        FRAMES / "page-thonny.png",
        "Live page. Windows installer. It already includes Python 3.14.",
    )
    command_prompt(FRAMES / "cmd.png")
    thonny_window(FRAMES / "thonny-app.png")

    # Spoken lines are timed at a clear read, about 130 words a minute, plus a breath.
    beats = [
        (slides[5], 20, "Title",
         "Hi. This is how we install Python on a Windows laptop. Chromebooks, skip this one and use the browser lesson. We install two things. Python first. Then Thonny, which is where we type."),
        (slides[6], 12, "Where to go",
         "Open your browser and go to python dot org, slash downloads. We want Python 3. Not Python 2."),
        (FRAMES / "page-python.png", 28, "Python download page",
         "This is the real page. See the big yellow button. It says Download Python 3.15.2. If your button has a newer last number, that is fine. It must say Python 3. Click it. When the file finishes, open it."),
        (slides[7], 24, "The tick",
         "On the first installer screen, look at the bottom. Tick Add python.exe to PATH. Then click Install Now. If Windows asks for a Yes, click Yes. If you see Disable path length limit, click that too."),
        (slides[8], 10, "Prove it",
         "Now we prove it worked. Click Start, type cmd, and press Enter."),
        (FRAMES / "cmd.png", 26, "python --version",
         "In the black window, type python space dash dash version, and press Enter. You want a line that starts with Python 3. This one says Python 3.15.2. Yours might be 3.15.3 or 3.14. If it says not recognized, install again, and tick Add python.exe to PATH."),
        (slides[9], 14, "Thonny next",
         "Python is in. Next is Thonny. That is the app we type in. The letters are already big. Go to thonny dot org."),
        (FRAMES / "page-thonny.png", 24, "Thonny download page",
         "This is the real Thonny page. Stay on Windows. Click Installer with Python 3.14 for Intel or AMD computers. A new ARM tablet uses the ARM link instead. Open the file. Then Next, Next, Install."),
        (slides[10], 12, "The line",
         "Open Thonny. Here is the one line we type. It is saved as hello_windows dot py."),
        (FRAMES / "thonny-app.png", 28, "Hello in Thonny",
         "Type print, open bracket, quote, Hello from Windows, quote, close bracket. Press the green Run button. Save the file as hello_windows dot py if it asks. Under the code, the shell says Hello from Windows. That is your first program."),
        (slides[11], 16, "Your turn",
         "Your turn. Run that line. Save it as hello_windows dot py. Screenshot the version, and the Hello line. Next time, we do a Mac."),
    ]

    scenes = [(path, seconds) for path, seconds, _, _ in beats]
    mp4 = OUT / "01-install-windows.mp4"
    encode(scenes, mp4)

    clock = 0
    cue = ["# 01-install-windows.mp4", "# Silent picture. Read 01-install-windows-VOICE.md from 0:00.", ""]
    voice = [
        "# Voice for the Windows install video",
        "",
        "Read this from the top while the video plays, or record it in one take and drop it on the video at 0:00 in CapCut.",
        "The pictures change at the times below. If you are still on a sentence when the picture moves, freeze that frame in CapCut until you finish the sentence.",
        "There is no narration in the file. Do not add music under your voice.",
        "",
    ]
    for _, seconds, title, line in beats:
        cue.append(f"{stamp(clock)}  {seconds:>2}s  {title}")
        voice.append(f"## {stamp(clock)}  {title}")
        voice.append("")
        voice.append(line)
        voice.append("")
        clock += seconds
    cue.append("")
    cue.append(f"Total {stamp(clock)}")
    (OUT / "01-install-windows.cue.txt").write_text("\n".join(cue) + "\n", encoding="utf-8")
    (OUT / "01-install-windows-VOICE.md").write_text("\n".join(voice) + "\n", encoding="utf-8")
    print("seconds", clock, "bytes", mp4.stat().st_size)


if __name__ == "__main__":
    main()
