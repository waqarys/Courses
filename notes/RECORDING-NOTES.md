# Python for Kids — OBS recording pack

Teach in your own words. Do not put the textbook PDF on screen. Code below is what you type live in Thonny. Students on Chromebooks type the same lines into Google Colab (Shift+Enter). Say that once per lesson.

One video = one Canva deck, full screen, then your voice. Target 8–12 minutes.

## OBS, once, then never change it

Scenes

1. `Slides` — Window Capture of Chrome or the Canva desktop app, on the Present view only. Hide bookmarks.
2. `Code` — Window Capture of Thonny. Font 24 or bigger. Light theme.
3. `Code + cam` — same as Code, plus the round webcam mask at 360×360, bottom right.

Filters on the camera (already built): Crop/Pad to a square, then Image Mask/Blend with `circle-mask-soft-alpha.png`, type Alpha Mask (Alpha Channel).

Audio: one mic, headphones on, noise gate + limiter. Record MKV, 1920×1080, 30 fps.

Hotkeys you set in OBS Settings → Hotkeys

- F1 = switch to `Slides`
- F2 = switch to `Code`
- F3 = switch to `Code + cam`

How to record one lesson

1. Open that lesson’s Canva deck. Share → Present. Full screen. F1.
2. Hit record. Read the title. Do not restart for small slips.
3. Advance slides with the Right arrow. Speak the SAY line. Do not read every word on the slide.
4. When the notes say SWITCH, press F2 and type the code slowly. Run it. Then the deliberate mistake. Fix it.
5. F1 for the last slide: Your turn, and the name of the next video.
6. Stop. Export later from CapCut only if you need zooms and captions. You can also publish the OBS file as-is.

Thonny on your laptop (the thing students see you use)

- Windows and Mac: install Thonny from https://thonny.org — it includes Python.
- View → font 24. One file per lesson, named in the notes.
- Chromebook students do not install Thonny. They use Colab.

## Playlist (record in this order)

Record 01 first. A child who already has Thonny or Colab never watches A, B, or C. Those three sit at the end. You reorder the YouTube playlist yourself. Do not rename the video files.

| # | Video | Book |
|---|---|---|
| 01 | Hello, World | 1.4, 1.8, 1.9 |
| 02 | What is Python? | 1.1–1.3 |
| 03 | Variables are labeled boxes | 2.1.1–2.1.2 |
| 04 | Names that make sense | 2.1.3–2.1.8 |
| 05 | Strings and input | 2.2.1 |
| 06 | Numbers, and the input trap | 2.2.2 |
| 07 | Time as a number | 2.2.3 |
| 08 | True, False, and comparisons | 2.2.4–2.2.5 |
| 09 | Maths Python understands | 2.3 |
| 10 | Comments that help | 2.4 |
| 11 | Project: pancake calculator | 2.7 |
| 12 | Project: wellbeing check-in | 2.8 |
| 13 | Lists, not 30 variables | 3.1–3.1.7 |
| 14 | Add, remove, loop a list | 3.1.8–3.1.9 |
| 15 | Slices and grids | 3.1.10–3.1.11 |
| 16 | Dictionaries | 3.2 |
| 17 | Records, tuples, sets | 3.3–3.6 |
| 18 | One line after another | 4.1 |
| 19 | if, else, elif | 4.2–4.2.5 |
| 20 | Decisions inside decisions | 4.2.6, 4.3 |
| 21 | while: again until… | 4.4.1 |
| 22 | for: a known number of times | 4.4.2–4.4.4 |
| 23 | Capstone: Guess the Number | 4.5 |
| A | Only if Python will not open on Windows | setup |
| B | Only if Python will not open on a Mac | setup |
| C | Chromebook, no install | setup |

---

## 01 — Hello, World

Book 1.4, 1.8, 1.9. Length: 9 min. File: `hello_world.py`.

Slides

1. Title. First program. One line. If Python is not open, stop and use the last videos, then come back.
2. `print` sends words to the screen. The words sit inside quotes. The line starts with `#` if it is a note, not code.
3. Smoke test: like turning a car on, not driving it across the city. Does it start? Does it print exactly `Hello, World!`?
4. SWITCH. Type:

```python
# My first program
print("Hello, World!")
```

Run it. Point at the output, not the code.
5. Mistake: `Print("Hello, World!")` with a capital P. Python is case-sensitive. `Print` is not `print`. Fix it.
6. Second run, still in Thonny:

```python
print("Hello, World!")
print("I am learning Python.")
```

Say: each line finishes before the next one starts. That is sequence. We name it properly in video 18.
7. The wellbeing game is where this course ends up: a small check-in a student can run. We will not build it today. We need variables first.
8. Your turn: change the second print to your first name. Run it. Next: what Python is.

## 02 — What is Python?

Book 1.1–1.6. Length: 8 min. Slides only. No install talk.

1. Title. Python is a language you type so the computer can follow you.
2. Made by Guido van Rossum, released in 1991. We care about one thing: the lines are short and readable.
3. People use it for games, websites, science, and AI. You will use it for tiny games and calculators first.
4. Three words: IDE (the app you type in), environment (Python plus that app), code (the lines).
5. On this course, home laptops use Thonny. Chromebooks use Colab. Same language. Different window.
6. AI can suggest a line. You still run it. If it crashes, the AI was wrong. You are the tester.
7. Your turn: tell someone one place Python is used, in your own words. Next: labeled boxes.

## 03 — Variables are labeled boxes

Book 2.1.1–2.1.2. Length: 10 min. File: `variables.py`.

1. A variable is a name stuck on a box. The box holds a value. You can change what is in the box. That is why it is called variable.
2. One equals sign stores. It is not “equals” from maths. Read `score = 0` as “score gets 0”.
3. SWITCH. Type and run:

```python
player_name = "Jimmy"
player_score = 0
is_game_over = False
health = 100.0

print(player_name)
print(player_score)
print(is_game_over)
print(health)
```

4. Change `player_score = 0` to `player_score = 50`. Run again. The name stayed. The value changed.
5. A constant is a value you promise not to change. Python has no lock for that. We shout the name in capitals so humans leave it alone.

```python
PI = 3.14159
MAX_PLAYERS = 4
```

Say: Python will let you change `PI`. Do not.
6. Mistake: `player-score = 50`. The hyphen is minus, not a name. Use `player_score`.
7. Your turn: make `lives = 3`, print it, then set it to 2 and print again. Next: good names.

## 04 — Names that make sense

Book 2.1.3–2.1.8. Length: 10 min. File: `names.py`.

1. A name can be long. Letters, digits, underscore. It cannot start with a digit. No spaces. No hyphens.
2. SWITCH. Good, then show each bad line and do not leave it in the file:

```python
name = "Alex"
player_score = 100
level1 = 1
```

Bad, say them, do not run more than one: `1level`, `player-score`, `my name`.
3. Keywords are Python’s own words. You cannot steal them. `if`, `else`, `for`, `while`, `True`, `False`, `and`, `or`, `not`, `in`, `is`, `def`, `class`, `return`. So `if = 5` is illegal.
4. snake_case is the Python habit: `player_name`, `current_score`, `is_game_active`. `currentScore` is camelCase, used in other languages. `PlayerName` looks like a class. We do not use it for variables.
5. Start booleans with `is_` or `has_`. Start counters with `num_` or `count_`.

```python
is_alive = True
has_key = False
num_players = 4
count_lives = 3
```

6. Meaning: `score` beats `x`. `name` beats `n`. One letter is only fine for a tiny loop later.
7. Old style you might see and should not copy: `strName`, `intAge`. That is Hungarian notation. Skip it.
8. Quick quiz, answers after a pause: `int_user_number` is Hungarian. `CalculateArea` is PascalCase. `MAX_LIMIT` is a constant. `tempVal` is camelCase.
9. Your turn: rewrite `Eggs Count`, `sugarSpoons`, `Flour-Amount`, `IsVegetarian` as `eggs_count`, `sugar_spoons`, `flour_amount`, `is_vegetarian`. Next: text.

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

## 07 — Time as a number

Book 2.2.3. Length: 8 min. File: `time_stamp.py`. Keep it light.

1. A timestamp is a count of seconds since 1 January 1970, UTC. A giant stopwatch.
2. SWITCH.

```python
from time import time, ctime

current_time = time()
print(current_time)
print(ctime(current_time))
```

3. Years since 1970. There are about 31557600 seconds in a year (365.25 days).

```python
seconds_in_a_year = 365.25 * 24 * 60 * 60
years_since_1970 = current_time / seconds_in_a_year
print(years_since_1970)
```

4. Check: this year minus 1970 should be close to that number. A fraction is fine. It is not January 1st anymore.
5. Your turn: print how many seconds are in one day (`24 * 60 * 60`). Next: True and False.

## 08 — True, False, and comparisons

Book 2.2.4–2.2.5. Length: 12 min. File: `booleans.py`.

1. A Boolean is only `True` or `False`. Capital T and F. `true` is a crash.
2. Comparisons make Booleans: `==`, `!=`, `>`, `<`, `>=`, `<=`.
3. SWITCH.

```python
score = 85
is_high_score = score > 80
is_perfect = score == 100
is_failing = score < 40
print(is_high_score, is_perfect, is_failing)
```

True, False, False.
4. One `=` stores. Two `==` asks “same?”.

```python
name = "Alex"
is_admin = name == "Admin"
print(is_admin)
```

5. `and` needs both. `or` needs one. `not` flips.

```python
has_sword = True
has_shield = False
print(has_sword and has_shield)
print(has_sword or has_shield)
is_game_over = False
print(not is_game_over)
```

6. Truth table, say it slowly. AND is True only on True/True. OR is False only on False/False. NOT flips the one box.
7. Mistake: `if score = 80` comes later; today just show `score = 80` versus `score == 80` side by side on the slide, and type only the comparison.
8. Your turn: `lives = 3`, print whether `lives > 0`. Next: maths.

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

## 10 — Comments that help

Book 2.4. Length: 8 min. File: `comments.py`.

1. A comment is a note. Python skips it. `#` for one line. Triple quotes for a long note or a long string.
2. Three tests: relevant, not obvious, same style as the rest of the file.
3. SWITCH. Bad versus good, say which you would delete:

```python
# Starting score for a new player
score = 50

# Increase score for defeating an enemy
score = score + 1
```

Shorter: `score += 1`.
4. A stub marks work you have not done yet.

```python
# TODO: ask for the player's name
def player_login():
    pass
```

`pass` means “do nothing, but stay legal.”
5. Mistake to discuss, not a crash: `# This line uses a variable` above `score = 50`. That comment adds nothing. Delete it.
6. Your turn: put one useful comment above a score line. Next: pancakes.

## 11 — Project: pancake calculator

Book 2.7. Length: 12 min. File: `pancake_recipe.py`. This is the first project they can finish.

1. A recipe for 4 people. We scale it to 6. Constants shout. Variables whisper in snake_case.
2. SWITCH. Type the whole program. Run it.

```python
# Scales a 4-serve pancake recipe

STANDARD_SERVINGS = 4

flour_cups = 2.5
sugar_tablespoons = 3
eggs_count = 2
milk_liters = 0.5
is_vegetarian = True

desired_servings = 6
scaling_factor = desired_servings / STANDARD_SERVINGS

new_flour = flour_cups * scaling_factor
new_sugar = sugar_tablespoons * scaling_factor
new_eggs = eggs_count * scaling_factor
new_milk = milk_liters * scaling_factor

print("New recipe amounts")
print("Flour:", new_flour, "cups")
print("Sugar:", new_sugar, "tablespoons")
print("Eggs:", new_eggs)
print("Milk:", new_milk, "liters")
print("Vegetarian:", is_vegetarian)
```

3. Point at types: flour is float, eggs is int, `is_vegetarian` is bool, the word `"cups"` is a string. `new_flour` becomes float because of `/`.
4. Ask for servings instead of hard-coding 6.

```python
desired_servings = int(input("How many servings? "))
```

Replace the old line. Run with 8.
5. Survey add-on, short:

```python
pancakes_per_month = 12
price = 3.50
monthly_revenue = pancakes_per_month * price
print("Monthly revenue: $", monthly_revenue)
print("*" * 20)
```

6. Your turn: change the price, or add a topping string and print it. Next: a 5-question check-in.

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

## 13 — Lists, not 30 variables

Book 3.1–3.1.7. Length: 11 min. File: `lists.py`.

1. A list is a row of boxes in one variable. Index 0 is the first box. The last index is length minus 1.
2. In other languages an array is often one type and a fixed size. In Python, start with a list. It can grow. It can mix types. You do not import anything.
3. SWITCH.

```python
scores = [85, 92, 78, 95, 88]
print(len(scores))
print(scores[0])
print(scores[4])
scores[2] = 80
print(scores)
```

4. Say it: length 5, first 85, last 88, then the middle box changes from 78 to 80.
5. Mistake: `print(scores[5])`. There is no box 5. Boxes are 0, 1, 2, 3, 4. Read `IndexError` as “that locker number does not exist.”
6. Your turn: a list of 4 favourite foods. Print the first and the last. Next: change the list.

## 14 — Add, remove, loop a list

Book 3.1.8–3.1.9. Length: 12 min. File: `inventory.py`.

1. `append` adds at the end. `insert(place, item)` squeezes in. `remove(value)` drops the first match. `pop()` drops the last and hands it back. `len`, `max`, `min`.
2. SWITCH. Inventory, not the age example. Easier to say out loud.

```python
inventory = ["sword", "shield", "armor", "bow"]
inventory.append("health potion")
inventory.insert(1, "golden sword")
inventory.remove("shield")
dropped_item = inventory.pop()
print(inventory)
print("Dropped:", dropped_item)
print("Count:", len(inventory))
```

Walk the list after each line if you can. Append, then insert, then remove, then pop.
3. A `for` loop visits every item. We go deeper in video 22. Today, just visit.

```python
for item in inventory:
    print("You have a", item)
```

`range(4)` is 0, 1, 2, 3. Prefer `for item in inventory` when you do not need the index.
4. Your turn: start with three school items, append one, pop one, print what is left. Next: slices.

## 15 — Slices and grids

Book 3.1.10–3.1.11. Length: 10 min. File: `grids.py`.

1. Negative index: `-1` is the last box, `-2` the one before.
2. A slice is `start:stop:step`. Stop is not included.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[1:4])
print(numbers[1:5:2])
```

50, then `[20, 30, 40]`, then `[20, 40]`.
3. A grid is a list of lists. Row, then column. Both start at 0.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0][1])
matrix[1][1] = 10
print(matrix)
```

`[0][1]` is 2. Then the 5 becomes 10.
4. Add a row with `append`. Delete a row with `del matrix[0]`.
5. Your turn: print the 6. It is row 1, column 2: `matrix[1][2]` before you change anything. Next: dictionaries.

## 16 — Dictionaries

Book 3.2. Length: 10 min. File: `dictionary.py`.

1. A list uses positions. A dictionary uses labels. Curly braces. `"key": value`. Commas between pairs.
2. SWITCH.

```python
student = {
    "name": "Jimmy",
    "age": 15,
    "grade": "Year 10",
}
print(student["name"])
print(student["age"])
```

3. Add, change, delete.

```python
student["school"] = "Code High"
student["age"] = 16
del student["grade"]
print(student)
```

4. Keys are unique. Values can repeat. A missing key crashes: `student["hobby"]`. Say: ask with a key you know exists.
5. Your turn: a dictionary for one game character with `name`, `level`, and `health`. Print the name. Next: three smaller types.

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

## 18 — One line after another

Book 4.1. Length: 8 min. File: `sequence.py`.

1. Three flows in this course: sequence (straight), selection (a choice), iteration (again).
2. Sequence means line 1 finishes, then line 2, then line 3. Python is interpreted: it reads a line and does it, then the next line.
3. A flowchart: oval start/stop, rectangle for a step, slanted box for input/output, diamond for a choice, arrows for direction. Today there is no diamond.
4. SWITCH.

```python
player_name = input("Enter your name: ")
print("Welcome,", player_name)
score = 0
print("Score starts at", score)
```

5. Point at the order. If you print `score` before `score = 0`, it crashes. Do that mistake. Move the line back.
6. Your turn: three lines that ask a colour and print it back. Next: choices.

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
## A — Only if Python will not open on Windows

Length: 8 min. File later: none. Scene: Slides the whole time, then 60 seconds of Thonny at the end.

SAY, slide by slide

1. Title. “Only if Python will not open on a Windows laptop. If Thonny or Colab is already open, go back to Hello.”
2. You need a browser and ten quiet minutes. You will install two things: Python, and Thonny, the big-text editor we use on camera.
3. Go to https://www.python.org/downloads/. Click the yellow Download Python button. You want Python 3, not 2.
4. Run the installer. On the first screen, tick **Add python.exe to PATH**. Then **Install Now**. If Windows asks for permission, click Yes.
5. When it says Setup was successful, click **Disable path length limit** if you see it, then Close.
6. Click Start, type `cmd`, open Command Prompt. Type `python --version` and press Enter. You should see Python 3.something. If you see “not recognized”, the PATH tick was missed. Uninstall, run the installer again, tick the box.
7. Go to https://thonny.org. Download the Windows installer. Next, Next, Install. Open Thonny. Font is already large.
8. SWITCH to Code. In Thonny type `print("Hello from Windows")` and press the green Run. Save as `hello_windows.py` on the Desktop when it asks.
9. Your turn: install it, run that one line, screenshot the version and the Hello line.

Deliberate mistake, on camera: type `print("Hello from Windows)` with the closing quote missing. Read the red text in plain words: “Python reached the end of the line still inside the quote.” Add the quote. Run again.

## B — Only if Python will not open on a Mac

Length: 8 min. Slides, then Thonny.

1. Title. “Only if Python will not open on a Mac. If Thonny or Colab is already open, go back to Hello.”
2. Do not use the old Python that some Macs hide in the system. We install our own.
3. Easiest path: https://thonny.org → macOS download. Open the `.pkg`. Continue, Install. If macOS says it cannot be opened, right-click the installer → Open → Open.
4. Open Thonny from Applications. If Gatekeeper complains, System Settings → Privacy & Security → Open Anyway.
5. Check the language: in Thonny, Tools → Manage packages is optional. Bottom-right or the shell shows Python 3.
6. Terminal check, only if you want it: open Terminal, type `python3 --version`. Thonny does not need this to run.
7. SWITCH. Type `print("Hello from Mac")`. Green Run. Save as `hello_mac.py`.
8. Same missing-quote mistake as Windows. Fix it.
9. Your turn: Hello line runs. If the school Mac blocks installs, use the Chromebook setup at the end. It also works on a Mac. Otherwise go back to Hello.

## C — Chromebook, no install

Length: 10 min. This is the path students actually use. Record it in Chrome, not Thonny. Scene: Slides, then a browser window (name the scene `Browser`).

1. Title. “Only if you are on a Chromebook and Colab is not open yet. No install. A browser is enough. Everyone else, go back to Hello.”
2. School laptops often block Linux and app installs. We will not turn Linux on.
3. Open Chrome. Go to https://colab.research.google.com. Sign in. If the school Google account is blocked, try a family Gmail, or go to the fallback on the next slide.
4. File → New notebook. Click the empty cell. Type `print("Hello, Chromebook")`. Press Shift+Enter. The answer appears under the cell.
5. A cell is one page. The next cell can see variables only if you ran the earlier cell. File → Save a copy in Drive.
6. Numbers come out of `input()` as text. We meet that properly in video 06. Today, only Hello.
7. Fallback if Colab is blocked: https://trinket.io → Python. Or https://replit.com → Python repl → Run. Pick one and use it all term.
8. Your turn: Hello runs, notebook has a name, it is saved.

Do not teach Crostini unless a teacher has already turned Linux on for the class.


## After you stop recording

- Trim only the “umm” and the flooded infinite loop, in CapCut, if you want. The Canva slides are already the edit.
- Captions: CapCut auto-captions, then fix `print`, `elif`, `float`, `Thonny`, `Colab`.
- Title the upload exactly as the table. Example: `Python for Kids 01: Hello, World`. Put A, B, and C last in YouTube. Example: `Python for Kids A: Only if Python will not open on Windows`.
- Description: two sentences from the title slide, and the Your turn task. On video 01 only, add one line: Python not open yet? The last three videos are Windows, Mac, and Chromebook.
- Do not upload the textbook PDF.

## Code you must run before you trust a take

Every fenced program above. If a line errors, fix the notes, then record. The usual ones: indent, colon, `int` around `input`, index 0, `True` not `true`.
