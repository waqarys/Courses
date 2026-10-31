# YouTube uploader (no Grok Bot usage)

One command uploads a rendered lesson to YouTube: **long video + Short + thumbnail + captions (SRT) + playlist + schedule**.
It uses the official YouTube Data API and runs on your Windows laptop (or WSL). It is safe to re-run, because
`uploaded.json` remembers what is already done.

Works with the render folders from `HighSchoolCourses/.../Science-Olympiad` (`NN_Topic/YouTube.md`, `Intro_Outro.md`,
`render/NN_Topic_full.mp4`, `_short.mp4`, `_full.srt`, `_full_chapters.txt`, `_thumb.jpg`) and with flat staging
folders (`02_Plants_YouTube.md`, `02_Plants_full.mp4`, `02_desc.txt`, `02s_desc.txt` ...). The Python-for-Kids lessons use the same layout
(`layout: python_kids` in config).

## Setup checklist (10 minutes, once)
1. Install Python 3.11+ from python.org (tick "Add to PATH").
2. Copy this `youtube-uploader` folder anywhere, e.g. `C:\working\youtube-uploader`.
3. Do **SETUP_GOOGLE.md** steps 1-5. This creates the Google project, turns on the API, adds you as a test user,
   and gets you `secrets\client_secret.json`.
4. `copy config.example.yaml config.yaml` and check `series_root`, `playlist` and `schedule.times` for each channel.
5. `run.bat auth --channel happy` (pick **Happy Learners ICSE** in the browser), then `run.bat auth --channel build`.
   Put the printed `channel_id` values in `config.yaml`.
6. Tell it about videos you already uploaded by hand, so they are never uploaded twice:
   ```bat
   run.bat mark 01_Intro  --channel happy --long-id bHWbCsvNers --short-id gEXMRf1JhXM
   run.bat mark 02_Plants --channel happy --long-id 6VNA24xQH5E --short-id NPxRe46vJfo --publish-at "2026-11-01 07:00"
   ```
7. Test without uploading: `run.bat queue --channel happy --dry-run`

## Daily use (one command)
Finish rendering, then:
```bat
run.bat upload "C:\working\Content\HighSchoolCourses\Grade2\Science-Olympiad\03_Animals" --channel happy
```
It picks the **next free slot** (default every day 07:00 IST; the Short goes 1 hour later), uploads, sets the thumbnail,
English (India) captions and the playlist, marks the video made for kids, and prints the links.

Or upload everything rendered but not yet uploaded:
```bat
run.bat queue --channel happy
```

| what | command |
|---|---|
| preview metadata, nothing uploaded | add `--dry-run` |
| publish right now (public) | `upload <folder> --channel happy --now` |
| exact time | `upload <folder> --channel happy --at "2026-11-05 17:00"` |
| skip the Short | `--no-short` |
| one video from a flat folder | `upload C:\staging --name 04_Human_Body --channel happy` |
| what's uploaded / next slot | `run.bat status --channel happy` (`--remote` also asks YouTube) |
| Python series | `run.bat upload <lesson_folder> --channel build` |

The schedule is set in `config.yaml` → `schedule:` (`times: ["07:00"]`, `days: daily` or `[mon, wed, fri]`,
`short_offset_minutes: 60`). Each channel can have its own.

**What goes in the description:** `NN_desc.txt` if it exists. Otherwise it's your intro text (from `Intro_Outro.md`), then the
`YouTube.md` description with its chapter list replaced by the real `render/..._chapters.txt`, trimmed to 3 hashtags.
Tags come from `YouTube.md` (max 14), with category Education (27) and language en-IN. The Short's description comes from `NNs_desc.txt` (or the
first paragraph), plus `Full lesson: https://youtu.be/<id>` and `#Shorts`. Its title is taken from `short_title.txt`, then from a
`## Short title` section in `YouTube.md`, then from the first question in the Short's description.

## Run it automatically every night (optional)
Windows Task Scheduler, 11 PM daily (one line in **cmd**; change the path):
```bat
schtasks /Create /SC DAILY /ST 23:00 /TN "YouTube queue happy" /TR "powershell -NoProfile -ExecutionPolicy Bypass -File C:\working\youtube-uploader\run.ps1 -Log queue --channel happy"
```
Remove it: `schtasks /Delete /TN "YouTube queue happy" /F`. Logs go to `logs\`. The laptop must be on and online.
The first sign-in must be done by hand (step 5). If the token expires in testing mode, the nightly run can't sign in
again by itself, so publish the app "In production" (SETUP_GOOGLE.md step 3) for unattended use.

**WSL:** `./run.sh upload /mnt/c/working/Content/.../03_Animals --channel happy`. Keep `config.yaml` paths as `/mnt/c/...`,
or use a separate config with `--config`.

## Troubleshooting
| message | fix |
|---|---|
| `Not enough quota left today` / `quotaExceeded` | The free quota is 10,000 units/day (about 2 lessons). Run again after 12:30 PM IST. Nothing is lost: it continues where it stopped. |
| `uploadLimitExceeded` | YouTube's own daily upload cap for the channel. Try again tomorrow. |
| browser opens again / `invalid_grant` / `Token has been expired or revoked` | Testing-mode sign-ins expire after 7 days. Sign in again, or publish the app (SETUP_GOOGLE.md step 3). Still failing? Delete `secrets\token_happy.json` and run `auth` again. |
| `Signed in as channel X but config expects Y` | You picked the wrong channel at sign-in. Delete that token file and run `auth` again. |
| `LOCKED PRIVATE` | See "Fallback" in SETUP_GOOGLE.md: change visibility/schedule in Studio, or set `upload: mode: private`. |
| `captions: FAILED` | Usually the video is still processing or the SRT is malformed (it needs `00:00:01,000 --> ...` lines). The next `upload`/`queue` run retries only the captions. You can also upload the `.srt` in Studio → Subtitles. |
| `thumbnail: FAILED ... forbidden` | Verify the channel by phone (youtube.com/verify). It retries on the next run. |
| `publishAt` error / video went public at once | The time was in the past or less than about 15 minutes away. Use `--at` with a later time. |
| `client_secret.json not found` | Put it in `secrets\` (SETUP_GOOGLE.md step 5). |
| Wrong text in description | Fix `YouTube.md` / `NN_desc.txt` *before* uploading, and check with `--dry-run`. After upload, edit in Studio. |

## Safety (public repo)
`secrets/`, `client_secret*.json`, `token*.json`, `config.yaml` and `uploaded.json` are all in `.gitignore`. Never `git add -f` them.

## For developers
`python -m pytest tests -q` runs the metadata, chapter, SRT, slot and state tests, plus the upload flow against a fake API.
Set `YTUP_TEST_FLAT` / `YTUP_TEST_REPO` to sample render folders. Code: `ytup/metadata.py` (files → title/description/tags),
`ytup/schedule.py` (slots), `ytup/state.py` (uploaded.json, quota), `ytup/api.py` (API, retries), `ytup/cli.py` (commands).
