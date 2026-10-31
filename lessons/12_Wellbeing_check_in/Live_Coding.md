# Live Coding – Lesson 12 Wellbeing check-in

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/15_*.py`.

## live_01 – The program

**Type this slowly, saying each part out loud:**

```python
print("Rate each one from 1 to 5.")
name = input("What is your name? ")
age = input("How old are you? ")
feel_positive = int(input("1 Felt positive? "))
did_exercise = int(input("2 Moved your body? "))
ate_well = int(input("3 Ate a proper meal? "))
drank_water = int(input("4 Drank water? "))
slept_well = int(input("5 Slept well? "))
score = (feel_positive + did_exercise + ate_well + drank_water + slept_well) / 5
print(name + " score:", round(score, 1), "/ 5")
```

**Expected output** (Run ▶ / F5):
```
Rate each one from 1 to 5.
What is your name? How old are you? 1 Felt positive? 2 Moved your body? ValueError: invalid literal for int() with base 10: 'yes'
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 12 — Project: wellbeing check-in

Book 2.8. Length: 12 min. File: `wellbeing.py`.

This is a school-style habit check-in, not a medical test. Say that on the title slide. Do not give health advice. Scores are just arithmetic.

1. Five questions, each 1 to 5. Average them. Print a small report.
2. SWITCH.

```python
print("Daily check-in. Rate each one from 1 to 5.")

name = input("What is your name? ")
age = input("How old are you? ")

feel_positive = int(input("1. Felt positive? "))
did_exercise = int(input("2. Moved your body? "))
ate_well = int(input("3. Ate a proper meal? "))
drank_water = int(input("4. Drank water? "))
slept_well = int(input("5. Slept well? "))

total = feel_positive + did_exercise + ate_well + drank_water + slept_well
score = total / 5

print()
print(name + "'s check-in (age " + age + ")")
print("Score:", round(score, 1), "/ 5")
```

3. Talk usability: the prompt says 1 to 5, so the user is not guessing. Later we can reject a 9. Not today.
4. Stars, optional, if time:

```python
print("Feel positive:", "*" * feel_positive)
```

5. Mistake: forget `int(...)` around one input, then add them. Show the crash: you cannot add text. Wrap `int`.
6. Your turn: add a sentence. If `score >= 4`, print `Strong day`. Else print `Be kind to yourself today`. If `if` is new, peek at video 19, or leave it for later. Next: lists.
