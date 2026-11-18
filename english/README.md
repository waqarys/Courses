# Everyday English — Fun Skill Builders (teen and adult learners, NOT made for kids)

Four original English-learning series, written for learners from A2 to B1 level. Format inspired by picture-vocabulary channels, but every
word list, example, question and dialogue here is our own writing (see [CREDITS.md](CREDITS.md)).

| # | Series | Lessons | Folder | Style |
|---|---|---|---|---|
| 1 | Everyday English with Pictures | 16 | [01_everyday_pictures](01_everyday_pictures/OUTLINE.md) | guess the picture → listen & repeat → meaning → Q&A example; reviews + final test |
| 2 | English Quiz Challenge 20/20 | 12 | [02_quiz_challenge](02_quiz_challenge/OUTLINE.md) | 20 (finale 30) multiple-choice questions, 5-second timer, reveal + reason, score check |
| 3 | Speak English Daily | 12 | [03_speak_daily](03_speak_daily/OUTLINE.md) | two-voice dialogue: Listen → Understand → Shadow → Role-play (both sides) → useful phrases |
| 4 | Verb Forms & Grammar with Pictures | 10 | [04_grammar_pictures](04_grammar_pictures/OUTLINE.md) | study cards + picture drills (V1 V2 V3 chant, fill the gap, spot the mistake) |

* Settings: [course.yaml](course.yaml) (voices af_heart + am_michael, speed 0.9, CC0 music bed, timers) and one
  `course.yaml` per series (name, colour, timers).
* One lesson = `<series>/lessons/<ID_Name>/lesson.md`: narration, on-screen items, quiz/practice pauses, YouTube
  title/description/tags and the Shorts list, all in one file. Format: `docs/ENGLISH_FORMAT.md` in eduvid-pipeline.
* Renderer: `eduvid english` in [waqarys/eduvid-pipeline](https://github.com/waqarys/eduvid-pipeline/tree/english-course),
  branch `english-course` (built on `python-course`, so `eduvid pycourse` still works).
* Every description gets the word list, chapters, subscribe link, OpenMoji picture credit and music credit automatically.
  Upload setting for every video and Short: **No, it's not made for kids**. Schedule them (never public at once).

## Laptop (Windows, PowerShell)

### Once

```powershell
cd C:\working\projects\ContentCreator
.\eduvid-pipeline\.venv\Scripts\Activate.ps1

# renderer: switch to the english-course branch and reinstall into the venv
git -C eduvid-pipeline fetch origin
git -C eduvid-pipeline switch english-course
git -C eduvid-pipeline pull
python -m pip install -e .\eduvid-pipeline

# content: switch the Courses clone to this branch (Courses\course_v2 stays the same on this branch)
git -C Courses fetch origin
git -C Courses switch english-everyday-v1
git -C Courses pull
```

The first render downloads the OpenMoji icons (about 47 MB, once) into `C:\Users\waqar\.eduvid\openmoji`.
The Kokoro voice files are found as for the Python course (`$env:KOKORO_DIR` if needed).

### Check and render

```powershell
cd C:\working\projects\ContentCreator
.\eduvid-pipeline\.venv\Scripts\Activate.ps1
git -C eduvid-pipeline pull
git -C Courses pull

# every lesson must end with RESULT: OK
eduvid english check Courses\english --all

# series 1 (16 lessons) and its Shorts
eduvid english render Courses\english\01_everyday_pictures --all --gpu
eduvid english short  Courses\english\01_everyday_pictures --all --gpu

# the other series the same way
eduvid english render Courses\english\02_quiz_challenge --all --gpu
eduvid english short  Courses\english\02_quiz_challenge --all --gpu
eduvid english render Courses\english\03_speak_daily --all --gpu
eduvid english short  Courses\english\03_speak_daily --all --gpu
eduvid english render Courses\english\04_grammar_pictures --all --gpu
eduvid english short  Courses\english\04_grammar_pictures --all --gpu

# one lesson by id, a quick look, exact length, or the narration text
eduvid english render Courses\english --id V01 --gpu
eduvid english render Courses\english --id V01 --preview
eduvid english render Courses\english --id V01 --timing
eduvid english script Courses\english --id V01
```

Outputs: `Courses\english\<series>\lessons\<lesson>\render\` (git-ignored): `<lesson>.mp4`, `.srt` (upload as a
separate caption file), `_chapters.txt`, `_thumb.jpg`, `_youtube.txt`, and `<lesson>_shortN.mp4` + `_shortN_youtube.txt`.

Regenerate the lesson tables in the OUTLINE files after editing: `python Courses\english\make_outline.py`.
