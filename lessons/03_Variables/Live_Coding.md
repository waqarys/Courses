# Live Coding – Lesson 03 Variables

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/06_*.py`.

## live_01 – Four boxes

**Type this slowly, saying each part out loud:**

```python
player_name = "Jimmy"
player_score = 0
is_game_over = False
health = 100.0
print(player_name, player_score, is_game_over, health)
```

**Expected output** (Run ▶ / F5):
```
Jimmy 0 False 100.0
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Change the score

**Type this slowly, saying each part out loud:**

```python
player_score = 50
print(player_score)
```

**What to say:**
- The name stayed.
- The value changed.

**Expected output** (Run ▶ / F5):
```
50
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – Constants shout

**Type this slowly, saying each part out loud:**

```python
PI = 3.14159
MAX_PLAYERS = 4
```

**What to say:**
- Python will not lock them.
- Capitals tell humans: leave this alone.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – Spot the mistake

**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.

```python
player-score = 50
```

**What to say:**
- A hyphen means minus.
- Use player_score.

**Expected output** (Run ▶ / F5):
```
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 03 — Variables are labeled boxes

Book 2.1.1–2.1.2. Length: 10 min. File: `variables.py`.

1. A variable is a name stuck on a box. The box holds a value. You can change what is in the box. That is why it is called variable.
2. One equals sign stores. It is not “equals” from maths. Read `score = 0` as “score gets 0”.
3. SWITCH. Type and run:

```python
player_name = "Jimmy"
player_score = 0
is_game_over = False
health = 100.0

print(player_name)
print(player_score)
print(is_game_over)
print(health)
```

4. Change `player_score = 0` to `player_score = 50`. Run again. The name stayed. The value changed.
5. A constant is a value you promise not to change. Python has no lock for that. We shout the name in capitals so humans leave it alone.

```python
PI = 3.14159
MAX_PLAYERS = 4
```

Say: Python will let you change `PI`. Do not.
6. Mistake: `player-score = 50`. The hyphen is minus, not a name. Use `player_score`.
7. Your turn: make `lives = 3`, print it, then set it to 2 and print again. Next: good names.
