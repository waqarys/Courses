# Live Coding – Lesson 19 if, else, elif

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/22_*.py`.

## live_01 – Alive?

**Type this slowly, saying each part out loud:**

```python
player_health = 100
if player_health > 0:
    print("Player is alive")
```

**Expected output** (Run ▶ / F5):
```
Player is alive
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – else is plan B

**Type this slowly, saying each part out loud:**

```python
player_stamina = 0
if player_stamina > 0:
    print("You can sprint")
else:
    print("Too tired to run")
```

**What to say:**
- Else has no test.
- Same indent as if.

**Expected output** (Run ▶ / F5):
```
Too tired to run
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – elif asks the next question

**Type this slowly, saying each part out loud:**

```python
power_level = 75
if power_level >= 80:
    print("Super powerful")
elif power_level >= 50:
    print("Doing well")
elif power_level >= 20:
    print("Need more power")
else:
    print("Power depleted")
```

**What to say:**
- 75 prints Doing well.
- Python stops at the first True.
- Put the high bar first.

**Expected output** (Run ▶ / F5):
```
Doing well
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – and, or, not inside if

**Type this slowly, saying each part out loud:**

```python
has_key = True
knows_code = False
locked_by_magic = False
can_unlock = (has_key or knows_code) and not locked_by_magic
if can_unlock:
    print("You unlocked the chest")
```

**What to say:**
- Not, then and, then or.
- Brackets when it gets busy.

**Expected output** (Run ▶ / F5):
```
You unlocked the chest
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 19 — if, else, elif

Book 4.2–4.2.5. Length: 14 min. File: `choices.py`. Long on purpose. Cut the truth-table repeat if you run over.

1. `if` runs the indented lines only when the condition is True. Colon at the end. Indent 4 spaces. Thonny does this when you press Enter.
2. SWITCH.

```python
player_health = 100
if player_health > 0:
    print("Player is alive")
```

3. `else` is plan B. It has no condition.

```python
player_stamina = 0
if player_stamina > 0:
    print("You can sprint")
else:
    print("Too tired to run")
```

4. `elif` is another question, asked only if the earlier ones were False. Only one block runs.

```python
power_level = 75
if power_level >= 80:
    print("Super powerful")
elif power_level >= 50:
    print("Doing well")
elif power_level >= 20:
    print("Need more power")
else:
    print("Power depleted")
```

Say: 75 matches the second test. Python does not look at the rest. Order matters. Put the high bar first.
5. `and`, `or`, `not` again, now inside `if`. `not` first, then `and`, then `or`. Use brackets when it gets busy.

```python
has_key = True
knows_code = False
locked_by_magic = False
inventory_space = 5
required_space = 3

can_unlock = (
    (has_key or knows_code)
    and not locked_by_magic
    and inventory_space >= required_space
)
if can_unlock:
    print("You unlocked the chest")
else:
    print("The chest stays shut")
```

6. Mistake: `else player_stamina > 0:` — else must not have a condition. And `Else` with a capital is wrong.
7. Your turn: homework_done = True. If it is True, print `Movie time`. Else print `Finish homework first`. Next: nested choices.
