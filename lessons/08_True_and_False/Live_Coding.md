# Live Coding – Lesson 08 True and False

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/11_*.py`.

## live_01 – Try a score

**Type this slowly, saying each part out loud:**

```python
score = 85
print(score > 80)
print(score == 100)
print(score < 40)
```

**What to say:**
- True, False, False.

**Expected output** (Run ▶ / F5):
```
True
False
False
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – = stores. == asks.

**Type this slowly, saying each part out loud:**

```python
name = "Alex"
is_admin = name == "Admin"
print(is_admin)
```

**Expected output** (Run ▶ / F5):
```
False
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – and, or, not

**Type this slowly, saying each part out loud:**

```python
has_sword = True
has_shield = False
print(has_sword and has_shield)
print(has_sword or has_shield)
print(not False)
```

**What to say:**
- And: both.
- Or: at least one.
- Not: flip.

**Expected output** (Run ▶ / F5):
```
False
True
True
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 08 — True, False, and comparisons

Book 2.2.4–2.2.5. Length: 12 min. File: `booleans.py`.

1. A Boolean is only `True` or `False`. Capital T and F. `true` is a crash.
2. Comparisons make Booleans: `==`, `!=`, `>`, `<`, `>=`, `<=`.
3. SWITCH.

```python
score = 85
is_high_score = score > 80
is_perfect = score == 100
is_failing = score < 40
print(is_high_score, is_perfect, is_failing)
```

True, False, False.
4. One `=` stores. Two `==` asks “same?”.

```python
name = "Alex"
is_admin = name == "Admin"
print(is_admin)
```

5. `and` needs both. `or` needs one. `not` flips.

```python
has_sword = True
has_shield = False
print(has_sword and has_shield)
print(has_sword or has_shield)
is_game_over = False
print(not is_game_over)
```

6. Truth table, say it slowly. AND is True only on True/True. OR is False only on False/False. NOT flips the one box.
7. Mistake: `if score = 80` comes later; today just show `score = 80` versus `score == 80` side by side on the slide, and type only the comparison.
8. Your turn: `lives = 3`, print whether `lives > 0`. Next: maths.
