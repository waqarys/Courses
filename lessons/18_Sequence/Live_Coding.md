# Live Coding – Lesson 18 Sequence

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/21_*.py`.

## live_01 – Welcome

**Type this slowly, saying each part out loud:**

```python
player_name = input("Enter your name: ")
print("Welcome,", player_name)
score = 0
print("Score starts at", score)
```

**Expected output** (Run ▶ / F5):
```
Enter your name: Welcome, Sam
Score starts at 0
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 18 — One line after another

Book 4.1. Length: 8 min. File: `sequence.py`.

1. Three flows in this course: sequence (straight), selection (a choice), iteration (again).
2. Sequence means line 1 finishes, then line 2, then line 3. Python is interpreted: it reads a line and does it, then the next line.
3. A flowchart: oval start/stop, rectangle for a step, slanted box for input/output, diamond for a choice, arrows for direction. Today there is no diamond.
4. SWITCH.

```python
player_name = input("Enter your name: ")
print("Welcome,", player_name)
score = 0
print("Score starts at", score)
```

5. Point at the order. If you print `score` before `score = 0`, it crashes. Do that mistake. Move the line back.
6. Your turn: three lines that ask a colour and print it back. Next: choices.
