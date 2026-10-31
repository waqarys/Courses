# CapCut (desktop) — the reusable "Zero to LLM" template project

Goal: editing a 15-minute module takes **≤ 45 minutes**: drop clips → auto-captions → remove silences → export.

## A. Build the template ONCE (≈1 hour)
1. New project, ratio **16:9**, 1080p 30 fps. Name it `ZTL_TEMPLATE`.
2. Track layout (top → bottom):
   | Track | Contents |
   |---|---|
   | Text 1 | lower-third (module number + title) — 5 s at 0:08 |
   | Text 2 | auto captions (added per video) |
   | Overlay 1 | section divider sting (4 s Imagine loop) — placeholders |
   | Main | 00 Intro sting (Imagine clip 5 s + logo) · **[drop takes here]** · 99 Outro (20 s end-screen background) |
   | Audio 1 | music bed for intro/outro only, −24 dB, fade 1 s |
3. **Intro (8 s total):** Imagine intro clip + text "Zero to LLM" (Montserrat ExtraBold, white, cyan glow) + module title text box (you only edit the words) + whoosh SFX. Save it as a **Compound clip** → right-click → *Add to My presets / "Save as template"* so it drops in as one block.
4. **Lower-third:** text animation "Typewriter" in, "Fade" out; navy rounded rectangle 70 % opacity behind. Save as **Text template** ("ZTL lower third").
5. **Captions style:** Captions → Auto captions → after generating, set style: Montserrat SemiBold 52, white, 4 px black stroke, position lower centre (above webcam circle: y ≈ 78 %), max 2 lines, highlight keyword colour #22D3EE. Click **"Save as preset"** ("ZTL captions").
6. **Outro (20 s):** Imagine outro background + "Next: Mxx" text placeholder. Leave the area for YouTube end-screen elements (two video boxes + subscribe) clear.
7. **Adjustment layer** (optional): slight sharpen +10, no colour LUT (OBS colours are already set).
8. **Export preset:** 1080p · 30 fps · H.264 · bitrate *Recommended/Higher* · MP4 · "Export captions" **SRT** ticked. Save as preset "ZTL 1080p".
9. File → **Duplicate project** each time — never edit the template itself.

## B. Per-video edit (≈30–45 min)
| # | Step | Time |
|---|---|---|
| 1 | Duplicate `ZTL_TEMPLATE` → `M05_Attention` | 1 min |
| 2 | Import the folder `D:\ZeroToLLM\M05\takes\` (files already named `M05_S01_CAM…`); select all → drag onto Main between intro and outro — they land in order | 2 min |
| 3 | Select the takes → right-click → **Remove silences** (threshold "Medium", keep 0.2 s padding). Check and delete any fumbled half-sentences you flagged with your "re-read" pause | 10–15 min |
| 4 | Training/progress segments: select → Speed 4–8× (curve speed off) | 2 min |
| 5 | Edit intro title + lower-third text (2 words) and outro "Next" text | 3 min |
| 6 | Drop a divider sting at the 2–3 biggest section changes (optional) | 3 min |
| 7 | **Captions → Auto captions** (English) → apply "ZTL captions" preset → skim for technical words (PyTorch, LoRA, tiktoken, softmax) and fix | 8–10 min |
| 8 | Audio: Normalise loudness on all takes (Audio → *Normalize loudness*, target −14 LUFS); enable *Enhance voice* only if the room was noisy | 2 min |
| 9 | Export with "ZTL 1080p" preset → `D:\ZeroToLLM\M05\export\M05_final.mp4` + `.srt` | 5 min (render) |

## C. Things NOT to do (they eat hours)
- No zoom/pan keyframes on IntelliJ — use font size 20 + Presentation Mode while recording instead.
- No B-roll over code. B-roll only on CAM and SLIDES segments.
- No re-ordering takes: the script order *is* the edit order.
- No colour grading.
