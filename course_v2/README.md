# Introduction to Python (course v2) — Fun Skill Builders

A complete beginner course for ages 7 to 20, hosted by **Ziggy the Python**. Each lesson explains the concept first,
then **types the code on screen line by line while Ziggy explains each line**, asks "what do you think will happen?"
before running, runs it for real, shows common mistakes, recaps, and ends with an exercise (pause + answer).

* **Outline (38 lessons, 5 modules) with measured lengths:** [COURSE_OUTLINE.md](COURSE_OUTLINE.md)
* **Scripts:** `lessons/<lesson>/lesson.md` — all 38 lessons fully written
* **Programs for learners:** `code/` (regenerate with `python course_v2/export_code.py`)
* **Settings:** [course.yaml](course.yaml) (host, voice, speed, dark editor theme, soft background music, pronunciations)
* **Renderer:** `eduvid pycourse` in [waqarys/eduvid-pipeline](https://github.com/waqarys/eduvid-pipeline/tree/python-course),
  branch `python-course`; lesson format in its `docs/PYCOURSE_FORMAT.md`

The older material on this branch (`lessons/`, `code/`, `slides/`, `tools/render_video.py`, the OBS workflow) is kept
unchanged. Course v2 does not need OBS or Grok Imagine pictures: everything is generated on the laptop.

## Render on the laptop (Windows, PowerShell)

Everything runs inside `C:\working\projects\ContentCreator`, where `eduvid-pipeline` is already cloned with a working
`.venv` (Python 3.11.9, torch cu124 with CUDA, NVENC). There is no `py` launcher, so the commands use `python`.
The Kokoro voice model comes from the minimal model download in `C:\Users\waqar\.eduvid\models`.

### Once

```powershell
cd C:\working\projects\ContentCreator\eduvid-pipeline

# 1. switch the renderer to the python-course branch
git fetch origin
git switch python-course
git pull

# 2. reinstall it into the existing venv (picks up the new `eduvid pycourse` code)
.\.venv\Scripts\Activate.ps1
python -m pip install -e .

# 3. clone this course next to eduvid-pipeline
cd ..
git clone -b python-course-v2 https://github.com/waqarys/Courses.git Courses

# 4. confirm the voice model and ffmpeg are found
eduvid doctor
ffmpeg -version
```

The download puts the voice files in `C:\Users\waqar\.eduvid\models\kokoro-onnx`, which is found automatically. If
`eduvid doctor` still doesn't find them after the download finishes, point it at the folder that holds
`kokoro-v1.0.onnx` and `voices-v1.0.bin`, for example `$env:KOKORO_DIR = "C:\Users\waqar\.eduvid\models\kokoro-onnx"`.

### Check and render

```powershell
cd C:\working\projects\ContentCreator
.\eduvid-pipeline\.venv\Scripts\Activate.ps1
git -C eduvid-pipeline pull
git -C Courses pull

# check every script: runs every program exactly as the video will; must end with RESULT: OK for all 38
eduvid pycourse check Courses\course_v2 --all

# render all 38 lessons (1080p30, NVENC)
eduvid pycourse render Courses\course_v2 --all --gpu

# one lesson, by folder or by id
eduvid pycourse check  Courses\course_v2\lessons\M1-02_Hello_World
eduvid pycourse render Courses\course_v2\lessons\M1-02_Hello_World --gpu
eduvid pycourse render Courses\course_v2 --id 4.10 --gpu

# exact length without making a video:      add --timing
# quick look first (720p, 15 fps):          add --preview
# only some sections:                       add --sections 5-6
# light editor instead of dark:             add --theme light
# no background music:                      add --no-music
```

Errors are printed by the Python that runs the lesson programs. The laptop venv is Python 3.11, so a few error
messages (the `^^^^` markers under a traceback line, for example) can look slightly different from the box renders
made with Python 3.13. The narration never quotes those markers.

Outputs go to `Courses\course_v2\lessons\<lesson>\render\` (git-ignored, never committed):

| File | Use |
|---|---|
| `<lesson>.mp4` | the video (1920×1080, 30 fps, AAC, −16 LUFS) |
| `<lesson>.srt` | English captions (upload separately; nothing is burned in) |
| `<lesson>_chapters.txt` | YouTube chapters with real timestamps |
| `<lesson>_thumb.jpg` | 1280×720 thumbnail |
| `<lesson>_youtube.txt` | title, description + chapters, tags |
| `<lesson>_timeline.json` | section start times (for checking) |

Re-rendering after an edit is fast: every spoken sentence is cached, so only changed sentences are re-spoken.

## Upload notes
* Audience setting: the other Fun Skill Builders series are set to "No, it's not made for kids". This course is aimed at
  ages 7 to 20, so confirm that setting against YouTube's made-for-kids rules before the first upload.
  Descriptions say "For beginners aged 7 to 20".
* Schedule; nothing goes public immediately.
