---
id: "1.1"
title: "Meet Python"
module: 1
module_title: "Getting Started"
next: "Hello, World!"
minutes: 5.2   # rendered video length
thumb_code: 'print(2 + 3)'
goals: ["What computers and code are", "Why Python is a great first language", "The editor, Run and output", "Text versus numbers"]
youtube:
  title: "Python Lesson 1.1: Meet Python - What Is Coding? | Introduction to Python"
  description: |
    What is code, and why do so many people learn Python first? Pip the Python explains how computers follow instructions,
    what a programming language is, and how the editor, the Run button and the output panel work.
    Then we run our first two lines and discover the difference between text and numbers.
    For beginners aged 7 to 20. Works with Thonny, IDLE, or any Python editor.
  tags: [python for beginners, what is python, what is coding, learn python, python for kids, coding for teens, fun skill builders]
---

<!-- Booklet 1.1-1.3 (key ideas: Python, IDE, environment, code). Install videos already exist in videos/ (setup A/B/C). -->

## INTRO
Hello, Happy Learners! I'm Pip the Python. Yes, I'm a snake, and I'm also named after the programming language I love. I'm here to teach you the Python programming language, step by step, from your very first line of code. Let's find out what coding really is.

## STUDY | Computers follow instructions
@ point Computers are fast, but they need instructions
A computer can do billions of tiny jobs every second. It can add numbers, draw pictures and play music. But here is the surprising part. On its own, a computer has no ideas at all. It waits for someone to tell it exactly what to do.
@ flow Pick up toothbrush > Add toothpaste > Brush for two minutes
Think about brushing your teeth. If you wrote the steps for a robot, you would say: pick up the toothbrush, add toothpaste, then brush for two minutes. If you mix up the order, the robot brushes with a dry brush first. Order matters!
@ point A set of instructions is called code
When we write instructions for a computer, we call it code. A complete set of instructions that does a job is called a program. Games, apps and websites are all programs written by people just like you.

## STUDY | What is Python?
@ point A programming language is how we talk to computers
Computers really understand only ones and zeros. Writing in ones and zeros would be very hard for us. So people invented programming languages. They sit in the middle, like a translator between you and the computer.
@ point Python reads almost like English
Python is one of the most popular programming languages in the world. It was created by Guido van Rossum and first released in 1991. Its big idea is that code should be easy to read. Many Python lines look almost like short English sentences.
@ point Used for games, websites, science and AI
And Python is not a toy. People use it to build websites, analyse data in science labs, control robots, make games, and train artificial intelligence. So the skills you learn here can grow with you for years.
@ point Level up: Python is an interpreted language
Here is a detail for the curious. Python is called an interpreted language. A program called the interpreter reads your code one line at a time and carries it out straight away. That is why you can type a line, press Run, and see the result immediately.

## STUDY | Your coding space
@ flow Editor: you type > Run: Python reads > Output: you see the result
To write Python, we use an editor. Thonny and IDLE are free, friendly editors made for beginners. Every editor has three important parts. The editor area, where you type your code. The Run button, which hands your code to Python. And the output area, where Python shows its answer.
@ point The whole setup is called your environment
Programmers call this whole setup their environment. A tool that bundles the editor, the Run button and the output together is called an I D E, which stands for integrated development environment. If Python is not installed yet, the setup videos at the end of this playlist show you how.

## CODE | first_steps.py
```python
print("Hi, I am Pip!")
print(2 + 3)
print("2 + 3")
```
@ say
Let's try it. Type each line with me, and don't worry about understanding every symbol yet. We'll study print properly in the next lesson.
@ line 1 | Text in quotes is shown exactly
Line one asks Python to show a greeting. The words are inside quote marks, so Python shows them exactly as they are.
@ line 2 | No quotes: Python does the maths
Line two has no quote marks. Just two plus three. Without quotes, Python treats this as maths, so it will work out the answer first.
@ line 3 | Quotes: it is just text
Line three looks almost the same, but this time the sum is inside quote marks. What do you think Python will show? The answer, or the sum itself? Make a guess!
@ run | 5 is maths. "2 + 3" is text.
Let's run it. The greeting comes first. Then five, because Python did the maths. Then two plus three, shown exactly as text, because quote marks mean: don't calculate, just show it. That small difference is one of the most important ideas in Python.

## REVISE | Quick revise
@ point A program is a list of instructions in the right order
A program is a list of instructions, and order matters.
@ point Python is a language that is easy to read
Python is a programming language that is easy to read and very powerful.
@ point Editor, Run, Output
You type in the editor, press Run, and read the output.
@ point Quotes = text. No quotes = Python works it out
And the big discovery: with quote marks Python shows text, and without them it works things out.

## PRACTICE | Your turn
@ task Make Python show your name. Then make it work out 7 times 6. (In Python, times is written with a star: *)
Your turn. Make Python show your name. Then on the next line, make Python work out seven times six. In Python, the times sign is a star, which you'll find above the number eight on most keyboards.
@ hint Your name needs quote marks. The sum must NOT have quote marks.
Hint: your name is text, so it needs quote marks. The sum must not have quote marks, or Python will just show it as text.
@ pause 10
Pause the video and try it now.

## ANSWER | name_and_maths.py
```python
print("Ojas")
print(7 * 6)
```
@ line 1
Here's my answer. Line one shows a name, inside quote marks.
@ line 2
Line two has seven, a star, and six, with no quote marks.
@ run
And the output: the name, then forty two. If you got forty two, Python did the maths for you. Brilliant!

## OUTRO
You now know what code is, what Python is, and how the editor, Run and output work together. Next time, we write the most famous program in the world: Hello, World. Like, share and subscribe, and keep coding. Happy Learning!
