# OBS Setup – live coding only

You record **only the live coding**. Concept explanations, intro/outro (unless you want your voice) and the
"Your turn" card are made by `tools/render_video.py`.

## Import (once)
Use the existing studio pack: follow `studio/IMPORT.txt` (unzip to `C:\PythonForKidsStudio`, import
`obs/Python-for-Kids.json`). You get scene **Teach**: screen + mint snake + webcam circle (bottom-right, 320×320,
Alpha Mask `circle-mask-alpha.png`).

## Scenes
| Scene | Sources | Use |
|---|---|---|
| **Teach** (Thonny) | Window Capture → `Thonny`, Camera (circle mask), Snake (optional) | Default for every lesson |
| **Teach IntelliJ** | Duplicate *Teach* (right-click → Duplicate), change the Window Capture to IntelliJ IDEA / PyCharm | Older kids, bigger programs |
| Slides | not needed any more | the AI explainer replaces slides |

Editor settings: font 24+ (Thonny: Tools → Options → Theme & Font; IntelliJ: Settings → Editor → Font 24 and
View → Appearance → Presentation Mode), light theme, close extra panels, window ≈ 1600×900 so the webcam circle
does not hide code (keep the bottom-right corner of the editor empty).

## Settings
- Video: Base and Output 1920×1080, 30 fps.
- Output → Recording: format **MKV** (safe if OBS crashes; the renderer reads MKV directly) or MP4; Encoder
  **NVIDIA NVENC H.264** (RTX 3050), Rate control CQP 20–23; Recording path = the lesson's `live` folder.
- Audio: Mic/Aux only, Desktop Audio muted (or keep it low if you want the Thonny bell). Mic filters in order:
  Noise Suppression (RNNoise) → Noise Gate → Compressor (ratio 4:1) → Limiter (−1 dB).
  Loudness does not need to be perfect: the renderer normalises every clip to −16 LUFS.
- Hotkeys: F9 Start/Stop recording, F10 Pause.

## Per step
1. Open `Live_Coding.md` at `live_01`. Empty editor.
2. F9. Say the task, type slowly, say each part, run (F5), point at the output. Deliberate mistakes: run, read the error, fix, run.
3. F9 to stop. Rename to `live_01.mkv` (or .mp4). Next step.
A slip? Keep going and trim later in `live/trim.json`, or record that step again (overwrite the file).
