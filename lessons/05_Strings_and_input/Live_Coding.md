# Live Coding – Lesson 05 Strings and input

You record ONLY these parts. OBS scene **Teach** (Thonny + webcam circle) or **Teach – IntelliJ** (see OBS_Setup.md). Font 24+, light theme. One recording per step. Save as `live/live_01.mp4`, `live/live_02.mp4` … (any resolution / fps; MKV is fine too – remux or rename not needed). Slips are OK: trim with `live/trim.json`.

Full lesson program for reference: `code/08_*.py`.

## live_01 – Type and print

**Type this slowly, saying each part out loud:**

```python
name = "Alex"
empty_string = ""
print(name)
print("Jimmy's car")
```

**Expected output** (Run ▶ / F5):
```
Alex
Jimmy's car
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_02 – input is always text

**Type this slowly, saying each part out loud:**

```python
name = input("What is your name? ")
print("Hello,", name)
age = input("How old are you? ")
print(type(age))
```

**What to say:**
- You will see class str.
- Age 15 is still text.

**Expected output** (Run ▶ / F5):
```
What is your name? Hello, Sam
How old are you? <class 'str'>
```

**Kid tip to say:** "Pause the video and type it with me!"

## live_03 – Spot the mistake

**This one is the deliberate mistake.** Type it, run it, read the red error out loud, then fix it.

```python
print("Hello, " name)
```

**What to say:**
- Missing comma.
- Print("Hello,", name).

**Expected output** (Run ▶ / F5):
```
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

**Kid tip to say:** "Pause the video and type it with me!"

---

## Your original recording notes (unchanged, for reference)

## 05 — Strings and input

Book 2.2.1. Length: 11 min. File: `strings_input.py`.

1. A string is text. One letter, many letters, or empty `""`.
2. Quotes: `'Alex'` and `"Alex"` are the same. Use double quotes when the text has an apostrophe: `"Jimmy's car"`.
3. SWITCH.

```python
name1 = "Alex"
name2 = "Alex"
empty_string = ""
print(name1)
print(empty_string)
```

4. `input` always hands you text, even if the person types 15.

```python
name = input("What is your name? ")
print("Hello,", name)
age = input("How old are you? ")
print(type(age))
```

Click into the shell and type a name, then an age. Point at `<class 'str'>`. “str means string. The age is still text. We cannot do maths with it yet.”
5. IPO: the `input` line is Input. `type(age)` is a tiny Process. `print` is Output.
6. Optional 60 seconds, not the point of the lesson: computers store letters as numbers. `print(ord("A"))` shows 65. That is ASCII. Python can also store other languages because it uses Unicode. Show one emoji with a normal character, not a long escape code: `print("Hello " + name)`.
7. Mistake: `print("Hello, " name)` without a comma. Add the comma.
8. Your turn: ask for a favourite game and print `I like` plus their answer. Next: numbers.
