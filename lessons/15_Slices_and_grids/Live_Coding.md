# Live Coding – Lesson 15 Slices and grids

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/18_*.py`.

## live_01 – Slice

**Type this slowly, saying each part out loud:**

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[1:4])
print(numbers[1:5:2])
```

**What to say:**
- 50.
- 20, 30, 40.
- 20, 40.
- Stop is not included.

**Expected output** (Run ▶ / F5):
```
50
[20, 30, 40]
[20, 40]
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – A grid is a list of lists

**Type this slowly, saying each part out loud:**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0][1])
matrix[1][1] = 10
print(matrix)
```

**What to say:**
- Row, then column.
- Both start at 0.
- [0][1] is 2.

**Expected output** (Run ▶ / F5):
```
2
[[1, 2, 3], [4, 10, 6], [7, 8, 9]]
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 15 — Slices and grids

Book 3.1.10–3.1.11. Length: 10 min. File: `grids.py`.

1. Negative index: `-1` is the last box, `-2` the one before.
2. A slice is `start:stop:step`. Stop is not included.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[1:4])
print(numbers[1:5:2])
```

50, then `[20, 30, 40]`, then `[20, 40]`.
3. A grid is a list of lists. Row, then column. Both start at 0.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0][1])
matrix[1][1] = 10
print(matrix)
```

`[0][1]` is 2. Then the 5 becomes 10.
4. Add a row with `append`. Delete a row with `del matrix[0]`.
5. Your turn: print the 6. It is row 1, column 2: `matrix[1][2]` before you change anything. Next: dictionaries.
