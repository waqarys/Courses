# Live Coding – Lesson 01 Hello, World

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/05_*.py`.

## live_01 – Hello, World!

**Type this slowly, saying each part out loud:**

```python
# My first program
print("Hello, World!")
```

**What to say:**
- # means Python skips that line.

**Expected output** (Run ▶ / F5):
```
Hello, World!
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Spot the mistake: Capitals matter

**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.

```python
Print("Hello, World!")
```

**What to say:**
- Print is not print.
- Fix the P.
- Run again.

**Expected output** (Run ▶ / F5):
```
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – Two lines, in order

**Type this slowly, saying each part out loud:**

```python
print("Hello, World!")
print("I am learning Python.")
```

**What to say:**
- Line 1 finishes.
- Then line 2.
- That is sequence.

**Expected output** (Run ▶ / F5):
```
Hello, World!
I am learning Python.
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 01 — Hello, World

Book 1.4, 1.8, 1.9. Length: 9 min. File: `hello_world.py`.

Slides

1. Title. First program. One line. If Python is not open, stop and use the last videos, then come back.
2. `print` sends words to the screen. The words sit inside quotes. The line starts with `#` if it is a note, not code.
3. Smoke test: like turning a car on, not driving it across the city. Does it start? Does it print exactly `Hello, World!`?
4. SWITCH. Type:

```python
# My first program
print("Hello, World!")
```

Run it. Point at the output, not the code.
5. Mistake: `Print("Hello, World!")` with a capital P. Python is case-sensitive. `Print` is not `print`. Fix it.
6. Second run, still in Thonny:

```python
print("Hello, World!")
print("I am learning Python.")
```

Say: each line finishes before the next one starts. That is sequence. We name it properly in video 18.
7. The wellbeing game is where this course ends up: a small check-in a student can run. We will not build it today. We need variables first.
8. Your turn: change the second print to your first name. Run it. Next: what Python is.
