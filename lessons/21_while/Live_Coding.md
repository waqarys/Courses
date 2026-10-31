# Live Coding – Lesson 21 while

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/24_*.py`.

## live_01 – Countdown

**Type this slowly, saying each part out loud:**

```python
resources = 5
while resources > 0:
    print("Working...", resources)
    resources = resources - 1
print("Done")
```

**Expected output** (Run ▶ / F5):
```
Working... 5
Working... 4
Working... 3
Working... 2
Working... 1
Done
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – break leaves now

**Type this slowly, saying each part out loud:**

```python
calculation = 0
while calculation < 10:
    calculation = calculation + 1
    if calculation == 4:
        print("Stopped early")
        break
print("After the loop", calculation)
```

**Expected output** (Run ▶ / F5):
```
Stopped early
After the loop 4
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – No do-while in Python

**Type this slowly, saying each part out loud:**

```python
while True:
    word = input("Type STOP to finish: ")
    if word == "STOP":
        break
    print("You typed", word)
```

**What to say:**
- The body runs, then you decide.
- Continue skips to the next lap.

**Expected output** (Run ▶ / F5):
```
Type STOP to finish: You typed Sam
Type STOP to finish: You typed 12
Type STOP to finish: You typed 5
Type STOP to finish: You typed yes
Type STOP to finish: You typed 7
Type STOP to finish: You typed 3
Type STOP to finish: You typed 50
Type STOP to finish: EOFError: EOF when reading a line
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – Spot the mistake

**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.

```python
n = 3
while n > 0:
    print(n)
```

**What to say:**
- N never shrinks.
- Press Stop.
- Then add n = n - 1.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_05 – A game number

**Type this slowly, saying each part out loud:**

```python
from random import randint
player_health = 100
while player_health > 0:
    damage = randint(10, 20)
    player_health = player_health - damage
    print("Health:", player_health)
print("Game over")
```

**What to say:**
- Randint(10, 20) includes 10 and 20.
- This is a game counter, not health advice.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 21 — while: again until…

Book 4.4.1. Length: 12 min. File: `while_loop.py`.

1. `while` repeats the indented block as long as the condition is True. The test happens before each lap. Something inside must change, or it never ends.
2. SWITCH. A countdown that cannot spin forever.

```python
resources = 5
while resources > 0:
    print("Working...", resources)
    resources = resources - 1
print("Done")
```

3. `break` leaves the loop now.

```python
resources = 10
calculation = 0
while resources > 0:
    calculation = calculation + 1
    resources = resources - 1
    if calculation == 4:
        print("Stopped early")
        break
print("After the loop", calculation)
```

4. A door you must get right at least once looks like `while True` plus `break`. Python has no do-while. This is the substitute. `continue` skips to the next lap.

```python
while True:
    word = input("Type STOP to finish: ")
    if word == "STOP":
        break
    print("You typed", word)
```

5. Mistake, carefully: start `n = 3` and `while n > 0: print(n)` and forget `n = n - 1`. It will flood the screen. Click the Thonny stop button (red). Then add the line that shrinks `n`. Say: “If the screen runs away, press Stop. Then find the line that never changes.”
6. Health version, short, no medical talk. It is a game number.

```python
from random import randint

player_health = 100
while player_health > 0:
    damage = randint(10, 20)
    player_health = player_health - damage
    print("Health:", player_health)
print("Game over")
```

`randint(10, 20)` is a random whole number from 10 to 20, including both ends.
7. Your turn: print 3, 2, 1, Go with a while loop. Next: for.
