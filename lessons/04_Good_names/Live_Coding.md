# Live Coding – Lesson 04 Good names

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/07_*.py`.

## live_01 – Legal and illegal

**Type this slowly, saying each part out loud:**

```python
name = "Alex"
player_score = 100
level1 = 1
```

**What to say:**
- Illegal: 1level.
- Illegal: my name.
- Illegal: player-score.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – snake_case

**Type this slowly, saying each part out loud:**

```python
player_name = "Alex"
current_score = 100
is_game_active = True
```

**What to say:**
- CurrentScore is camelCase.
- Other languages use that.
- Python variables do not.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – Prefixes that help

**Type this slowly, saying each part out loud:**

```python
is_alive = True
has_key = False
num_players = 4
count_lives = 3
```

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 04 — Names that make sense

Book 2.1.3–2.1.8. Length: 10 min. File: `names.py`.

1. A name can be long. Letters, digits, underscore. It cannot start with a digit. No spaces. No hyphens.
2. SWITCH. Good, then show each bad line and do not leave it in the file:

```python
name = "Alex"
player_score = 100
level1 = 1
```

Bad, say them, do not run more than one: `1level`, `player-score`, `my name`.
3. Keywords are Python’s own words. You cannot steal them. `if`, `else`, `for`, `while`, `True`, `False`, `and`, `or`, `not`, `in`, `is`, `def`, `class`, `return`. So `if = 5` is illegal.
4. snake_case is the Python habit: `player_name`, `current_score`, `is_game_active`. `currentScore` is camelCase, used in other languages. `PlayerName` looks like a class. We do not use it for variables.
5. Start booleans with `is_` or `has_`. Start counters with `num_` or `count_`.

```python
is_alive = True
has_key = False
num_players = 4
count_lives = 3
```

6. Meaning: `score` beats `x`. `name` beats `n`. One letter is only fine for a tiny loop later.
7. Old style you might see and should not copy: `strName`, `intAge`. That is Hungarian notation. Skip it.
8. Quick quiz, answers after a pause: `int_user_number` is Hungarian. `CalculateArea` is PascalCase. `MAX_LIMIT` is a constant. `tempVal` is camelCase.
9. Your turn: rewrite `Eggs Count`, `sugarSpoons`, `Flour-Amount`, `IsVegetarian` as `eggs_count`, `sugar_spoons`, `flour_amount`, `is_vegetarian`. Next: text.
