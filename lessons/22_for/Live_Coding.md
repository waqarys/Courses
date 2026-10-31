# Live Coding – Lesson 22 for

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/25_*.py`.

## live_01 – range

**Type this slowly, saying each part out loud:**

```python
for i in range(5):
    print("Lap", i)
print("Done")
```

**What to say:**
- 0 1 2 3 4.
- Not 5.

**Expected output** (Run ▶ / F5):
```
Lap 0
Lap 1
Lap 2
Lap 3
Lap 4
Done
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – A list

**Type this slowly, saying each part out loud:**

```python
items = ["map", "rope", "torch"]
for item in items:
    print("Pack", item)
```

**Expected output** (Run ▶ / F5):
```
Pack map
Pack rope
Pack torch
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – Index and value

**Type this slowly, saying each part out loud:**

```python
for i, item in enumerate(items, start=1):
    print(i, item)
```

**Expected output** (Run ▶ / F5):
```
1 map
2 rope
3 torch
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – continue and break

**Type this slowly, saying each part out loud:**

```python
challenges = ["goblin", "trap", "prisoner", "dragon"]
for challenge in challenges:
    if challenge == "trap":
        print("Skip the trap")
        continue
    if challenge == "prisoner":
        print("Rescued")
        break
    print("Battled a", challenge)
```

**Expected output** (Run ▶ / F5):
```
Battled a goblin
Skip the trap
Rescued
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_05 – Countdown you can count

**Type this slowly, saying each part out loud:**

```python
for n in range(10, 0, -1):
    print(n)
print("Go")
```

**What to say:**
- No do-while.
- No repeat-until.
- "again while not finished" is while not finished.

**Expected output** (Run ▶ / F5):
```
10
9
8
7
6
5
4
3
2
1
Go
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 22 — for: a known number of times

Book 4.4.2–4.4.4. Length: 12 min. File: `for_loop.py`.

1. Use `for` when you know the collection, or you know how many laps. Use `while` when you are waiting for something to become true.
2. `range(5)` is 0, 1, 2, 3, 4. Not 5.

```python
for i in range(5):
    print("Lap", i)
print("Done")
```

3. Over a list:

```python
items = ["map", "rope", "torch"]
for item in items:
    print("Pack", item)
```

4. Index and value together:

```python
for i, item in enumerate(items):
    print(i, item)
```

`enumerate` starts at 0. Add 1 if you want “1. map” on screen.
5. Step: `range(0, len(items), 2)` visits even indexes only.
6. `continue` skips one item. `break` stops the whole loop.

```python
challenges = ["goblin", "trap", "prisoner", "dragon"]
for challenge in challenges:
    if challenge == "trap":
        print("Skip the trap")
        continue
    if challenge == "prisoner":
        print("Rescued")
        break
    print("Battled a", challenge)
```

7. Python has no do-while and no repeat-until. Repeat-until means “go again while the end test is still false.” We write that as `while not finished`.
8. Countdown with `for`, because we know the laps: `for n in range(10, 0, -1): print(n)`. Then `print("Go")`.
9. Your turn: a list of three tasks, printed as `1. wake up` using `enumerate`. Next: the game.
