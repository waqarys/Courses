# M01 — Live-coding plan (IntelliJ IDEA + Python plugin)

Project: `zero-to-llm` (one IntelliJ project for the whole course, see PIPELINE.md §3). File: `m01/next_token.py`.
Font: JetBrains Mono 20 pt, Presentation Mode (View → Appearance → Enter Presentation Mode), run window docked bottom.

| Step | Do | Say (beat) | Expected output |
|---|---|---|---|
| 1 | Paste `snippets/01_bigram_counts.py` (Live Template `m01a` or Ctrl+V) | "We count which word follows which." | — |
| 2 | Highlight `follows[current][nxt] += 1` | "This one line *is* the training." | — |
| 3 | Run (Ctrl+Shift+F10) | "After 'the', cat wins: 3 out of 6." | `after 'the'  -> {'cat': 0.5, 'mat': 0.17, ...}` |
| 4 | New file `generate.py`, paste snippet 02 | "Now the loop." | — |
| 5 | Run | "Greedy repeats itself; sampling wanders." | greedy line loops `the cat sat on the cat sat…` |
| 6 | Change `random.seed(0)` → `seed(1)`, run | "Different seed, different story — that's sampling." | new sampled line |

Type-live vs paste: type only the `+= 1` line and the `greedy` branch (the "aha" lines); paste the rest.
Fallback: if a run fails on camera, don't stop — fix, re-run, and cut in CapCut at the silence.
