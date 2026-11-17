---
id: "5.3"
title: "Python's Toolbox: Modules"
module: 5
module_title: "Next Steps"
next: "Testing your code"
minutes: 8.18
thumb_code: 'import random'
goals: ["What a module is and how import works", "random: randint, choice, shuffle", "math: sqrt, pi, ceil, floor", "datetime: dates and days between them"]
youtube:
  title: "Python Lesson 5.3: Modules - import random, math and datetime | Introduction to Python"
  description: |
    Python comes with a huge toolbox. Ziggy the Python shows how to import modules and use three of the most
    useful: random for dice and choices, math for square roots and rounding up, and datetime for dates and
    counting the days until a birthday. Plus a random compliment generator.
    For beginners aged 7 to 20.
  tags: [python modules, import random python, python math module, python datetime, learn python, fun skill builders]
---

<!-- Beyond the booklet: modules. Booklet 2.2.3 mentions date and time. Random results are seeded (@ seed) and the date is fixed so the video is repeatable. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Last time, we wrote our own functions. But you don't have to write everything yourself. Python comes with a giant toolbox, full of ready made functions written by other programmers. Today, you'll learn how to open that toolbox, and use three of its most useful tools: random, math and datetime.

## STUDY | What is a module?
@ point A module = a file full of ready-made functions
A module is a file full of ready made functions and values, grouped by topic. There's a module for random numbers, one for maths, one for dates, and hundreds more.
@ point The standard library: modules that come with Python
The modules that come with Python are called the standard library. They're already on your computer. You just have to ask for them.
@ snippet import random
To use a module, we import it, usually at the very top of the program. Import, then the module's name.
@ snippet random.randint(1, 6)
Then we use its functions with a dot: the module's name, a dot, and the function's name. This one gives a random whole number from one to six, and both ends are included.
@ point Why not load everything? It keeps programs small and clear
Why doesn't Python load every module automatically? Because there are so many! Importing only what you need keeps programs fast, and shows anyone reading the code exactly which tools it uses.

## CODE | dice.py
```python
import random

print("Rolling five dice...")
for i in range(5):
    roll = random.randint(1, 6)
    print(f"Dice {i + 1}: {roll}")
```
@ seed 5
@ line 1 | import random — open the toolbox
Line one imports the random module.
@ line 3 | A message
Line three prints a message.
@ line 4 | Roll five times
Line four loops five times.
@ line 5 | randint(1, 6): a random number from 1 to 6
Line five picks a random whole number from one to six, just like rolling a dice.
@ line 6 | Show each roll
And line six shows each roll, numbered from one.
@ predict 4 | Can you predict random numbers?
Can you predict what we'll roll? Of course not! That's the point of random.
@ run | Five random rolls
Run. Five, three, six, three, six. If you run this at home you'll get different numbers, and different numbers every time you run it. For this video, we've fixed the random numbers so they come out the same, which is called seeding.

## CODE | random_tools.py
```python
import random

colours = ["red", "green", "blue", "purple"]
print("Random colour:", random.choice(colours))

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print("Shuffled:", cards)

print("Random decimal:", round(random.random(), 2))
```
@ seed 3
@ say
The random module has more tools than randint. Let's try three more.
@ line 3-4 | choice(list): pick one item at random
Lines three and four use choice, which picks one item from a list at random.
@ line 6-7 | shuffle(list): mix up the order
Line seven shuffles a list, mixing up its order, like shuffling cards. Notice it changes the list itself, so we don't use equals.
@ line 8 | Show the shuffled cards
Line eight shows the shuffled cards.
@ line 10 | random(): a decimal between 0 and 1
And line ten makes a random decimal between zero and one, rounded to two places.
@ run | choice, shuffle and random
Run. The random colour is green. The cards are now ace, queen, jack, king. And the random decimal is zero point six three. Games use these tools all the time: shuffling cards, picking enemies, or deciding where treasure appears.

## STUDY | The math module
@ table Tool | What it does | Example ; math.sqrt(x) | square root | math.sqrt(81) is 9.0 ; math.pi | the number pi | 3.14159... ; math.ceil(x) | rounds UP | math.ceil(4.1) is 5 ; math.floor(x) | rounds DOWN | math.floor(4.9) is 4
The math module is full of maths tools. Square root finds the number that multiplies by itself to give x. Pi is the famous number for circles. Ceil, short for ceiling, always rounds up. And floor always rounds down.
@ point ceil and floor ignore the usual "round half up" rule
Remember, ceil and floor don't care how close you are. Ceil of four point one is five, and floor of four point nine is four.

## CODE | maths_tools.py
```python
import math

print("Square root of 81:", math.sqrt(81))
print("Pi:", round(math.pi, 2))

radius = 5
area = math.pi * radius ** 2
print("Circle area:", round(area, 1))

people = 22
seats_per_bus = 10
print("Buses needed:", math.ceil(people / seats_per_bus))
```
@ line 1 | import math
Import the math module.
@ line 3 | Square root
Line three finds the square root of eighty one.
@ line 4 | Pi, to 2 decimal places
Line four shows pi, rounded to two places.
@ line 6-8 | Area of a circle = pi × r²
Lines six to eight work out the area of a circle with radius five: pi times the radius squared.
@ line 10-12 | How many buses for 22 people?
And lines ten to twelve solve a real problem. Twenty two people, and each bus holds ten. How many buses do we need?
@ predict 6 | 22 ÷ 10 = 2.2. How many buses?
Twenty two divided by ten is two point two. But you can't hire point two of a bus! How many do we need?
@ run | 9.0, 3.14, 78.5 and 3 buses
Run. The square root of eighty one is nine point zero. Pi is three point one four. The circle's area is seventy eight point five. And we need three buses. Ceil rounded two point two up to three, so nobody gets left behind. Normal round would have said two, and two people would be waving goodbye!

## STUDY | Dates with datetime
@ snippet from datetime import date
Next, dates. Here we use a slightly different import. From datetime, import date. This brings in just the date tool, so we can write date, instead of datetime dot date.
@ point date(year, month, day) makes a date
Date with a year, month and day makes a date value.
@ point date.today() gives today's date
Date dot today gives today's date, from the computer's clock.
@ point Subtract dates to get the gap: (later - earlier).days
And here's the clever part. You can subtract one date from another, and dot days gives the number of days between them. No counting on a calendar needed!

## CODE | birthday.py
```python
from datetime import date

today = date(2026, 11, 17)
print("Today is", today)
print("The year is", today.year)
print("It's a", today.strftime("%A"))

birthday = date(2027, 3, 8)
days_left = (birthday - today).days
print(f"Only {days_left} days until my birthday!")
```
@ line 1 | Import just the date tool
Line one imports date from the datetime module.
@ line 3 | A fixed date, so the video is repeatable
Line three makes a date. At home, you'd write date dot today, but we'll fix the date here so the video always shows the same thing.
@ line 4-5 | Print the date, and just its year
Line four prints the date, and line five prints only its year.
@ line 6 | strftime("%A") gives the day's name
Line six uses a tool called S T R F time, which formats dates. Percent capital A means the full name of the day.
@ line 8-9 | Subtract dates, take .days
Lines eight and nine make a birthday date, subtract today from it, and take the days.
@ line 10 | The countdown
And line ten prints the countdown.
@ run | 111 days to go
Run. Today is two thousand and twenty six, eleven, seventeen. Notice dates print as year, month, day. The year is twenty twenty six. It's a Tuesday. And only one hundred and eleven days until the birthday. Python handled the different month lengths for us. Try it at home with date dot today, and your own birthday.

## STUDY | Other ways to import
@ table How you import | How you use it ; import math | math.sqrt(9) ; from math import sqrt | sqrt(9) ; import random as r | r.randint(1, 6)
There are a few ways to import. Import math means you write math dot before each tool. From math import sqrt brings in just one tool, so you can use it without the dot. And import random as r gives the module a shorter nickname.
@ point Never name your own file random.py or math.py!
A very common trap: never save your own program as random dot py, or math dot py. Python will import your file instead of the real module, and you'll get confusing errors.

## STUDY | Common mistakes
@ table Mistake | What happens ; randint(1, 6) without import | NameError ; random.randint(1, 6) without import random | NameError: random isn't defined ; math.sqrt("81") | TypeError: needs a number ; date(2026, 13, 1) | ValueError: there's no month 13
Common mistakes. Forgetting the import, or forgetting the module name and dot, gives a NameError. Giving a maths tool text instead of a number gives a TypeError. And impossible dates, like month thirteen, give a ValueError.

## REVISE | Quick revise
@ point import module at the top, then module.tool()
Import a module at the top, then use its tools with a dot.
@ point random: randint, choice, shuffle
Random gives us randint, choice and shuffle.
@ point math: sqrt, pi, ceil (up), floor (down)
Math gives us square roots, pi, ceil to round up and floor to round down.
@ point datetime: date(y, m, d), date.today(), (later - earlier).days
Datetime makes dates, finds today, and counts the days between dates.

## PRACTICE | Compliment generator
@ task Make a random compliment generator:\nadjectives = ["awesome", "brilliant", "super", "fantastic"]\nnouns = ["coder", "thinker", "builder", "explorer"]\nPrint 2 random compliments like "You are a super thinker!"
Your turn. Make a random compliment generator. Create a list of adjectives, like awesome, brilliant, super and fantastic, and a list of nouns, like coder, thinker, builder and explorer. Then print two random compliments, such as: you are a super thinker!
@ hint random.choice(adjectives) and random.choice(nouns) inside an f-string
Hint: inside a loop that runs twice, use random dot choice on each list, and put them into an F string.
@ pause 15
Pause the video and try it.

## ANSWER | compliments.py
```python
import random

adjectives = ["awesome", "brilliant", "super", "fantastic"]
nouns = ["coder", "thinker", "builder", "explorer"]

for i in range(2):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    print(f"You are a {adj} {noun}!")
```
@ seed 7
@ line 1
Import random.
@ line 3-4
Two lists of words.
@ line 6-9
Twice, pick a random adjective and a random noun, and print a compliment.
@ run
Run. You are a super thinker! You are a fantastic coder! Yours will be different, and different every time. Add more words to the lists, and you'll get even more combinations.

## OUTRO
Fantastic! You've opened Python's toolbox, and there are hundreds more modules to explore. Next time, we'll learn how to test our code properly, so we can be confident it really works. Like, share and subscribe, and keep coding. Happy Learning!
