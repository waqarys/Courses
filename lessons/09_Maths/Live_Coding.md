# Live Coding – Lesson 09 Maths

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/12_*.py`.

## live_01 – One expression

**Type this slowly, saying each part out loud:**

```python
result = 3 + 5 * (6 - 2) ** 2 / 4 - 1
print(result)
```

**What to say:**
- (6-2) is 4.
- 4**2 is 16.
- 5*16/4 is 20.0.
- 3+20-1 is 22.0.

**Expected output** (Run ▶ / F5):
```
22.0
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – Division surprise

**Type this slowly, saying each part out loud:**

```python
print(10 / 5)
print(10 // 5)
```

**What to say:**
- 2.0 and 2.

**Expected output** (Run ▶ / F5):
```
2.0
2
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – 7/3 as a mixed number

**Type this slowly, saying each part out loud:**

```python
whole = 7 // 3
left = 7 % 3
print(whole, "and", left, "/ 3")
```

**Expected output** (Run ▶ / F5):
```
2 and 1 / 3
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_04 – + and * on text

**Type this slowly, saying each part out loud:**

```python
print("Hello" + " " + "World")
print("*" * 10)
```

**Expected output** (Run ▶ / F5):
```
Hello World
**********
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_05 – Spot the mistake

**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.

```python
print("2" + 3)
```

**What to say:**
- Text plus a number is refused.
- Int("2") + 3 is 5.
- "2" + "3" is the text 23.

**Expected output** (Run ▶ / F5):
```
TypeError: can only concatenate str (not "int") to str
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 09 — Maths Python understands

Book 2.3. Length: 11 min. File: `maths.py`.

1. Operators: `+ - * / // % **`. Say each in words. `%` is the remainder. `**` is power.
2. BIMDAS: brackets, indices (`**`), multiply and divide left to right, add and subtract left to right.
3. SWITCH.

```python
result = 3 + 5 * (6 - 2) ** 2 / 4 - 1
print(result)
```

Walk it: `(6-2)` is 4. `4**2` is 16. `5*16/4` is 20.0. `3+20.0-1` is 22.0.
4. `print(10 / 5)` is `2.0`. `print(10 // 5)` is `2`.
5. Mixed numbers. 7 divided by 3 is 2 remainder 1.

```python
numerator = 7
denominator = 3
whole_number = numerator // denominator
remainder = numerator % denominator
print(whole_number, remainder, "/", denominator)
```

6. Strings use `+` to join and `*` to repeat. They are not maths.

```python
print("Hello" + " " + "World")
print("*" * 10)
```

Mistake: `print("2" + 3)`. Say: text plus a number is refused. `print(int("2") + 3)` is 5. `print("2" + "3")` is the text 23.
7. `round(2.5)` is 2, not 3. Python sends a .5 to the even number. Mention it. Do not dwell. For school-style “.5 goes up”, add 0.5 and then chop, only if someone asks: `int(2.5 + 0.5)`.
8. Your turn: header of 20 stars, your name, footer of 20 stars. Next: comments.
