# Live Coding – Lesson 10 Comments

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/13_*.py`.

## live_01 – Keep this

**Type this slowly, saying each part out loud:**

```python
# Starting score for a new player
score = 50
# Increase score for defeating an enemy
score = score + 1
```

**What to say:**
- Shorter: score += 1.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – A stub

**Type this slowly, saying each part out loud:**

```python
# TODO: ask for the player's name
def player_login():
    pass
```

**What to say:**
- Pass means: legal, but nothing yet.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 10 — Comments that help

Book 2.4. Length: 8 min. File: `comments.py`.

1. A comment is a note. Python skips it. `#` for one line. Triple quotes for a long note or a long string.
2. Three tests: relevant, not obvious, same style as the rest of the file.
3. SWITCH. Bad versus good, say which you would delete:

```python
# Starting score for a new player
score = 50

# Increase score for defeating an enemy
score = score + 1
```

Shorter: `score += 1`.
4. A stub marks work you have not done yet.

```python
# TODO: ask for the player's name
def player_login():
    pass
```

`pass` means “do nothing, but stay legal.”
5. Mistake to discuss, not a crash: `# This line uses a variable` above `score = 50`. That comment adds nothing. Delete it.
6. Your turn: put one useful comment above a score line. Next: pancakes.
