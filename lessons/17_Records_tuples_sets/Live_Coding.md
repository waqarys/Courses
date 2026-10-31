# Live Coding – Lesson 17 Records, tuples, sets

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/20_*.py`.

## live_01 – Character

**Type this slowly, saying each part out loud:**

```python
from dataclasses import dataclass

@dataclass
class Character:
    name: str
    level: int
    health: int

player1 = Character("Archer", 5, 100)
print(player1.name)
player1.health = 80
print(player1.health)
```

**Expected output** (Run ▶ / F5):
```
Archer
80
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – A tuple does not change

**Type this slowly, saying each part out loud:**

```python
position = (10, 20)
x, y = position
print(x, y)
```

**What to say:**
- One item needs a comma: (1,).
- Position[0] = 5 fails.
- That is the point.

**Expected output** (Run ▶ / F5):
```
10 20
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – A set keeps uniques

**Type this slowly, saying each part out loud:**

```python
found = {"key", "coin", "key"}
print(found)
found.add("map")
print("coin" in found)
```

**What to say:**
- One key, not two.
- Empty set is set().
- {} is a dictionary.

**Expected output** (Run ▶ / F5):
```
{'coin', 'key'}
True
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – Tasks

**Type this slowly, saying each part out loud:**

```python
tasks = [["wake up", 10], ["breakfast", 15], ["code", 45]]
total = 0
for task in tasks:
    print(task[0], task[1], "min")
    total = total + task[1]
print("Total", total)
```

**Expected output** (Run ▶ / F5):
```
wake up 10 min
breakfast 15 min
code 45 min
Total 70
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 17 — Records, tuples, sets

Book 3.3–3.6. Length: 12 min. File: `records.py`. Three ideas, one video. Do not rush the set.

1. A record is one person’s form. Fields can be different types. In Python a simple way is a dataclass.

```python
from dataclasses import dataclass

@dataclass
class Character:
    name: str
    level: int
    health: int

player1 = Character("Archer", 5, 100)
print(player1)
print(player1.name)
player1.health = 80
print(player1.health)
```

2. A tuple is a list you cannot edit. Parentheses. One item needs a comma: `(1,)`.

```python
position = (10, 20)
x, y = position
print(x, y)
```

Good for a fixed pair. Trying `position[0] = 5` fails. Show that crash and say “that is the point.”
3. A set keeps unique items. No order you can trust. Empty set is `set()`, not `{}` (`{}` is a dictionary).

```python
found = {"key", "coin", "key"}
print(found)
found.add("map")
print("coin" in found)
```

The printed set shows one `"key"`, not two.
4. Daily tasks idea, in our own words: a list of `[task, minutes]` pairs. Loop, add the minutes.

```python
tasks = [
    ["wake up", 10],
    ["breakfast", 15],
    ["code", 45],
]
total = 0
for task in tasks:
    print(task[0], task[1], "min")
    total = total + task[1]
print("Total:", total)
```

5. Your turn: add one task and run it again. Next: sequence.
