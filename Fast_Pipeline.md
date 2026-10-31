# Python for Kids – Fast Pipeline (Imagine + Kokoro + OBS live coding)

Branch `python-kids-fast-pipeline`. Same idea as the Class 2 Science Olympiad pipeline: **the computer builds the video**.
You only (1) make pictures in Grok Imagine and (2) record the live coding in OBS. Everything that *explains* a
concept is AI: Kokoro voice + Imagine pictures/clips + burned-in captions. Your own intro/outro voice is optional.

```
INTRO (≈10 s)  your voice/intro.m4a  OR  AI voice reads Intro_Outro.md   – over THIS lesson's thumbnail
TITLE card     "Hello, World • Python for Kids • Lesson 1"
BODY           in the order of Segments.txt, e.g.
                 explain 1-3   AI narration + scene_01..03 (still = slow zoom, scene_NN.mp4 = Imagine clip)
                 code 1 | …    "LET'S CODE!" card → live/live_01.mp4 (your OBS recording, Thonny/IntelliJ + webcam circle)
                 explain 4     next concept …
                 code 2 | …    …
                 yourturn      challenge card read by the AI voice (Challenge.md)
                 quiz          optional, if you add Quiz.md (same format as the Science series)
OUTRO (≈8 s)   your voice/outro.m4a  OR  AI voice   – over the NEXT lesson's thumbnail + "UP NEXT" ribbon
```
All parts are joined with 0.3 s crossfades, every part is loudness-normalised to −16 LUFS, any live-clip
resolution/fps/aspect is scaled + padded to 1920×1080 30 fps.

## Outputs (`lessons/NN_Topic/render/`, git-ignored)
| File | Use |
|---|---|
| `NN_Topic_full.mp4` | The video to upload (1080p30, explainer captions burned in) |
| `NN_Topic_full.srt` | Upload as English subtitles (AI narration + intro/outro; your live talk: YouTube auto-captions, or `--whisper`) |
| `NN_Topic_chapters.txt` | Real timestamps – paste into the description |
| `NN_Topic_thumb.jpg` | 1280×720 thumbnail (from `images/thumb_art.jpg` + title text) |
| `NN_Topic_short.mp4` | 9:16 Short from the first explainer (≤45 s) |
| `NN_Topic_parts.json` | Where each part starts – handy for checking the order |

## One-time setup (Windows laptop, ≈30 min)
1. Python 3.11+, ffmpeg (`winget install Gyan.FFmpeg`), Git – you already have these from the Science series.
2. `git clone -b python-kids-fast-pipeline https://github.com/waqarys/Courses.git C:\working\Content\PythonKids`
3. `cd C:\working\Content\PythonKids` → `python -m venv .venv` → `.venv\Scripts\activate` → `pip install pillow numpy soundfile kokoro-onnx`
4. Copy `kokoro-v1.0.onnx` + `voices-v1.0.bin` into `tools\kokoro\` (same files as the Science repo – just copy that folder; git-ignored).
5. Double-click `tools\fonts\Fredoka.ttf` → Install.
6. Import the OBS scenes – see [OBS_Setup.md](OBS_Setup.md).
7. Test without any pictures or recordings: `python tools\render_video.py 01 --placeholder --quick --gpu`

## The weekend routine (per lesson ≈ 35–50 min of your time)
1. **Pictures (15–20 min)** – open `lessons\NN_*\Visual_Prompts.md`. In Grok Imagine attach `Character\Minty_reference.png`,
   paste each prompt **in order**, download the first good one. Scenes marked **🎬 VIDEO**: also make the 4–6 s clip
   (optional). Thumbnail prompt last. Then:
   `python tools\import_images.py "%USERPROFILE%\Downloads" 01 --thumb`
2. **Preview (2 min)** – `python tools\render_video.py 01 --quick --gpu` and watch the explainer. Missing live clips show a
   "Record live_01 here" card, so you can already see the flow.
3. **Live coding (15–25 min)** – open `Live_Coding.md`. OBS scene **Teach** (Thonny) or **Teach IntelliJ**. One recording per
   `live_NN` step: type the code, run it, show the deliberate mistake where marked. Stop recording after each step.
   Rename/move each file to `lessons\NN_*\live\live_01.mp4`, `live_02.mp4` … (OBS: Settings → Output → Recording Path =
   that `live` folder and rename afterwards; MKV/MOV fine). Messy start/end? Add `live\trim.json`:
   `{"live_01": {"start": 3.5, "end": 92}}`
4. **Intro/outro voice (optional, 2 min)** – read `Intro_Outro.md` into CapCut (or your phone), export audio as
   `voice\intro.m4a` and `voice\outro.m4a`. Skip it and the AI voice reads the same text.
5. **Render (one command)** – `python tools\render_video.py 01 --gpu`  (or `--all --gpu` for the weekend batch).
6. **Check at 2×** – open `render\01_Hello_World_full.mp4`. Fix → re-render only that lesson (AI voice is cached).
7. **Upload** – hand `render\` + `YouTube.md` to Grok Bot ("upload Python lesson 01 to Happy Learners ICSE, schedule …").

CapCut is only for recording the intro/outro voice (and an optional quick fix). No timeline editing.

## Commands
```
python tools\render_video.py 01 --gpu                        # full lesson
python tools\render_video.py 01 --quick --placeholder        # 720p preview, no pictures/recordings needed
python tools\render_video.py --all --gpu                     # every lesson that has images
python tools\render_video.py 01 --ai-intro-outro             # ignore voice\ recordings
python tools\render_video.py 01 --intro D:\rec\in.m4a --outro D:\rec\out.m4a
python tools\render_video.py 01 --no-intro-outro             # body only
python tools\render_video.py 01 --whisper                    # caption your live talk too (pip install faster-whisper)
python tools\render_video.py 01 --voice am_puck --speed 0.95 # other Kokoro voice (keep one for the whole series)
python tools\make_lessons.py                                 # (re)create missing lesson files from slides/notes/code
```
Measured on the Grok Bot box (8 CPU cores, no GPU): lesson 01 placeholder preview (`--quick`, 1.9 min video) in 45 s.

## Choices made (change if you like)
- **Channel:** the repo didn't name one. Docs and YouTube.md assume **Happy Learners ICSE** (it covers Programming for
  ICSE learners, made for kids, sign-off "Happy Learning!"). For @BuildWithWaqar change the intro/outro lines and YouTube.md.
- **Mascot:** the mint-green python from the studio pack, called **Minty** here (`Character/Minty_reference.png` =
  `studio/obs/snake.png`). Rename freely – only Script.md / Visual_Prompts.md mention the name.
- **8-second cartoon classroom open:** no longer a separate segment (it would add 8 s to every video). It is the
  optional look of the thumbnail art (Visual_Prompts thumbnail prompt), and the intro voice plays over the thumbnail. The old rule "AI avatar only speaks the open and 'your turn', never teaches code" becomes: **AI voice explains
  concepts and reads the Your-turn card; all code on screen is your real live recording.**
- Lessons 02–23 Script/Visual/Live files are **drafts generated from the slides** – read once and polish.
  Lesson 01 is hand-written. `make_lessons.py` never overwrites existing files unless you pass `--force`.

See also: [OBS_Setup.md](OBS_Setup.md) · [Folder_Layout.md](Folder_Layout.md) · [Troubleshooting.md](Troubleshooting.md) ·
[All_Intros_Outros.md](All_Intros_Outros.md) · [Lessons.md](Lessons.md)
