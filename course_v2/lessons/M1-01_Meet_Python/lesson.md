---
id: "1.1"
title: "Meet Python"
module: 1
module_title: "Getting Started"
next: "Hello, World!"
minutes: 8.31
thumb_code: 'print(2 + 3)'
goals: ["What a program is", "Why we use a programming language", "The editor, the Run button and the output", "Text versus maths in Python"]
youtube:
  title: "Python Lesson 1.1: Meet Python - What Is Code? | Introduction to Python"
  description: |
    Start your coding journey with Ziggy the Python! Learn what a program is, why computers need a programming
    language, how Python reads your instructions, and how an editor, a Run button and an output panel work together.
    Then we write our very first lines of Python, predict what they will do, and try a first challenge.
    For beginners aged 7 to 20.
  tags: [python for beginners, learn python, what is python, first python program, coding for beginners, fun skill builders]
---

<!-- Booklet chapter 1 "Introduction". Course v2, lesson 1. -->

## INTRO
Hello, Happy Learners! Welcome to Introduction to Python. I'm Ziggy the Python. Yes, I'm a snake, and I'm also named after the programming language I love. In this course, we'll learn to give computers instructions, step by step, one line at a time. No experience needed. If you can read this sentence, you can learn to code. Let's go!

## STUDY | What is a program?
@ point A program is a list of instructions
Let's start with a big question. What is a program? A program is simply a list of instructions that a computer follows. That's it. Every app on a phone, every game, every website, is made of instructions that somebody wrote.
@ point Like a recipe: steps, in order
Think about a recipe for making a sandwich. Take two slices of bread. Spread the butter. Add the cheese. Put the slices together. The steps happen in order, and the order matters. If you put the slices together before adding the cheese, you get a very sad sandwich.
@ point Computers follow instructions exactly
Computers are amazing at following instructions. They're incredibly fast, and they never get bored. But they do exactly what you say, not what you meant. If a recipe says add salt, a person knows to add a pinch. A computer might pour in the whole bag. So we must be clear and precise.
@ point Writing instructions for a computer = coding
Writing these instructions is called coding, or programming. And the people who do it are called programmers. By the end of this lesson, that includes you.

## STUDY | Why a programming language?
@ point Computers really understand 1s and 0s
Deep inside, a computer only understands tiny on and off signals, which we write as ones and zeros. Writing a game in ones and zeros would take forever, and it would be impossible to read.
@ point A programming language sits in between
So people invented programming languages. A programming language sits in the middle. It's easy enough for humans to read and write, and exact enough for a computer to follow.
@ table Language | Often used for ; Python | science, AI, games, websites, automation ; Scratch | first steps with blocks ; JavaScript | web pages ; C++ | fast games and engines
There are hundreds of programming languages. Here are a few. Scratch uses blocks you drag around. JavaScript runs in web pages. C plus plus is used in fast games. And Python is used almost everywhere: science, artificial intelligence, games, websites, and saving people time with boring jobs.
@ point Python reads almost like English
We're learning Python because it reads almost like English. It's short, it's clear, and it's used by beginners and by experts at huge companies. You won't outgrow it.
@ point The interpreter reads your code, top to bottom
When you run a Python program, a helper called the interpreter reads your code from the top line to the bottom line, and carries out each instruction, one after another.

## STUDY | Your coding workspace
@ flow Editor: you type code > Run: Python reads it > Output: you see the result
To write Python, we use three things. The editor is where you type your code. The Run button tells Python to start reading. And the output panel shows what your program prints.
@ point Thonny is a free editor made for beginners
In this course, our screen looks like a simple beginner editor, such as Thonny, which is free. Any Python editor works the same way: type, run, look at the output.
@ point Every program is saved in a file ending in .py
Every Python program is saved in a file, and the file name ends in dot P Y. That tells the computer it's a Python file.

## CODE | first_steps.py
```python
print("Hi")
print(2 + 3)
print("2 + 3")
```
@ say
Time to write real code! Watch the editor. I'll type one line at a time and explain each one.
@ line 1 | print shows something on the screen
Line one says print, then round brackets, and inside them, the word Hi in quote marks. print is a command that means: show this on the screen.
@ run | Our first output!
Let's press Run and see. There it is in the output panel: Hi. You've just watched a real program run.
@ line 2 | No quotes: Python does the maths
Line two is print, and inside the brackets, two plus three, with no quote marks this time.
@ predict 4 | What will line 2 print?
Before we run it, what do you think this line will show? Have a think.
@ run | 2 + 3 is worked out: 5
Run. The first line shows Hi again, because Python always starts from the top. And the second line shows five. With no quote marks, Python treats two plus three as maths and works out the answer.
@ line 3 | The same thing, but in quotes
Line three looks almost the same, but now two plus three is inside quote marks.
@ predict 4 | Five again? Or something else?
Is this going to show five again? Make a guess.
@ run | Quotes = text, shown exactly as typed
Run it! The last line shows two plus three, exactly as we typed it. Quote marks tell Python: this is text, don't work anything out, just show it. That tiny difference, quotes or no quotes, is one of the most important ideas in Python.

## CODE | maths_machine.py
```python
print(10 - 4)
print(6 * 7)
print(20 / 4)
print("6 * 7 =", 6 * 7)
```
@ say
Let's turn Python into a calculator. Computers use slightly different symbols for some maths.
@ line 1 | minus is the usual -
Line one: ten minus four. The minus sign is the normal dash on your keyboard.
@ line 2 | * means multiply
Line two: six times seven. On a keyboard, we don't use an x for times. We use the star, which is called an asterisk.
@ line 3 | / means divide
Line three: twenty divided by four. Dividing uses a forward slash.
@ predict 4 | Can you work them out before Python does?
Can you beat the computer? Work out all three answers in your head before I press Run.
@ run | 6, 42 and 5.0
Run. Six. Forty two. And five point zero. Interesting! When Python divides, it always gives a decimal number, even when the answer is a whole number. We'll learn more about that later.
@ line 4 | Text and maths, separated by a comma
Line four mixes both ideas. First some text in quotes, then a comma, then real maths without quotes.
@ run | The text is shown, the maths is worked out
Run again. The last line says: six times seven equals forty two. The text part is shown exactly, the maths part is worked out, and the comma puts a space between them. You can already make Python explain its own answers.

## STUDY | Common beginner mistakes
@ table Mistake | What happens ; Print("Hi") with a capital P | NameError: Python is case-sensitive ; print("Hi" missing a bracket | SyntaxError ; print(Hi) missing quotes | NameError: Python looks for a name
Everyone makes a few small mistakes at the start, so let's spot them now. Python is case sensitive, which means a capital P and a small p are different letters to Python. So print must be all small letters. Every opening bracket needs a closing bracket. And text needs quote marks on both sides, otherwise Python thinks the word is a name it should already know.
@ point Errors are normal: they are clues, not failures
If you see a red message, don't worry. That's called an error, and it's just Python telling you what confused it. Professional programmers see errors every single day. In lesson three, we'll become error detectives.

## REVISE | Quick revise
@ point A program is a list of instructions, in order
A program is a list of instructions that the computer follows in order.
@ point Python is a programming language that reads like English
Python is a programming language, a middle ground that people and computers can both understand.
@ point print() shows things in the output
print shows something in the output panel.
@ point "In quotes" = text. No quotes = maths
Text goes in quote marks and is shown exactly. Without quotes, Python works out the maths.

## PRACTICE | Your turn
@ task 1. Print your name.\n2. Print the answer to 7 × 6, worked out by Python.\n3. Bonus: print it with a label, like 7 × 6 = 42
Your turn! Open an editor and write a small program. Line one prints your name. Line two prints the answer to seven times six, and Python should work it out, not you. For a bonus, print the answer with a label in front of it.
@ hint Name: use quotes. Maths: no quotes, and * for times.
Hint: your name needs quote marks. The maths doesn't, and remember that times is the star symbol.
@ pause 15
Pause the video now and give it a go.

## ANSWER | name_and_maths.py
```python
print("Asha")
print(7 * 6)
print("7 * 6 =", 7 * 6)
```
@ line 1
Here's one answer. Line one prints a name in quote marks. Use your own name, of course.
@ line 2
Line two prints seven times six, without quotes, so Python works it out.
@ line 3
And the bonus line: a label in quotes, a comma, then the maths.
@ run
Run it. Asha. Forty two. Seven times six equals forty two. If yours looks like this, brilliant work! If not, check your quote marks and brackets, and try again.

## OUTRO
Fantastic work! You now know what a program is, why we use Python, and how to make Python show text and do maths. Next time, we'll write the most famous program in the world: Hello, World! Like, share and subscribe, and keep coding. Happy Learning!
