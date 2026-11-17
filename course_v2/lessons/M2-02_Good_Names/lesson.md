---
id: "2.2"
title: "Good Names and Constants"
module: 2
module_title: "Variables, Input and Output"
next: "Strings: Playing with Text"
minutes: 4.8   # rendered video length
thumb_code: 'MAX_LIVES = 3'
goals: ["Python's naming rules", "snake_case style", "Meaningful names", "Constants in CAPITALS"]
youtube:
  title: "Python Lesson 2.2: Naming Variables - snake_case and Constants | Introduction to Python"
  description: |
    Good names make code easy to read. Pip the Python covers the rules Python insists on, the snake_case style
    Python programmers use, how to pick meaningful names, and how constants are written in capitals.
    We even fix a broken name live. Then you clean up some badly named variables.
    For beginners aged 7 to 20.
  tags: [python variable names, snake case, python constants, clean code for kids, learn python, fun skill builders]
---

<!-- Booklet 2.1.2-2.1.8: constants, conventions, snake case, meaningful names, camel case, Hungarian notation. -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Last time we made variables. Today we'll learn how to name them well. Good names make your code easy to read, for your friends, for your teachers, and for you, when you come back to it next month!

## STUDY | The rules Python insists on
@ point Use letters, numbers and underscores _
Python has a few strict rules for names. A name can use letters, numbers and the underscore, which is the little line along the bottom. No other symbols are allowed.
@ point A name cannot start with a number
A name can't begin with a number. So player one, spelled with the one at the end, is fine. But one first, starting with the number, will cause an error.
@ point No spaces, and no hyphens
No spaces are allowed, and no hyphens either. Python would read a hyphen as a minus sign and think you're trying to subtract!
@ point Capitals matter: score and Score are different boxes
And remember, Python is case sensitive. Score with a capital S and score with a small s are two completely different boxes.

## STUDY | Names that help humans
@ point snake_case: small letters joined by underscores
Python programmers have a favourite style called snake case. Use small letters, and join words with underscores, like player underscore score. Fitting, for a language called Python, isn't it?
@ table Bad name | Better name ; x | age ; n | number_of_pets ; thing | favourite_colour
Next, make names meaningful. A name like x tells you nothing. Age tells you exactly what's inside. A good name is like a good label on a box: you know what's in it without opening it.
@ point Constants: values that should never change, in CAPITALS
Some values should stay the same for the whole program, like the number of days in a week, or the maximum lives in a game. We call these constants, and we write their names in capital letters, like max underscore lives.
@ point Level up: Python trusts you. CAPITALS are a promise, not a lock.
Here's a secret. Python won't actually stop you from changing a constant. The capital letters are a message to humans: please don't change this. You might also see other styles in other languages, such as camel case, where each new word starts with a capital letter. In Python, we stick with snake case for variables and capitals for constants. These style rules come from Python's official style guide, called PEP 8.

## CODE | names.py
```python
player-score = 5
MAX_LIVES = 3
player_name = "Asha"
lives_left = MAX_LIVES
print(player_name, "has", lives_left, "lives")
```
@ say
Let's see what happens when we break a rule.
@ line 1 | A hyphen in a name?
On line one, we write player, hyphen, score gets five.
@ run | Python sees "player minus score"
Run it. SyntaxError! Python read the hyphen as minus, so it thought we were trying to store a value in player minus score, which makes no sense.
@ edit 1 => player_score = 5
Let's fix it by replacing the hyphen with an underscore. Now it's snake case.
@ line 2 | Constant: CAPITALS
Line two creates a constant called max lives, in capital letters, holding three.
@ line 3 | snake_case variable
Line three is a normal variable in snake case: player name.
@ line 4 | A variable can copy another's value
Line four is interesting. Lives left gets max lives. Python looks inside the max lives box, finds three, and puts a copy of it into lives left.
@ line 5
And line five prints a sentence using our variables.
@ run | Clear names = code that reads like a sentence
Run it. Asha has three lives. Look how easy the code is to read. Even someone who has never coded could guess what it does. That's what good names give you.

## REVISE | Quick revise
@ point Letters, numbers, _ only. Never start with a number.
Names use letters, numbers and underscores, and never start with a number.
@ point No spaces or hyphens. Capitals matter.
No spaces or hyphens, and capitals make a difference.
@ point Variables in snake_case, constants in CAPITALS
Write variables in snake case and constants in capitals.
@ point Choose names that explain what's inside
And choose names that explain what's inside the box.

## PRACTICE | Fix the names
@ task These names are broken or unhelpful. Rewrite them:\n1st_place = "Ravi"\nmy name = "Zara"\nx = 12   # this is an age
Your turn. Here are three names that are broken or unhelpful. The first starts with a number. The second has a space. And the third is just x, but the comment says it's an age. Rewrite all three with good, legal names, and print them.
@ hint Move the number, use underscores, and say what the value is.
Hint: move the number away from the start, use underscores instead of spaces, and give the age a name that says what it is.
@ pause 12
Pause the video and fix them.

## ANSWER | fixed_names.py
```python
first_place = "Ravi"
my_name = "Zara"
age = 12
print(first_place, my_name, age)
```
@ line 1
First place, written as a word, so it doesn't start with a number.
@ line 2
My name, with an underscore instead of a space.
@ line 3
And age instead of x, so we don't even need the comment any more.
@ line 4
Let's print all three to check they work.
@ run
Ravi, Zara, twelve. All legal, all clear. Other good answers are possible, like place one, or zara name. If yours runs and is easy to understand, you got it!

## OUTRO
Great job! Your code is getting cleaner already. Next time, we'll play with text: joining words together, measuring them, shouting them in capitals, and a super handy trick called F strings. Like, share and subscribe, and keep coding. Happy Learning!
