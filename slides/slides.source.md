# 00 | Teacher: how to record | 00
## Open this deck in Chrome
@ OBS setup
- File, Open, slides.html
- Press F for fullscreen
- OBS scene: window capture this Chrome window
- Name that scene Slides

## Keys while you talk
@ Do not click around
- Right arrow: next slide
- Left arrow: previous slide
- L: lesson list
- Esc: close the list

## Two OBS scenes
@ Set hotkeys once
- F1: Slides, this deck
- F2: Thonny, or Chrome on Colab
- Mic on. Headphones on.
- Record 1920x1080, 30 fps

## When you see Switch
@ Cut, do not keep talking to a code slide
- Press F2
- Type the program slowly
- Run it
- Then do the mistake on the next slide
- Press F1 to come back

## One video, one lesson
@ Then stop
- Open with L and pick the lesson
- Talk 8 to 12 minutes
- End on Your turn
- Do not show the textbook PDF
- Kids start at 01. Setup is A, B, and C

# 01 | Hello, World | 05
## Hello, World
@ Lesson 01 · start here
- Python is not open? Stop. Use the last videos, then come back.
- One line
- print sends words to the screen
- Quotes hold the words

## A note is not code
```
# My first program
print("Hello, World!")
```
- # means Python skips that line

## Smoke test
- Like starting a car
- Not driving across the city
- Does it run?
- Does it say Hello, World!

## Capitals matter
@ The mistake
```
Print("Hello, World!")
```
- Print is not print
- Fix the P
- Run again

## Two lines, in order
```
print("Hello, World!")
print("I am learning Python.")
```
- Line 1 finishes
- Then line 2
- That is sequence

## Your turn
- Change line 2 to your first name
- Run it
- Next: what Python is

# 02 | What is Python? | 04
## What is Python?
@ Lesson 02
- A language you type
- The computer follows the lines
- Short lines, on purpose

## A little history, then we move
- Guido van Rossum
- Released in 1991
- We care that a beginner can read it

## People use it for
- Games
- Websites
- Science
- AI
- You start with calculators and tiny games

## Three words
- IDE: the app you type in
- Environment: Python plus that app
- Code: the lines

## Two windows
- Home laptop: Thonny
- Chromebook: Colab
- Same language

## AI can hint
- A hint is not tested
- You run the line
- A crash means the hint was wrong
- You are the tester

## Your turn
- Tell someone one place Python is used
- Your own words
- Next: labeled boxes

# 03 | Variables | 06
## Variables are labeled boxes
@ Lesson 03
- A name stuck on a box
- The box holds a value
- You can change what is inside

## One equals sign stores
- Read score = 0 as
- score gets 0
- It is not maths equals
- Two equals signs come later

## Four boxes
@ Switch to Thonny or Colab
```
player_name = "Jimmy"
player_score = 0
is_game_over = False
health = 100.0
print(player_name, player_score, is_game_over, health)
```

## Change the score
```
player_score = 50
print(player_score)
```
- The name stayed
- The value changed

## Constants shout
```
PI = 3.14159
MAX_PLAYERS = 4
```
- Python will not lock them
- Capitals tell humans: leave this alone

## The mistake
```
player-score = 50
```
- A hyphen means minus
- Use player_score

## Your turn
- lives = 3
- Print it
- Set it to 2 and print again
- Next: good names

# 04 | Good names | 07
## Names that make sense
@ Lesson 04
- Letters, digits, underscore
- Cannot start with a digit
- No spaces
- No hyphens

## Legal and illegal
```
name = "Alex"
player_score = 100
level1 = 1
```
- Illegal: 1level
- Illegal: my name
- Illegal: player-score

## Do not steal keywords
- if, else, for, while
- True, False
- and, or, not
- def, class, return
- if = 5 is illegal

## snake_case
```
player_name = "Alex"
current_score = 100
is_game_active = True
```
- currentScore is camelCase
- Other languages use that
- Python variables do not

## Prefixes that help
```
is_alive = True
has_key = False
num_players = 4
count_lives = 3
```

## Meaning beats a single letter
- score beats x
- name beats n
- One letter is only for a tiny loop later

## Name these
- int_user_number is Hungarian. Skip it.
- CalculateArea is PascalCase. Classes, not variables.
- MAX_LIMIT is a constant.
- tempVal is camelCase.

## Your turn
- Eggs Count becomes eggs_count
- sugarSpoons becomes sugar_spoons
- Flour-Amount becomes flour_amount
- IsVegetarian becomes is_vegetarian

# 05 | Strings and input | 08
## Text is a string
@ Lesson 05
- One letter, many letters, or empty
- Quotes: "Alex" or 'Alex'
- An apostrophe needs double quotes

## Type and print
@ Switch
```
name = "Alex"
empty_string = ""
print(name)
print("Jimmy's car")
```

## input is always text
```
name = input("What is your name? ")
print("Hello,", name)
age = input("How old are you? ")
print(type(age))
```
- You will see class str
- Age 15 is still text

## Input, process, output
- input line: Input
- type(age): a tiny Process
- print: Output

## The mistake
```
print("Hello, " name)
```
- Missing comma
- print("Hello,", name)

## Your turn
- Ask for a favourite game
- Print I like, then their answer
- Next: numbers

# 06 | Numbers | 09
## int and float
@ Lesson 06
- int: whole numbers. 3, 0, -1
- float: a decimal. 7.5
- 3.0 is a float

## Integer maths
@ Switch
```
score = 10 + 5
health = 100 - 20
bonus = 2 * 5
viruses = 10 ** 3
players = 10 // 3
remainder = 10 % 3
print(score, health, bonus, viruses, players, remainder)
```
- Answers: 15, 80, 10, 1000, 3, 1

## Float maths
```
distance = 5.0 * 2.5
average = 10.0 / 3.0
power = 2.0 ** 3
print(distance, average, power)
```
- 12.5, about 3.333, 8.0
- Plain / always makes a float

## Convert on purpose
```
number = int("42")
decimal = float("42")
whole = int(60.55)
rounded = round(60.55)
print(number, decimal, whole, rounded)
```
- int(60.55) chops to 60
- round goes to 61

## The input trap
```
age = input("Enter your age: ")
age = int(age)
print(age + 1)
```

## The mistake
```
print(int("ten"))
```
- The word ten is not a number
- Type 10 instead

## Your turn
- Ask for two whole numbers
- Add them
- Print the sum
- Next: time

# 07 | Time as a number | 10
## A giant stopwatch
@ Lesson 07
- A timestamp counts seconds
- Start line: 1 January 1970, UTC
- ctime turns that into words

## Now
@ Switch
```
from time import time, ctime
current_time = time()
print(current_time)
print(ctime(current_time))
```

## Years since 1970
```
seconds_in_a_year = 365.25 * 24 * 60 * 60
years = current_time / seconds_in_a_year
print(years)
```
- 365.25 covers leap years
- This year minus 1970 should be close

## Your turn
- How many seconds in one day?
- 24 * 60 * 60
- Print it
- Next: True and False

# 08 | True and False | 11
## Only two values
@ Lesson 08
- True
- False
- Capital T and F
- true in lowercase crashes

## Comparisons
- == same
- != not the same
- > < >= <=
- They produce True or False

## Try a score
@ Switch
```
score = 85
print(score > 80)
print(score == 100)
print(score < 40)
```
- True, False, False

## = stores. == asks.
```
name = "Alex"
is_admin = name == "Admin"
print(is_admin)
```

## and, or, not
```
has_sword = True
has_shield = False
print(has_sword and has_shield)
print(has_sword or has_shield)
print(not False)
```
- and: both
- or: at least one
- not: flip

## Truth tables, slow
- AND is True only for True and True
- OR is False only for False and False
- NOT flips the single box

## Your turn
```
lives = 3
print(lives > 0)
```
- Next: maths

# 09 | Maths | 12
## The signs
@ Lesson 09
- + - * /
- // integer division
- % remainder
- ** power

## BIMDAS
- Brackets first
- Then **
- Then * and /, left to right
- Then + and -, left to right

## One expression
@ Switch
```
result = 3 + 5 * (6 - 2) ** 2 / 4 - 1
print(result)
```
- (6-2) is 4
- 4**2 is 16
- 5*16/4 is 20.0
- 3+20-1 is 22.0

## Division surprise
```
print(10 / 5)
print(10 // 5)
```
- 2.0 and 2

## 7/3 as a mixed number
```
whole = 7 // 3
left = 7 % 3
print(whole, "and", left, "/ 3")
```

## + and * on text
```
print("Hello" + " " + "World")
print("*" * 10)
```

## The mistake
```
print("2" + 3)
```
- Text plus a number is refused
- int("2") + 3 is 5
- "2" + "3" is the text 23

## Your turn
- 20 stars
- Your name
- 20 stars
- Next: comments

# 10 | Comments | 13
## Notes Python skips
@ Lesson 10
- # one line
- A comment must earn its place
- Relevant
- Not obvious
- Same style every time

## Keep this
@ Switch
```
# Starting score for a new player
score = 50
# Increase score for defeating an enemy
score = score + 1
```
- Shorter: score += 1

## A stub
```
# TODO: ask for the player's name
def player_login():
    pass
```
- pass means: legal, but nothing yet

## Delete this kind
- # This line uses a variable
- It tells you nothing
- The code already says score = 50

## Your turn
- One useful comment
- Above a score line
- Next: pancakes

# 11 | Pancake calculator | 14
## Scale a recipe
@ Lesson 11 · first project
- Recipe serves 4
- Cook asks for 6
- Constants shout
- Variables use snake_case

## The program
@ Switch. Type it, then run.
```
STANDARD_SERVINGS = 4
flour_cups = 2.5
sugar_tablespoons = 3
eggs_count = 2
milk_liters = 0.5
is_vegetarian = True
desired_servings = 6
scaling_factor = desired_servings / STANDARD_SERVINGS
print("Flour", flour_cups * scaling_factor)
print("Sugar", sugar_tablespoons * scaling_factor)
print("Eggs", eggs_count * scaling_factor)
print("Milk", milk_liters * scaling_factor)
```

## Name the types
- flour_cups is float
- eggs_count is int
- is_vegetarian is True or False
- "Flour" is a string

## Ask, do not hard-code
```
desired_servings = int(input("How many servings? "))
```
- Replace the old 6
- Run it with 8

## Your turn
- Add a topping string
- Print it under the recipe
- Next: a 5-question check-in

# 12 | Wellbeing check-in | 15
## A habit check-in
@ Lesson 12
- Not a medical test
- Five scores, 1 to 5
- Add them
- Divide by 5

## The program
@ Switch
```
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

## Make the question clear
- The prompt says 1 to 5
- The user should not guess the scale
- We reject a 9 in a later lesson

## The mistake
- Forget int() on one answer
- Then you add text to a number
- Python refuses
- Wrap int() and run again

## Your turn
- If score is 4 or more, print Strong day
- Else print Be kind to yourself today
- if is lesson 22 if you want to wait
- Next: lists

# 13 | Lists | 16
## One variable, many boxes
@ Lesson 13
- A row of lockers
- First locker is index 0
- Last index is length minus 1

## Lists, not arrays, to start
- A list can grow
- A list can mix types
- No import
- Arrays in other languages are stricter

## Scores
@ Switch
```
scores = [85, 92, 78, 95, 88]
print(len(scores))
print(scores[0])
print(scores[4])
scores[2] = 80
print(scores)
```
- Length 5
- First 85
- Last 88
- Middle becomes 80

## The mistake
```
print(scores[5])
```
- There is no locker 5
- Lockers: 0 1 2 3 4
- IndexError means that number does not exist

## Your turn
- Four favourite foods
- Print the first
- Print the last
- Next: change the list

# 14 | List methods and for | 17
## Four moves
@ Lesson 14
- append: add at the end
- insert(place, item)
- remove(value): first match
- pop(): take the last one off

## Inventory
@ Switch. Read the list after each move.
```
inventory = ["sword", "shield", "armor", "bow"]
inventory.append("health potion")
inventory.insert(1, "golden sword")
inventory.remove("shield")
dropped = inventory.pop()
print(inventory)
print("Dropped", dropped)
print("Count", len(inventory))
```

## Visit every item
```
for item in inventory:
    print("You have a", item)
```
- for is "for each"
- We go deeper in lesson 25

## Your turn
- Three school items
- append one
- pop one
- Print what is left
- Next: slices and grids

# 15 | Slices and grids | 18
## Negative index
@ Lesson 15
- -1 is the last box
- -2 is the one before that

## Slice
@ Switch
```
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[1:4])
print(numbers[1:5:2])
```
- 50
- 20, 30, 40
- 20, 40
- Stop is not included

## A grid is a list of lists
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0][1])
matrix[1][1] = 10
print(matrix)
```
- Row, then column
- Both start at 0
- [0][1] is 2

## Your turn
- Print the 6
- It is row 1, column 2
- matrix[1][2]
- Next: dictionaries

# 16 | Dictionaries | 19
## Labels, not positions
@ Lesson 16
- Curly braces
- "key": value
- Commas between pairs

## A student
@ Switch
```
student = {
    "name": "Jimmy",
    "age": 15,
    "grade": "Year 10",
}
print(student["name"])
print(student["age"])
```

## Add, change, delete
```
student["school"] = "Code High"
student["age"] = 16
del student["grade"]
print(student)
```

## Keys are unique
- Two keys cannot share a name
- Values may repeat
- student["hobby"] crashes
- Use a key you know exists

## Your turn
- One character
- name, level, health
- Print the name
- Next: records, tuples, sets

# 17 | Records, tuples, sets | 20
## A record is a form
@ Lesson 17
- Fields can be different types
- dataclass is one clean way

## Character
@ Switch
```
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

## A tuple does not change
```
position = (10, 20)
x, y = position
print(x, y)
```
- One item needs a comma: (1,)
- position[0] = 5 fails
- That is the point

## A set keeps uniques
```
found = {"key", "coin", "key"}
print(found)
found.add("map")
print("coin" in found)
```
- One key, not two
- Empty set is set()
- {} is a dictionary

## Tasks
```
tasks = [["wake up", 10], ["breakfast", 15], ["code", 45]]
total = 0
for task in tasks:
    print(task[0], task[1], "min")
    total = total + task[1]
print("Total", total)
```

## Your turn
- Add one task
- Run it again
- Next: sequence

# 18 | Sequence | 21
## Three kinds of flow
@ Lesson 18
- Sequence: straight ahead
- Selection: a choice
- Iteration: again
- Today is only the first

## Line, then line
- Line 1 finishes
- Then line 2
- Python reads a line and does it

## Flowchart shapes
- Oval: start or stop
- Rectangle: a step
- Slanted box: input or output
- Diamond: a choice, later
- Arrow: the direction

## Welcome
@ Switch
```
player_name = input("Enter your name: ")
print("Welcome,", player_name)
score = 0
print("Score starts at", score)
```

## The mistake
- Print score before score = 0
- The name does not exist yet
- Move the line back

## Your turn
- Ask for a colour
- Print it back
- Three lines is enough
- Next: if

# 19 | if, else, elif | 22
## if
@ Lesson 19
- Colon at the end
- Indent the lines that depend on it
- They run only when the test is True

## Alive?
@ Switch
```
player_health = 100
if player_health > 0:
    print("Player is alive")
```

## else is plan B
```
player_stamina = 0
if player_stamina > 0:
    print("You can sprint")
else:
    print("Too tired to run")
```
- else has no test
- Same indent as if

## elif asks the next question
```
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
- 75 prints Doing well
- Python stops at the first True
- Put the high bar first

## and, or, not inside if
```
has_key = True
knows_code = False
locked_by_magic = False
can_unlock = (has_key or knows_code) and not locked_by_magic
if can_unlock:
    print("You unlocked the chest")
```
- not, then and, then or
- Brackets when it gets busy

## The mistake
- else must not have a condition
- Else with a capital E is wrong
- Write elif, not else if

## Your turn
- homework_done = True
- If True: Movie time
- Else: Finish homework first
- Next: a question inside a question

# 20 | Nested if and match | 23
## A second question
@ Lesson 20
- Ask it only if the first answer was yes
- Indent again

## The door
@ Switch
```
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
- Flip has_enemy to False and run
- Flip has_key to False and run

## match one word
```
player_action = "JUMP"
match player_action:
    case "JUMP":
        print("Player jumped")
    case "RUN":
        print("Player is running")
    case _:
        print("Unknown action")
```
- _ means anything else
- Needs Python 3.10 or newer

## Which tool
- Ranges of a number: if, elif
- One exact word, many arms: match
- Two levels of if is fine
- Deeper than that: flatten it

## Your turn
- Set player_action to "RUN"
- Run it
- Next: while

# 21 | while | 24
## Again, while this is true
@ Lesson 21
- Test before each lap
- Something inside must change
- Or it never ends

## Countdown
@ Switch
```
resources = 5
while resources > 0:
    print("Working...", resources)
    resources = resources - 1
print("Done")
```

## break leaves now
```
calculation = 0
while calculation < 10:
    calculation = calculation + 1
    if calculation == 4:
        print("Stopped early")
        break
print("After the loop", calculation)
```

## No do-while in Python
```
while True:
    word = input("Type STOP to finish: ")
    if word == "STOP":
        break
    print("You typed", word)
```
- The body runs, then you decide
- continue skips to the next lap

## The mistake
@ Have the Stop button ready
```
n = 3
while n > 0:
    print(n)
```
- n never shrinks
- Press Stop
- Then add n = n - 1

## A game number
```
from random import randint
player_health = 100
while player_health > 0:
    damage = randint(10, 20)
    player_health = player_health - damage
    print("Health:", player_health)
print("Game over")
```
- randint(10, 20) includes 10 and 20
- This is a game counter, not health advice

## Your turn
- Print 3, 2, 1, Go
- Use while
- Next: for

# 22 | for | 25
## A known number of laps
@ Lesson 22
- for: you know the collection, or the count
- while: you are waiting for something

## range
@ Switch
```
for i in range(5):
    print("Lap", i)
print("Done")
```
- 0 1 2 3 4
- Not 5

## A list
```
items = ["map", "rope", "torch"]
for item in items:
    print("Pack", item)
```

## Index and value
```
for i, item in enumerate(items, start=1):
    print(i, item)
```

## continue and break
```
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

## Countdown you can count
```
for n in range(10, 0, -1):
    print(n)
print("Go")
```
- No do-while
- No repeat-until
- "again while not finished" is while not finished

## Your turn
- Three tasks
- Print 1. wake up using enumerate
- Next: the game

# 23 | Guess the Number | 26
## The capstone
@ Lesson 23 · about 15 minutes
- Secret number, 1 to 100
- Seven tries
- Too high, too low, or not a number
- Type it in pieces

## Piece 1
@ Switch
```
import random
ATTEMPT_LIMIT = 7
answer = random.randint(1, 100)
attempt = 0
won = False
print("Welcome to Guess the Number")
```
- randint includes 1 and 100
- Do not print answer in the real game

## Piece 2, the loop
```
while attempt < ATTEMPT_LIMIT and not won:
    print("Attempt", attempt + 1, "of", ATTEMPT_LIMIT)
    text = input("Your guess (1-100): ")
```

## Piece 3, reject junk
```
    if not text.isnumeric():
        print("Type a whole number.")
        continue
    guess = int(text)
    if guess < 1 or guess > 100:
        print("Stay between 1 and 100.")
        continue
    attempt = attempt + 1
```
- A bad input does not burn a try
- continue goes to the next lap

## Piece 4, the hint
```
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

## Play it
- One real guess on camera
- Then type ten
- Show the friendly message
- Chromebook: paste into one Colab cell

## Your turn
- Change the limit to 5
- Or the range to 1–20
- You now have the toolbox
- The course stops here
# A | Only if Python will not open on Windows | 01
## Install Python on Windows
@ Setup · only if Python will not open
- For a Windows laptop at home
- Already in Thonny or Colab? Go back to Hello
- Two installs: Python, then Thonny

## Download Python 3
- python.org/downloads
- Big Download button
- Python 3, not Python 2
- Run the installer

## The tick people miss
- Tick Add python.exe to PATH
- Then Install Now
- Click Yes if Windows asks
- Disable path length limit if you see it

## Prove it
- Start, type cmd, Enter
- python --version
- You want Python 3.something
- Not recognized? Install again and tick PATH

## Install Thonny
- thonny.org
- Windows installer
- Next, Next, Install
- Open Thonny. The type is already big.

## Switch
@ Switch to Thonny
```
print("Hello from Windows")
```

## Your turn
- Run that line
- Save as hello_windows.py
- Screenshot the version and the Hello line
- Next: back to Hello, unless the computer is a Mac

# B | Only if Python will not open on a Mac | 02
## Install Python on a Mac
@ Setup · only if Python will not open
- For a Mac at home
- Already in Thonny or Colab? Go back to Hello
- Do not use the old hidden system Python

## Download
- thonny.org
- macOS download
- Open the pkg
- Continue, then Install

## If the Mac says no
- Right-click the installer
- Open, then Open again
- Or Privacy and Security
- Then Open Anyway

## First line
@ Switch to Thonny
```
print("Hello from Mac")
```

## Optional check
- Open Terminal only if you want to
- python3 --version
- Thonny does not need this

## Your turn
- Green Run
- Save as hello_mac.py
- School Mac blocked? Use the Chromebook setup
- Next: back to Hello, unless you are on a Chromebook

# C | Chromebook, no install | 03
## Python on a Chromebook
@ Setup · class path, no install
- Only if you are on a Chromebook
- Already in Colab? Go back to Hello
- No install. Chrome is enough

## Leave Linux off
- Schools often block Linux
- Do not install Thonny here
- Stay in the browser
- Same Python language

## Open Colab
- colab.research.google.com
- Sign in
- File, New notebook
- School account blocked? Use a family Gmail

## Run a cell
@ Switch to Chrome
```
print("Hello, Chromebook")
```
- Shift+Enter
- The answer sits under the cell

## Save
- File, Save a copy in Drive
- Name the notebook
- Later cells see a name only if you ran the earlier cell

## If Colab is blocked
- trinket.io, then Python
- or replit.com, Python, Run
- Pick one
- Use it all term

## Your turn
- Hello is on the screen
- The notebook is saved
- Next: back to Hello

