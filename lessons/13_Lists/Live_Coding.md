# Live Coding – Lesson 13 Lists

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/16_*.py`.

## live_01 – Scores

**Type this slowly, saying each part out loud:**

```python
scores = [85, 92, 78, 95, 88]
print(len(scores))
print(scores[0])
print(scores[4])
scores[2] = 80
print(scores)
```

**What to say:**
- Length 5.
- First 85.
- Last 88.
- Middle becomes 80.

**Expected output** (Run ▶ / F5):
```
5
85
88
[85, 92, 80, 95, 88]
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Spot the mistake

**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.

```python
print(scores[5])
```

**What to say:**
- There is no locker 5.
- Lockers: 0 1 2 3 4.
- IndexError means that number does not exist.

**Expected output** (Run ▶ / F5):
```
IndexError: list index out of range
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 13 — Lists, not 30 variables

Book 3.1–3.1.7. Length: 11 min. File: `lists.py`.

1. A list is a row of boxes in one variable. Index 0 is the first box. The last index is length minus 1.
2. In other languages an array is often one type and a fixed size. In Python, start with a list. It can grow. It can mix types. You do not import anything.
3. SWITCH.

```python
scores = [85, 92, 78, 95, 88]
print(len(scores))
print(scores[0])
print(scores[4])
scores[2] = 80
print(scores)
```

4. Say it: length 5, first 85, last 88, then the middle box changes from 78 to 80.
5. Mistake: `print(scores[5])`. There is no box 5. Boxes are 0, 1, 2, 3, 4. Read `IndexError` as “that locker number does not exist.”
6. Your turn: a list of 4 favourite foods. Print the first and the last. Next: change the list.
