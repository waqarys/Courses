---
id: "4.6"
title: "match / case"
module: 4
module_title: "Making Decisions and Loops"
next: "while Loops"
minutes: 6.86
thumb_code: 'match day:'
goals: ["Choosing between exact values with match", "case _ as the default", "Several values in one case with |", "When to use match and when to use elif"]
youtube:
  title: "Python Lesson 4.6: match and case - A Menu of Choices | Introduction to Python"
  description: |
    Python 3.10 added match and case: a tidy way to choose between exact options. Ziggy the Python compares it to a
    menu with numbered buttons, turns day numbers into day names, groups several values into one case, adds a
    default with case _, and builds a little calculator. We also see when elif is still the better choice.
    For beginners aged 7 to 20.
  tags: [python match case, python switch statement, structural pattern matching, python 3.10, learn python, fun skill builders]
---

<!-- Booklet chapter 4: selection with match/case. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Imagine a vending machine with numbered buttons. Press one for juice, two for water, three for a snack. Each button leads to exactly one result. Today we'll learn match and case, which is Python's tidy way of choosing between exact options like these.

## STUDY | A menu of exact options
@ snippet match choice:\n    case 1:\n        print("Juice")\n    case 2:\n        print("Water")\n    case _:\n        print("Unknown button")
Here's what it looks like. The word match, the value we're checking, and a colon. Then, indented, a list of cases. Each case has a value, a colon, and an indented block.
@ point Python compares the value with each case, from the top
Python takes the value and compares it with each case, from the top down. When it finds an exact match, it runs that block, and skips the rest. Just like elif, the first match wins.
@ point case _ : the default, when nothing else matches
The last case uses an underscore. The underscore is a wildcard that matches anything at all, so it works like else: it catches every value that didn't match an earlier case. It's called the default case.
@ point Needs Python 3.10 or newer
Match and case were added in Python three point ten, in twenty twenty one. Any modern Python has them. If you ever see a syntax error on the word match, your Python is too old.
@ point Other languages call this a switch statement
Many other languages have something similar, called a switch statement. The booklet's case statements are the same idea.

## CODE | day_name.py
```python
day = int(input("Day number (1-7): "))
match day:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case 4:
        name = "Thursday"
    case 5:
        name = "Friday"
    case 6 | 7:
        name = "the weekend!"
    case _:
        name = "not a real day"
print(f"Day {day} is {name}")
```
@ input 6
@ line 1 | Ask for a day number
Line one asks for a day number, from one to seven.
@ line 2 | match the value
Line two says match day, colon.
@ line 3-12 | One case per day
Then one case for each school day, from one to five. Each case sets the name of the day. Notice the indentation: the cases are indented under match, and each block is indented under its case.
@ line 13-14 | case 6 | 7 : either value matches
Line thirteen shows a neat trick. Case six, a straight line symbol, seven. The straight line means or, so this case matches either six or seven.
@ line 15-16 | case _ : anything else
And the default case catches anything else, like zero or ten.
@ line 17 | After the match
After the match, we print the result.
@ predict 5 | Day 6. Which case matches?
The user types six. Which case will match?
@ run | 6 matches case 6 | 7
Run. Day six is the weekend! The value six didn't match one to five, but it matched case six or seven. If you type nine in your own editor, you'll see the default: not a real day.

## STUDY | match or elif?
@ table Use match when... | Use elif when... ; checking ONE value against exact options | checking ranges: score >= 90 ; there are many fixed choices: menus, commands | conditions use different variables ; you want a clear, table-like layout | conditions combine and / or
So when should you use match, and when should you use elif? Use match when you're checking one value against a list of exact options, like menu numbers, commands or colours. Use elif when you need ranges, like score at least ninety, or when your conditions involve different variables, or and and or.
@ point Both work; choose the one that's clearer to read
Many problems can be solved with either. Choose the one that's easier to read. Match shines when there are lots of exact choices, because it looks like a neat table.

## CODE | calculator.py
```python
a = float(input("First number: "))
op = input("Operation (+ - * /): ")
b = float(input("Second number: "))
match op:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*" | "x":
        result = a * b
    case "/":
        result = a / b
    case _:
        result = "unknown operation"
print("Result:", result)
```
@ input 7 | x | 6
@ say
Match works with strings too. Let's build a calculator.
@ line 1-3 | Two numbers and an operation
Three questions: the first number, an operation symbol, and the second number. We use float, so decimals work too.
@ line 4 | match the operation
Then we match the operation.
@ line 5-8 | Plus and minus
Two cases for plus and minus. The values are strings, so they're in quotes.
@ line 9-10 | Accept * OR x for multiply
For multiply, we accept either the star or the letter x, because lots of people type x for times.
@ line 11-12 | Divide
A case for divide.
@ line 13-14 | Default: anything else
And the default catches anything we don't understand.
@ line 15 | Show the result
Finally, we print the result.
@ predict 5 | 7 x 6. Which case? What result?
The user types seven, the letter x, and six. Which case matches, and what's the result?
@ run | "x" matched the multiply case: 42.0
Run. Result: forty two point zero. The letter x matched the multiply case, thanks to the straight line symbol. And it's forty two point zero, because we used float. A real calculator app has exactly this kind of decision inside it.

## CODE | commands.py
```python
command = input("Command: ").strip().lower()
match command:
    case "north" | "n":
        print("You walk north into the forest.")
    case "south" | "s":
        print("You walk south to the river.")
    case "look":
        print("Tall trees all around. A path leads north.")
    case "quit":
        print("Goodbye, adventurer!")
    case _:
        print(f"I don't understand '{command}'.")
```
@ input LOOK
@ say
Here's one more, the kind of thing used in text adventure games. The player types a command, and the game responds.
@ line 1 | Clean up the command
Line one asks for a command, then cleans it up. Dot strip removes any spaces at the start or end, and dot lower makes it lower case. So LOOK, with capitals and a stray space, still works.
@ line 2-6 | Directions, with short versions
The first cases are directions. Each one accepts the full word or a single letter.
@ line 7-10 | look and quit
Then look, and quit.
@ line 11-12 | Default: an f-string shows what they typed
And the default uses an F string to show the player what they typed.
@ predict 5 | "LOOK" in capitals. Will it match?
The player types look in capital letters. Will it match the look case?
@ run | strip() and lower() cleaned it up
Run. Tall trees all around, a path leads north. Dot lower turned it into plain look, so it matched. In Lesson four point seven, we'll put this inside a loop, so the player can keep typing commands until they quit.

## STUDY | Common mistakes
@ table Mistake | What happens ; case 1 or 2: | wrong: put the bar symbol between values ; no case _ | nothing happens for other values ; case "Yes": vs input "yes" | no match: capitals differ ; match on Python 3.9 or older | SyntaxError: upgrade Python
Common match mistakes. Writing the word or between values, instead of the straight line symbol. Forgetting the default case, so unexpected values silently do nothing. Comparing strings with different capitals, which never match, so use dot lower. And using an old version of Python.

## REVISE | Quick revise
@ point match value: then case options, first match wins
Match a value, then list the cases. The first match wins.
@ point case _ is the default (like else)
Case underscore is the default, like else.
@ point case a | b matches either value
A straight line between values means either one.
@ point match for exact options; elif for ranges and mixed conditions
Use match for exact options, and elif for ranges and mixed conditions.

## PRACTICE | Snack menu
@ task Make a snack menu:\n1 → "Apple: 2 coins"  2 → "Juice: 3 coins"  3 → "Sandwich: 5 coins"\nanything else → "Please choose 1, 2 or 3"\nAsk for the choice as a whole number and use match.
Your turn. Make a snack menu. If the user chooses one, print apple, two coins. Two is juice, three coins. Three is a sandwich, five coins. Anything else should print: please choose one, two or three. Ask for the choice as a whole number, and use match.
@ hint choice = int(input(...)); match choice: case 1: ... case _:
Hint: convert the input with int, then three cases and a default.
@ pause 15
Pause the video and try it.

## ANSWER | snack_menu.py
```python
print("1 Apple  2 Juice  3 Sandwich")
choice = int(input("Your choice: "))
match choice:
    case 1:
        print("Apple: 2 coins")
    case 2:
        print("Juice: 3 coins")
    case 3:
        print("Sandwich: 5 coins")
    case _:
        print("Please choose 1, 2 or 3")
```
@ input 4
@ line 1-2
Show the menu, and ask for a choice.
@ line 3-9
Match, with three cases.
@ line 10-11
And the default.
@ run
Run with four. Please choose one, two or three. The default case caught it. Try one, two and three in your own editor to test every case.

## OUTRO
Brilliant! You can now pick from exact options with match and case. Next time, we'll start the loops part of this module with while loops, which keep going for as long as a condition is True. Like, share and subscribe, and keep coding. Happy Learning!
