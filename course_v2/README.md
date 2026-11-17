# Introduction to Python (course v2) — Fun Skill Builders

A complete beginner course for ages 7 to 20, hosted by **Pip the Python**. Each lesson explains the concept first,
then **types the code on screen line by line while Pip explains each line**, runs it for real, recaps, and ends with
an exercise (countdown + answer).

* **Outline (38 lessons, 5 modules):** [COURSE_OUTLINE.md](COURSE_OUTLINE.md)
* **Scripts:** `lessons/<lesson>/lesson.md` — Modules 1 and 2 (13 lessons) fully written
* **Programs for learners:** `code/` (regenerate with `python course_v2/export_code.py`)
* **Settings:** [course.yaml](course.yaml) (voice, speed, editor theme, music, pronunciations)
* **Renderer:** `eduvid pycourse` in [waqarys/eduvid-pipeline](https://github.com/waqarys/eduvid-pipeline/tree/python-course),
  branch `python-course`; lesson format in its `docs/PYCOURSE_FORMAT.md`

The older material on this branch (`lessons/`, `code/`, `slides/`, `tools/render_video.py`, the OBS workflow) is kept
unchanged. Course v2 does not need OBS or Grok Imagine pictures: everything is generated on the laptop.

## Render on the laptop (Windows, PowerShell)

Everything below runs inside `C:\working\projects\ContentCreator`, where `eduvid-pipeline` and `edu-video-forge`
are already cloned. edu-video-forge is not used for this course.

### Once

```powershell
cd C:\working\projects\ContentCreator

# 1. the renderer: switch the eduvid-pipeline clone to the python-course branch
cd eduvid-pipeline
git fetch origin
git switch python-course
cd ..

# 2. this course (a fresh clone, next to the other two repos)
git clone -b python-course-v2 https://github.com/waqarys/Courses.git Courses

# 3. Python environment (skip if you already have one with eduvid installed: then just run `pip install -e .\eduvid-pipeline` again)
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .\eduvid-pipeline

# 4. Kokoro voice model (~350 MB; skip if `eduvid doctor` already shows it)
eduvid models download --profile minimal
#    ...or reuse kokoro-v1.0.onnx + voices-v1.0.bin you already have:
#    $env:KOKORO_DIR = "C:\path\to\folder\with\kokoro\files"
```

ffmpeg must be on PATH (`ffmpeg -version`). The RTX 3050's NVENC encoder is used automatically.

### Each lesson

```powershell
cd C:\working\projects\ContentCreator
.\.venv\Scripts\Activate.ps1
git -C eduvid-pipeline pull
git -C Courses pull

# check the script: runs every program exactly as the video will, prints the outputs
eduvid pycourse check Courses\course_v2\lessons\M1-02_Hello_World

# render (1080p30, ~2 minutes on the laptop)
eduvid pycourse render Courses\course_v2\lessons\M1-02_Hello_World --gpu

# quick look first (720p, 15 fps):           add --preview
# only the coding part:                      add --sections 5
# light editor instead of dark:              add --theme light
# all written lessons in one go:             eduvid pycourse render Courses\course_v2 --all --gpu
# by id:                                     eduvid pycourse render Courses\course_v2 --id 2.4 --gpu
```

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
