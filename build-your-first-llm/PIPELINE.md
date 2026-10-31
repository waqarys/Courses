# PIPELINE — producing a "Zero to LLM" module with minimal editing

Tools: your **Windows laptop**, **Grok AI** (chat), **Grok Bot** (this assistant), **Grok Imagine**, **OBS Studio**, **IntelliJ IDEA**, **CapCut desktop**.
Principle: *all thinking happens before the record button; recording is reading; editing is mechanical.*

---
## 0. One-time setup (≈3 hours, once)
| # | Task | Guide | Time |
|---|---|---|---|
| 0.1 | Clone this branch: `git clone -b build-your-first-llm https://github.com/waqarys/Courses` | — | 5 min |
| 0.2 | Folder layout on disk (below) | §2 | 5 min |
| 0.3 | IntelliJ + Python venv + recording look + Live Templates | [templates/INTELLIJ_SETUP.md](templates/INTELLIJ_SETUP.md) | 40 min |
| 0.4 | OBS scenes, sources, audio filters, hotkeys | [templates/OBS_SCENES.md](templates/OBS_SCENES.md) | 45 min |
| 0.5 | CapCut template project + caption preset + export preset | [templates/CAPCUT_TEMPLATE.md](templates/CAPCUT_TEMPLATE.md) | 60 min |
| 0.6 | Thumbnail template in CapCut | [templates/THUMBNAIL_STYLE.md](templates/THUMBNAIL_STYLE.md) | 15 min |
| 0.7 | Teleprompter: second monitor/tablet with `build/<m>/teleprompter.html`, positioned right under the webcam | §4 | 10 min |
| 0.8 | Marp for slides: VS Code "Marp for VS Code" extension **or** `npm i -g @marp-team/marp-cli` | §3 | 10 min |

Optional but nice: a phone with Touch Portal/Stream Deck Mobile for OBS hotkeys.

## 1. The assembly line (per module)
```
PREP (Grok Bot + Grok)  →  ASSETS (Imagine)  →  RECORD (OBS+IntelliJ)  →  EDIT (CapCut)  →  PUBLISH (Grok Bot)
   45 min                     20 min               60–75 min                 45 min              15 min
```
**≈3–3.5 hours per 15-minute module.** That's the whole budget — if a step overruns, simplify, don't polish.

## 2. Folder layout on the laptop
```
D:\ZeroToLLM\
  code\zero-to-llm\m01 … m11\     ← IntelliJ project (snippets get pasted here)
  M05\
    takes\     M05_S01_CAM.mp4, M05_S02_SLIDES.mp4, …   (OBS output, renamed)
    broll\     intro.mp4, divider.mp4, outro.png, thumb_bg.png  (Imagine)
    export\    M05_final.mp4, M05_final.srt, M05_thumb.png
```
OBS writes to `D:\ZeroToLLM\takes\`; at the end of a session move + rename (ask Grok Bot, or rename by hand following the shot list).

## 3. PREP — the day before (≈45 min)
1. **Re-read the module** in `modules/NN_slug/`: `script.md`, `livecode.md`, `slides.md`.
2. **Personalise with Grok AI** (≈15 min): open the module's `grok_prompts.md`, run prompt **D (Script tighten)** with `script.md` attached and **E (Hook variations)**. Paste the parts you like back into `script.md`. Keep the `## S… · SCENE · name (≈time)` header lines unchanged — the helper parses them.
3. **Build outputs** (≈1 min): `python tools/prep_module.py 05` → `build/05_…/` gets `teleprompter.html`, `teleprompter.txt`, `shot_list.md`, `snippets/`, `upload.json`, `description.txt`.
4. **Slides**: open `modules/05_…/slides.md` in VS Code with Marp, check it, then export HTML for recording:
   `marp --theme-set templates/marp-theme.css modules/05_attention-from-scratch/slides.md -o build/05_attention-from-scratch/slides.html` (PDF already in the module folder).
5. **Dry-run the code** (≈15 min): paste every snippet into `code\zero-to-llm\m05\` and run it once. Pre-download models. Create Live Templates for the long snippets (`m05a`, `m05b`…).
6. Print or keep `shot_list.md` open.

**Or ask Grok Bot to do steps 2–4:** *"Grok Bot, prep module 05 of Zero to LLM: tighten the script with my style, run prep_module.py, export the slides HTML and PDF, and push to the build-your-first-llm branch."*

## 4. ASSETS — Grok Imagine (≈20 min)
Open `modules/05_…/imagine.md`. Generate, in this order:
1. **Thumbnail background** (image) — pick best of 4.
2. **Intro sting** (image → *Make video*, 5 s).
3. **Big-idea b-roll** (6–8 s) — used once in a SLIDES segment.
4. Reuse **divider loop** and **outro background** from M01 for every module (consistency + saves time).
Save to `D:\ZeroToLLM\M05\broll\`. Make the thumbnail now (THUMBNAIL_STYLE.md) — while the topic is fresh.

## 5. RECORD — OBS + IntelliJ (≈60–75 min for 15 min of video)
Session checklist (2 min): Windows *Do Not Disturb* on · phone silent · water · webcam framed, eyes level · light in front · IntelliJ Presentation look · slides HTML in full-screen browser (F11) · teleprompter on screen under the camera · OBS 10-second test take, check audio peaks −12…−6 dB.

For each row of `shot_list.md`:
1. **Ctrl+Alt+1/2/3** to the scene in the "OBS scene" column.
2. **Ctrl+Alt+F12** (Split recording) — or F9 to start the first time.
3. 2 s silence → read the beats (Space on the teleprompter to scroll) → 2 s silence.
4. Fumble → stop, 2 s silence, restart *that beat*. Never restart the segment unless it's unrecoverable.
5. IDE segments: follow `livecode.md`; type only the lines marked "Type live", paste/Live-Template the rest. If code errors on camera — keep calm, fix it, explain (viewers like it), CapCut trims the dead air.
6. Training runs or long downloads: switch to **IDE-FULL** (Ctrl+Alt+4), keep recording silently; it gets sped up 8×.
7. Tick the row.
End: **Ctrl+Alt+F10**. Move files to `M05\takes\` and rename to the shot-list names (`M05_S03_SLIDES.mp4`).
Then (optional) `python tools/prep_module.py 05 --durations D:\ZeroToLLM\M05\takes` → chapter times in `upload.json` now come from your real clips (needs `ffprobe`, from ffmpeg: `winget install Gyan.FFmpeg`).

Rules that remove editing: one segment = one file · same scene settings every time · no zooms · retake beats, not segments · don't watch takes back during the session.

## 6. EDIT — CapCut (≈45 min)
Follow [templates/CAPCUT_TEMPLATE.md §B](templates/CAPCUT_TEMPLATE.md): duplicate template → drop takes in order → Remove silences → speed-up long runs → edit 3 text boxes → Auto captions + preset → normalise loudness → export MP4 + SRT. Then watch **only the first 60 s and the last 60 s** at 1×, and scrub the rest at 2×. Don't re-edit for perfection.

## 7. PUBLISH — with Grok Bot (≈15 min of your time)
Copy `M05_final.mp4`, `M05_final.srt`, `M05_thumb.png` somewhere Grok Bot can reach (Google Drive folder `ZeroToLLM/M05/` works well). Then send Grok Bot:

> *Upload Drive ZeroToLLM/M05/M05_final.mp4 to my channel Waqar Shaikh Builds as **Private**, using build-your-first-llm/build/05_attention-from-scratch/upload.json for title, description, tags and chapters. Set the thumbnail M05_thumb.png, upload M05_final.srt as English captions, add it to the playlist "Zero to LLM — Build Your Own Language Model" in module order, add end screens to the previous and next module, and send me the link.*

Grok Bot will also, on request:
- create the playlist the first time and keep it sorted by module number;
- replace `<PLAYLIST_LINK>`, `<PREV_LINK>`, `<NEXT_LINK>` in descriptions once links exist;
- generate the pinned comment and community-tab poll (grok_prompts.md F and B) and draft them for your approval;
- switch videos from Private to **Scheduled** at your chosen time after you've reviewed them;
- regenerate a thumbnail background with Grok Imagine if you don't like yours.
You review the Private video on your phone (5 min) → reply "publish M05 Tuesday 7 pm IST".

## 8. Per-video checklist (copy into an issue or Notion page)
| ☐ | Step | Who | Est. |
|---|---|---|---|
| ☐ | Script tightened (Grok D, E) & `prep_module.py` run | you / Grok Bot | 30 min |
| ☐ | Code dry-run, models cached, Live Templates made | you | 15 min |
| ☐ | Slides HTML exported & checked | you / Grok Bot | 5 min |
| ☐ | Imagine: thumb bg, intro sting, b-roll | you | 20 min |
| ☐ | Thumbnail made | you | 10 min |
| ☐ | Recording session (all shot-list rows ticked) | you | 60–75 min |
| ☐ | Takes renamed; `--durations` run | you / Grok Bot | 5 min |
| ☐ | CapCut edit + captions + export | you | 45 min |
| ☐ | Spot-check first/last minute | you | 5 min |
| ☐ | Upload Private + thumb + captions + playlist | Grok Bot | — |
| ☐ | Review on phone, approve schedule | you | 5 min |
| ☐ | Quiz/poll/pinned comment drafted (Grok A, B, F) | Grok Bot | — |
| | **Total of your time** | | **≈3.3 h** |

## 9. Weekly cadence (2 modules/week → 11 modules in ~6 weeks)
| Day | Block | Work |
|---|---|---|
| Mon (evening, 1.5 h) | PREP | Prep module A + B (scripts tightened, code dry-run, slides) |
| Tue (1 h) | ASSETS | Imagine + thumbnails for A and B |
| Wed (2 h) | RECORD | Record A **and** B back-to-back (same lighting, same clothes = consistent series) |
| Thu (1.5 h) | EDIT | Edit A, export; hand to Grok Bot for Private upload |
| Fri (1 h) | EDIT | Edit B, export; hand over |
| Sat (15 min) | REVIEW | Review both Private uploads, approve schedule (e.g. Tue & Fri 7 pm IST) |
| Sun | off | Grok Bot posts community poll for next week's topic (after approval) |

Batching rule: always record two modules in one session — setup cost is paid once.
Suggested release order is the module order; if you want to start with a "wow" video, release **M06 (Rebuild GPT-2)** as a standalone teaser first — it works without the earlier ones.

## 10. If you're short on time
- Skip the b-roll and divider (intro sting + thumbnail only).
- Record SLIDES segments as one take with Split between slides.
- Use YouTube auto-captions instead of the CapCut SRT.
- M01, M10, M11 are mostly slides/camera → fastest modules; do them on a tired week.

## 11. Helper reference
`python tools/prep_module.py --help` · outputs land in `build/` (git-ignored). The module source files are the single source of truth; regenerate `build/` any time.
