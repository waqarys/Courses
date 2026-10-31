# Live Coding – Lesson 23 Guess the Number

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/26_*.py`.

## live_01 – Piece 1

**Type this slowly, saying each part out loud:**

```python
import random
ATTEMPT_LIMIT = 7
answer = random.randint(1, 100)
attempt = 0
won = False
print("Welcome to Guess the Number")
```

**What to say:**
- Randint includes 1 and 100.
- Do not print answer in the real game.

**Expected output** (Run ▶ / F5):
```
Welcome to Guess the Number
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Piece 2, the loop

**Type this slowly, saying each part out loud:**

```python
while attempt < ATTEMPT_LIMIT and not won:
    print("Attempt", attempt + 1, "of", ATTEMPT_LIMIT)
    text = input("Your guess (1-100): ")
```

**Expected output** (Run ▶ / F5):
```
Attempt 1 of 7
Your guess (1-100): Attempt 1 of 7
Your guess (1-100): Attempt 1 of 7
Your guess (1-100): Attempt 1 of 7
Your guess (1-100): Attempt 1 of 7
Your guess (1-100): Attempt 1 of 7
Your guess (1-100): Attempt 1 of 7
Your guess (1-100): Attempt 1 of 7
Your guess (1-100): EOFError: EOF when reading a line
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – Piece 3, reject junk

**Type this slowly, saying each part out loud:**

```python
    if not text.isnumeric():
        print("Type a whole number.")
        continue
    guess = int(text)
    if guess < 1 or guess > 100:
        print("Stay between 1 and 100.")
        continue
    attempt = attempt + 1
```

**What to say:**
- A bad input does not burn a try.
- Continue goes to the next lap.

**Expected output** (Run ▶ / F5):
```
Welcome to Guess the Number
Attempt 1 of 7
Your guess (1-100): Type a whole number.
Attempt 1 of 7
Your guess (1-100): Attempt 2 of 7
Your guess (1-100): Attempt 3 of 7
Your guess (1-100): Type a whole number.
Attempt 3 of 7
Your guess (1-100): Attempt 4 of 7
Your guess (1-100): Attempt 5 of 7
Your guess (1-100): Attempt 6 of 7
Your guess (1-100): EOFError: EOF when reading a line
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – Piece 4, the hint

**Type this slowly, saying each part out loud:**

```python
    if guess == answer:
        won = True
        print("You got it in", attempt, "tries.")
    elif guess < answer:
        print("Too low")
    else:
        print("Too high")
if not won:
    print("Out of tries. It was", answer)
```

**Expected output** (Run ▶ / F5):
```
Welcome to Guess the Number
Attempt 1 of 7
Your guess (1-100): Type a whole number.
Attempt 1 of 7
Your guess (1-100): Too low
Attempt 2 of 7
Your guess (1-100): Too low
Attempt 3 of 7
Your guess (1-100): Type a whole number.
Attempt 3 of 7
Your guess (1-100): Too low
Attempt 4 of 7
Your guess (1-100): Too low
Attempt 5 of 7
Your guess (1-100): Too low
Attempt 6 of 7
Your guess (1-100): EOFError: EOF when reading a line
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_05 – Switch

**Type this slowly, saying each part out loud:**

```python
print("Hello from Windows")
```

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_06 – First line

**Type this slowly, saying each part out loud:**

```python
print("Hello from Mac")
```

**Expected output** (Run ▶ / F5):
```
Welcome to Guess the Number
Attempt 1 of 7
Your guess (1-100): Type a whole number.
Attempt 1 of 7
Your guess (1-100): Too low
Attempt 2 of 7
Your guess (1-100): Too low
Attempt 3 of 7
Your guess (1-100): Type a whole number.
Attempt 3 of 7
Your guess (1-100): Too low
Attempt 4 of 7
Your guess (1-100): Too low
Attempt 5 of 7
Your guess (1-100): Too low
Attempt 6 of 7
Your guess (1-100): EOFError: EOF when reading a line
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_07 – Run a cell

**Type this slowly, saying each part out loud:**

```python
print("Hello, Chromebook")
```

**What to say:**
- Shift+Enter.
- The answer sits under the cell.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 23 — Capstone: Guess the Number

Book 4.5. Length: 15 min. File: `guess_the_number.py`. This is the episode people remember. Type it in pieces. Run after each piece.

1. Title. A secret number from 1 to 100. Seven tries. Too high, too low, or not a number.
2. Piece 1, welcome and secret.

```python
import random

ATTEMPT_LIMIT = 7
print("Welcome to Guess the Number")
answer = random.randint(1, 100)
attempt = 0
```

`randint(1, 100)` includes 1 and 100. Do not print `answer` in the finished game. You may print it once while testing, then delete that print.
3. Piece 2, the loop and a raw guess.

```python
while attempt < ATTEMPT_LIMIT:
    print("Attempt", attempt + 1, "of", ATTEMPT_LIMIT)
    guess = input("Your guess (1-100): ")
    attempt = attempt + 1
```

4. Piece 3, reject junk before the compare. `continue` does not count as a clever guess… actually decide on camera: invalid input should not burn an attempt. So move `attempt = attempt + 1` to after the checks.

```python
while attempt < ATTEMPT_LIMIT:
    print("Attempt", attempt + 1, "of", ATTEMPT_LIMIT)
    guess = input("Your guess (1-100): ")

    if not guess.isnumeric():
        print("Type a whole number.")
        continue

    guess = int(guess)
    if guess < 1 or guess > 100:
        print("Stay between 1 and 100.")
        continue

    attempt = attempt + 1

    if guess == answer:
        print("You got it:", answer)
        break
    elif guess < answer:
        print("Too low")
    else:
        print("Too high")

if guess != answer:
    print("Out of tries. It was", answer)
```

The last `if` can crash if the player never made a valid guess. For the recording, play it properly once so `guess` exists. Mention the rough edge in one sentence. Do not vanish into a fix unless you have time: set `won = False` and flip it on a correct guess. Cleaner version if you re-record:

```python
import random

ATTEMPT_LIMIT = 7
answer = random.randint(1, 100)
attempt = 0
won = False

print("Welcome to Guess the Number")

while attempt < ATTEMPT_LIMIT and not won:
    print("Attempt", attempt + 1, "of", ATTEMPT_LIMIT)
    text = input("Your guess (1-100): ")

    if not text.isnumeric():
        print("Type a whole number.")
        continue

    guess = int(text)
    if guess < 1 or guess > 100:
        print("Stay between 1 and 100.")
        continue

    attempt = attempt + 1

    if guess == answer:
        won = True
        print("You got it in", attempt, "tries.")
    elif guess < answer:
        print("Too low")
    else:
        print("Too high")

if not won:
    print("Out of tries. It was", answer)
```

Use this cleaner version on camera. It is the one to publish.
5. Play it once, fast, with a real guess. Then show one bad input: `ten`.
6. Chromebook: paste the same file into one Colab cell and run it. Input boxes appear under the cell.
7. Your turn: change the limit to 5, or the range to 1–20. Next: you have the whole toolbox. Build a bigger check-in or a bigger game if you want. The course stops here.
