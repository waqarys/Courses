# Live Coding – Lesson 20 Nested if and match

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/23_*.py`.

## live_01 – The door

**Type this slowly, saying each part out loud:**

```python
has_key = True
has_weapon = True
has_enemy = True
if has_key:
    if has_weapon:
        if has_enemy:
            print("Fight to enter")
        else:
            print("Safe to enter")
    else:
        print("Need a weapon first")
else:
    print("Find the key")
```

**What to say:**
- Flip has_enemy to False and run.
- Flip has_key to False and run.

**Expected output** (Run ▶ / F5):
```
Fight to enter
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – match one word

**Type this slowly, saying each part out loud:**

```python
player_action = "JUMP"
match player_action:
    case "JUMP":
        print("Player jumped")
    case "RUN":
        print("Player is running")
    case _:
        print("Unknown action")
```

**What to say:**
- _ means anything else.
- Needs Python 3.10 or newer.

**Expected output** (Run ▶ / F5):
```
Player jumped
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 20 — Decisions inside decisions

Book 4.2.6 and 4.3. Length: 12 min. File: `nested.py`.

1. A nested `if` is a second question you ask only after the first answer was yes. Indent again.
2. SWITCH. Dungeon door.

```python
has_key = True
has_weapon = True
has_enemy = True

if has_key:
    if has_weapon:
        if has_enemy:
            print("Fight to enter")
        else:
            print("Safe to enter")
    else:
        print("Need a weapon first")
else:
    print("Find the key")
```

Change `has_enemy` to False, run again. Change `has_key` to False, run again. The inner lines never run if the outer test fails.
3. `match` / `case` is a cleaner list when you are matching one value. Needs Python 3.10 or newer. Thonny’s Python is new enough.

```python
player_action = "JUMP"

match player_action:
    case "JUMP":
        print("Player jumped")
    case "RUN":
        print("Player is running")
    case "ATTACK":
        print("Player attacked")
    case _:
        print("Unknown action")
```

`_` means anything else.
4. Say when to pick which: many ranges of one number → `if` / `elif`. One exact word, many arms → `match`. Deep “if this, then if that” is fine for two levels. Past that, `match` or a flatter `elif` is kinder.
5. Your turn: set `player_action` to `"RUN"` and run. Next: while.
