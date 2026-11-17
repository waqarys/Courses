---
id: "5.1"
title: "Functions: Your Own Commands"
module: 5
module_title: "Next Steps"
next: "Parameters and return"
minutes: 7.28
thumb_code: 'def say_hello():'
goals: ["What a function is and why we use them", "def, the colon and the indented body", "Defining vs calling", "Functions calling other functions"]
youtube:
  title: "Python Lesson 5.1: Functions - Make Your Own Commands with def | Introduction to Python"
  description: |
    Module 5 begins! Ziggy the Python explains functions as reusable recipe cards: how to define one with def,
    how to call it, why defining doesn't run anything, and why functions make programs shorter, clearer and
    easier to fix. We build banners, a song with a repeating chorus, and functions that call other functions.
    For beginners aged 7 to 20.
  tags: [python functions, def python, python for beginners functions, reusable code, learn python, fun skill builders]
---

<!-- Beyond the booklet: functions (sub-programs). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Welcome to Module Five, Next Steps. We've used lots of Python's built in functions, like print, input, len and range. Today, you'll learn to make your own. Functions let you give a name to a group of instructions, and then use them whenever you like, with a single line.

## STUDY | What is a function?
@ point A function = a named group of instructions
A function is a named group of instructions that does one job. Once you've made it, you can run all those instructions just by using the name.
@ point Like a recipe card you can use again and again
Think of a recipe card. You write the steps for making pancakes once. After that, whenever someone says let's make pancakes, you don't rewrite the recipe. You just follow the card. A function is a recipe card for the computer.
@ point We've already used built-in functions: print(), len(), input()
You've been using functions since lesson one. Print, len, input, range and round are all functions that Python's creators wrote for us. Now we'll write our own.
@ table Without functions | With functions ; the same code copied many times | written once, used many times ; a fix must be made in every copy | fix it in one place ; one long list of instructions | small named pieces that explain themselves
Why bother? Without functions, you often copy the same lines into lots of places. If there's a bug, you have to fix every copy. With functions, the code is written once, fixed in one place, and the program is split into small named pieces that explain what they do.

## STUDY | Defining and calling
@ snippet def say_hello():\n    print("Hello!")\n    print("Welcome to Python.")
To make a function, we define it. The word def, short for define, then the function's name, a pair of round brackets, and a colon. Then the body: the instructions, indented by four spaces.
@ point Defining does NOT run the code
Here's the surprising part: defining a function doesn't run it. It just teaches Python a new command, like writing the recipe card and putting it in a drawer.
@ snippet say_hello()
To run it, we call the function: its name, followed by round brackets. Every time you call it, the whole body runs.
@ point Name functions with verbs, in snake_case
Function names follow the same rules as variable names, in snake case. Good function names usually start with a verb, because a function does something: say hello, draw banner, show score.
@ point Define functions BEFORE you call them
And Python reads from top to bottom, so a function must be defined before the line that calls it. That's why functions usually go at the top of a program.

## CODE | hello_function.py
```python
def say_hello():
    print("Hello!")
    print("Welcome to Python.")

print("Program starts")
```
@ line 1 | def name(): defines a new command
Line one defines a function called say hello. Def, the name, round brackets, and a colon.
@ line 2-3 | The indented body
Lines two and three are the body, indented.
@ line 5 | The main program
After a blank line, the main program starts with a message.
@ predict 4 | Will "Hello!" be printed?
We've defined say hello. Will hello appear when we run this?
@ run | Defining doesn't run the body
Run. Only program starts! The function was defined, but nobody called it. The recipe card is in the drawer, unused.
@ edit 6 => say_hello()
Let's call it, by writing its name with round brackets.
@ edit 7 => say_hello()
And again.
@ edit 8 => say_hello()
And a third time.
@ predict 4 | Three calls. How many lines of output?
Three calls. How many lines will we see now?
@ run | Each call runs the whole body
Run. Program starts, then hello and welcome, three times. Seven lines. Each call ran the whole body. Two lines inside the function gave us six lines of output, from just three short calls.

## CODE | banner.py
```python
def draw_line():
    print("*" * 30)

def show_banner():
    draw_line()
    print("   ZIGGY'S CODING CLUB")
    draw_line()

show_banner()
print("Meeting every Friday!")
show_banner()
```
@ say
Functions can call other functions. Let's build a banner out of smaller pieces.
@ line 1-2 | A tiny function: one line of stars
The first function, draw line, prints a line of thirty stars.
@ line 4 | A second function
The second function, show banner, uses the first.
@ line 5-7 | It calls draw_line twice
It calls draw line, prints a title, and calls draw line again.
@ line 9 | Call show_banner
Then the main program calls show banner.
@ line 10-11 | Some text, then the banner again
Prints a message, and shows the banner once more.
@ predict 6 | How many lines of stars will appear?
How many lines of stars will we see in total?
@ run | Four lines of stars
Run. Four lines of stars: two in each banner. Python followed the calls like a trail: the main program called show banner, which called draw line, which printed the stars. Then it came back and carried on. Now imagine we want dashes instead of stars. We change one character, in one place, and every banner updates.

## CODE | song.py
```python
def chorus():
    print("Code all day, code all night,")
    print("Debug the bugs and get it right!")
    print()

print("Verse 1: I started with print...")
chorus()
print("Verse 2: Then I learned a loop...")
chorus()
print("Verse 3: Now I write functions!")
chorus()
```
@ say
Here's a fun example. Songs have a chorus that repeats between the verses. That's a perfect job for a function.
@ line 1-4 | The chorus, written once
The chorus is written once, as a function: two lines of lyrics and a blank line.
@ line 6-11 | Verses, with the chorus between them
Then three verses, with the chorus called after each one.
@ run | The chorus repeats after every verse
Run. Verse one, chorus. Verse two, chorus. Verse three, chorus. If the songwriter changes a word in the chorus, it changes everywhere, automatically. This idea is called don't repeat yourself, and it's one of the most important habits in programming.

## STUDY | Tracing a function call
@ flow Main program reaches say_hello() > Jump into the function's body > Run every line of the body > Return to the line after the call
Let's look at exactly what happens when Python calls a function. The main program reaches the call. Python jumps into the function and runs its body from top to bottom. Then it returns to where it came from, and carries on with the next line.
@ point Many editors have a "debug" mode to watch this step by step
Many editors, including Thonny, have a debug mode that lets you step through a program one line at a time, and watch Python jump in and out of functions. It's a brilliant way to understand what your code is really doing.

## STUDY | Common mistakes
@ table Mistake | What happens ; say_hello (no brackets) | nothing happens: the function isn't called ; calling before def | NameError: Python hasn't seen it yet ; def say_hello() (no colon) | SyntaxError ; body not indented | IndentationError
Common function mistakes. Writing the name without round brackets doesn't call the function, so nothing happens. Calling a function before it's defined gives a NameError. Forgetting the colon after the brackets. And forgetting to indent the body.

## REVISE | Quick revise
@ point A function is a named, reusable group of instructions
A function is a named, reusable group of instructions.
@ point def name(): then an indented body
Define it with def, the name, brackets and a colon, then an indented body.
@ point Defining doesn't run it; calling name() does
Defining doesn't run it. Calling it with round brackets does.
@ point Functions can call other functions; define before calling
Functions can call other functions, and must be defined before they're called.

## PRACTICE | Banner function
@ task 1. Write a function called cheer() that prints "Hip hip, hooray!"\n2. Write a function called celebrate() that calls cheer() three times, then prints "Well done!"\n3. Call celebrate()
Your turn. Write a function called cheer, that prints: hip hip, hooray! Then write a second function, called celebrate, that calls cheer three times, and then prints well done. Finally, call celebrate.
@ hint def cheer(): ... then def celebrate(): with three cheer() calls inside
Hint: define cheer first. Inside celebrate, call cheer three times. Then one call to celebrate at the bottom, not indented.
@ pause 15
Pause the video and try it.

## ANSWER | celebrate.py
```python
def cheer():
    print("Hip hip, hooray!")

def celebrate():
    cheer()
    cheer()
    cheer()
    print("Well done!")

celebrate()
```
@ line 1-2
The cheer function.
@ line 4-8
The celebrate function calls cheer three times, then prints well done.
@ line 10
And one call starts it all.
@ run
Run. Hip hip hooray, three times, and well done. If you used a for loop with range three inside celebrate, that's an even better answer!

## OUTRO
Brilliant! You can now create your own commands. Next time, we'll make functions much more powerful, by passing information into them with parameters, and getting answers back with return. Like, share and subscribe, and keep coding. Happy Learning!
