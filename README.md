# Python for Kids

> **New: Fast Pipeline (branch `python-kids-fast-pipeline`).** AI explainer (Imagine pictures + Kokoro voice) →
> your live coding in OBS (Thonny / IntelliJ + webcam circle) → Your-turn card, wrapped in intro/outro, rendered with
> one command: `python tools/render_video.py 01 --gpu`. Start with [Fast_Pipeline.md](Fast_Pipeline.md),
> lessons in [Lessons.md](Lessons.md). The silent-slides + OBS voiceover workflow below is the **older workflow**
> (superseded for new videos, kept for reference and the install videos).


Branch: `python-introduction-to-kids`

Silent pictures, speaker notes, and example programs for a first Python course. You add the voice in OBS. Nothing in the videos is narrated.

Children start at Hello, World. Install videos stay in the repo, but they are last, and only if Python will not open. Reorder that way in YouTube Studio. The files keep their old names.

## What is here

| Path | What it is |
|---|---|
| `slides/slides.html` | Kid deck. Teacher notes, then lessons 01–23, then setup A, B, and C. Each lesson has a picture. Code sits in a file card you type in Thonny. |
| `notes/RECORDING-NOTES.md` | What to say, what to type, and the deliberate mistake. |
| `code/` | One program per lesson. Safe to run, except the game, which waits for a guess. |
| `videos/01-install-windows.mp4` | Silent Windows setup, 3 min 34 sec. Last in the playlist, not first. |
| `videos/02-install-mac.mp4` | Silent Mac setup. Last in the playlist. |
| `videos/03-install-chromebook.mp4` | Silent Chromebook pictures. Colab in the browser. No Linux. Last in the playlist. |
| `videos/01-install-windows-VOICE.md` | Read this aloud for the Windows video. The pictures change on these times. |

## Yes, you only add the voice

Each install video is a 1080p picture track plus a silent audio track. OBS plays the picture. Your microphone is the voiceover. They do not fight each other, because the video has nothing to say.

The Mac and Chromebook videos hold each slide for 28 seconds. The Windows video does not. It is cut to `videos/01-install-windows-VOICE.md`. Record that script, then put the voice on the silent video at 0:00 in CapCut. If a sentence runs past a cut, freeze that frame until you finish it.

### OBS, once

1. Download this branch as ZIP, or `git clone -b python-introduction-to-kids https://github.com/waqarys/Courses.git`
2. Scene `Picture`: **+** → **Media Source** → pick `videos/01-install-windows.mp4`.
   - Tick **Restart playback when source becomes active**.
   - Leave **Loop** off.
3. In the mixer, make sure the media source is not muted by mistake, and that your **Mic** is on. The media track is silent, so viewers will only hear you.
4. Settings → Hotkeys. Find that media source. Set **Pause** to `F8` and **Play** to `F9`.
5. Record 1920×1080, 30 fps. Headphones on.

### One install video

1. Open the matching cue file and the same lesson in `notes/RECORDING-NOTES.md`.
2. Start recording. Talk the title. The picture changes every 28 seconds.
3. Press **F8** if you are still talking when you feel the picture is about to move. Press **F9** when you want the next step.
4. Stop after the **Your turn** slide.
5. You do not need a second take for the slides. Trim only if you paused too long.

Lessons 01 through 23 have no video yet. Open the `slides` folder and double-click `slides.html` in Chrome. Keep the `img` folder beside it or the pictures disappear. Press the right arrow, or click the right edge. Press **L** for the lesson list, **F** for fullscreen. Lesson 01 is Hello, World. Setup A, B, and C are at the bottom of that list. The code card is the file you type in Thonny. Window-capture that Chrome window. Switch to Thonny when the card says to type it. If a slide is tall, the page shrinks it so the last line stays on screen.

Chromebook students never install Python. Setup C, at the end, sends them to Google Colab. A child who already has Thonny or Colab skips A, B, and C.

## Run an example

```bash
python3 code/05_hello_world.py
python3 code/14_pancake_recipe.py
```

`code/26_guess_the_number.py` waits for you to type a number.

Rebuild the install videos after you edit `slides/slides.source.md`:

```bash
python3 tools/render_install_videos.py
```
