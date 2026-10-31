# OBS Studio — scene collection "Zero to LLM"

Set this up **once** (≈45 min). After that every module is: pick scene → hotkey → talk.

## 1. Settings (File → Settings)
| Section | Setting | Value |
|---|---|---|
| Video | Base (canvas) | 1920×1080 |
| Video | Output (scaled) | 1920×1080 |
| Video | FPS | 30 |
| Output → Mode | | **Advanced** |
| Output → Recording | Type | Standard |
| | Recording path | `D:\ZeroToLLM\takes` (any fast drive) |
| | Recording format | **Hybrid MP4** (OBS 30.2+) — or MKV + "Automatically remux to MP4" (Advanced tab) |
| | Video encoder | NVIDIA NVENC H.264 (or AMD/Intel QSV H.264; x264 if no GPU) |
| | Rate control | CQP / CQ level **20** (NVENC) · CRF 20 (x264) |
| | Preset | P5 / Quality · Profile high · Look-ahead off · Keyframe 2 s |
| | Audio track | 1 |
| Audio | Sample rate | 48 kHz · Channels Stereo |
| Advanced | Filename formatting | `%CCYY-%MM-%DD_%hh-%mm-%ss` (you rename to `M05_S03_IDE` with the helper, see PIPELINE §5) |
| Advanced | Process priority | Above normal |

Why not stream settings? We record locally at high quality; YouTube re-encodes anyway. CQ 20 at 1080p30 ≈ 6–12 GB/hour — fine.

## 2. Audio chain (Mic source → right-click → Filters), in this order
1. **Noise Suppression** — RNNoise
2. **Expander** (or Noise Gate: close −45 dB, open −35 dB)
3. **Compressor** — ratio 3:1, threshold −18 dB, attack 6 ms, release 60 ms, output gain +3 dB
4. **Limiter** — threshold −1.5 dB
Target: speaking peaks around −12 to −6 dB on the mixer. Mute "Desktop Audio" in every scene (no notification sounds in takes).

## 3. Sources (create once, reuse in all scenes via "Add Existing")
| Source | Type | Setup |
|---|---|---|
| `Cam` | Video Capture Device | 1920×1080 30 fps (or 1280×720 if the webcam can't); filters: Color Correction (slight +contrast), optional **Background Removal** plugin not needed |
| `Cam Circle` | the same `Cam` added again + **Image Mask/Blend** filter with `templates/assets/circle_mask.png` (Type "Alpha Mask (Color Channel)") | size 340×340, position bottom-right **x 1540, y 700** (inside the free corner the Marp theme leaves) |
| `Ring` | Image `templates/assets/ring.png` (cyan 8 px ring, 356×356) | position x 1532, y 692 so it frames the circle |
| `Slides` | **Window Capture** → browser window with the Marp HTML (or PDF in full-screen Edge) — capture method "Windows 10 (1903+)" | Fit to screen |
| `IDE` | **Window Capture** → IntelliJ (`idea64.exe`), client area only | Fit to screen; crop the title bar |
| `Lower Third` | Text (GDI+) "Waqar Shaikh · Waqar Shaikh Builds" Montserrat 40 px on a navy rounded box image | only in CAM scene, hidden by default |

The two PNGs are already in `templates/assets/` (`circle_mask.png`, `ring.png`).

## 4. Scenes
| # | Scene | Sources (top → bottom) | Used for |
|---|---|---|---|
| 1 | **CAM** | Lower Third (hidden), Cam (full screen, slight zoom crop) | hook, recap, opinions |
| 2 | **SLIDES** | Ring, Cam Circle, Slides | concept segments |
| 3 | **IDE** | Ring, Cam Circle, IDE | live coding |
| 4 | **IDE-FULL** | IDE only | long typing / training runs (no face) |
| 5 | **BRB/BLANK** | Color source #0B1026 | pause safely between segments |

## 5. Hotkeys (Settings → Hotkeys) — pick keys IntelliJ doesn't use
| Action | Key |
|---|---|
| Start recording | **Ctrl+Alt+F9** |
| Stop recording | **Ctrl+Alt+F10** |
| Pause / unpause recording | **Ctrl+Alt+F11** |
| Scene CAM / SLIDES / IDE / IDE-FULL | **Ctrl+Alt+1 / 2 / 3 / 4** |
| Show/hide Lower Third | Ctrl+Alt+L |
| Split recording file (OBS 30+: "Split Recording") | **Ctrl+Alt+F12** — use this between segments instead of stop/start |

Optional: map these on a phone with **Touch Portal** or an Elgato Stream Deck (free "Stream Deck Mobile" trial) for one-tap scene changes.

## 6. Recording discipline (the reason editing is fast)
- One segment = one file. Switch scene → wait 1 s → hit **Split** (or Start) → 2 s silence → talk → 2 s silence → Split.
- Fumble? Stop talking, wait 2 s, re-read the beat. CapCut's *Remove silences* drops the gap; you delete the bad half-sentence (one cut).
- Never change OBS settings mid-module.
- Do a 10-second test take at the start of every session and check audio levels.

## 7. Export / backup of this setup
Scene Collection → Export → `templates/obs/ZeroToLLM_scenes.json`; Profile → Export → `templates/obs/ZeroToLLM_profile/`. Commit both (no secrets in them) so you can rebuild on a new laptop in 2 minutes. (Not included yet — export after you build it.)
