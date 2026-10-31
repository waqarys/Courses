# Live Coding – Lesson 06 Numbers

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/09_*.py`.

## live_01 – Integer maths

**Type this slowly, saying each part out loud:**

```python
score = 10 + 5
health = 100 - 20
bonus = 2 * 5
viruses = 10 ** 3
players = 10 // 3
remainder = 10 % 3
print(score, health, bonus, viruses, players, remainder)
```

**What to say:**
- Answers: 15, 80, 10, 1000, 3, 1.

**Expected output** (Run ▶ / F5):
```
15 80 10 1000 3 1
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Float maths

**Type this slowly, saying each part out loud:**

```python
distance = 5.0 * 2.5
average = 10.0 / 3.0
power = 2.0 ** 3
print(distance, average, power)
```

**What to say:**
- 12.5, about 3.333, 8.0.
- Plain / always makes a float.

**Expected output** (Run ▶ / F5):
```
12.5 3.3333333333333335 8.0
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – Convert on purpose

**Type this slowly, saying each part out loud:**

```python
number = int("42")
decimal = float("42")
whole = int(60.55)
rounded = round(60.55)
print(number, decimal, whole, rounded)
```

**What to say:**
- Int(60.55) chops to 60.
- Round goes to 61.

**Expected output** (Run ▶ / F5):
```
42 42.0 60 61
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – The input trap

**Type this slowly, saying each part out loud:**

```python
age = input("Enter your age: ")
age = int(age)
print(age + 1)
```

**Expected output** (Run ▶ / F5):
```
Enter your age: ValueError: invalid literal for int() with base 10: 'Sam'
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_05 – Spot the mistake

**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.

```python
print(int("ten"))
```

**What to say:**
- The word ten is not a number.
- Type 10 instead.

**Expected output** (Run ▶ / F5):
```
(nothing printed)
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 06 — Numbers, and the input trap

Book 2.2.2. Length: 12 min. File: `numbers.py`.

1. `int` is a whole number: `3`, `0`, `-1`. `float` has a decimal: `7.5`, `3.0`.
2. SWITCH. Integers:

```python
player_score = 100
lives = 3
score = 10 + 5
health = 100 - 20
bonus = 2 * 5
viruses = 10 ** 3
players = 10 // 3
remainder = 10 % 3
print(score, health, bonus, viruses, players, remainder)
```

Say the answers before you reveal: 15, 80, 10, 1000, 3, 1.
3. Floats:

```python
distance = 5.0 * 2.5
average = 10.0 / 3.0
power = 2.0 ** 3
print(distance, average, power)
```

12.5, 3.333…, 8.0. Plain `/` always gives a float. `//` cuts off the decimal.
4. Convert on purpose.

```python
text_number = "42"
number = int(text_number)
decimal = float(text_number)
blood = 60.55
whole_number = int(blood)
rounded_number = round(blood)
print(number, decimal, whole_number, rounded_number)
```

`int(60.55)` chops to 60. It does not round. `round` goes to 61.
5. The trap:

```python
age = input("Enter your age: ")
print(type(age))
age = int(age)
print(type(age))
print(age + 1)
```

6. Mistake: `int("ten")`. Read the error: the word ten is not a number. Type `10` instead.
7. Your turn: ask for two whole numbers, add them, print the sum. Next: time.
