# Live Coding – Lesson 16 Dictionaries

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/19_*.py`.

## live_01 – A student

**Type this slowly, saying each part out loud:**

```python
student = {
    "name": "Jimmy",
    "age": 15,
    "grade": "Year 10",
}
print(student["name"])
print(student["age"])
```

**Expected output** (Run ▶ / F5):
```
Jimmy
15
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Add, change, delete

**Type this slowly, saying each part out loud:**

```python
student["school"] = "Code High"
student["age"] = 16
del student["grade"]
print(student)
```

**Expected output** (Run ▶ / F5):
```
{'name': 'Jimmy', 'age': 16, 'school': 'Code High'}
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 16 — Dictionaries

Book 3.2. Length: 10 min. File: `dictionary.py`.

1. A list uses positions. A dictionary uses labels. Curly braces. `"key": value`. Commas between pairs.
2. SWITCH.

```python
student = {
    "name": "Jimmy",
    "age": 15,
    "grade": "Year 10",
}
print(student["name"])
print(student["age"])
```

3. Add, change, delete.

```python
student["school"] = "Code High"
student["age"] = 16
del student["grade"]
print(student)
```

4. Keys are unique. Values can repeat. A missing key crashes: `student["hobby"]`. Say: ask with a key you know exists.
5. Your turn: a dictionary for one game character with `name`, `level`, and `health`. Print the name. Next: three smaller types.
