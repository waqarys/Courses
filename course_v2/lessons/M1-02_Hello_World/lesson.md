---
id: "1.2"
title: "Hello, World!"
module: 1
module_title: "Getting Started"
next: "Errors Are Clues"
minutes: 5.7   # rendered video length
thumb_code: 'print("Hello, World!")'
goals: ["What a program is", "How print shows text", "Strings and comments", "Python reads top to bottom"]
youtube:
  title: "Python Lesson 1.2: Hello, World! Your First Program | Introduction to Python"
  description: |
    Write your very first Python program! Pip the Python explains what print does, why text goes inside quote marks,
    what a comment is, and how Python reads your code from top to bottom. Then we type the program line by line,
    run it, and finish with a small exercise you can pause and try.
    For beginners aged 7 to 20. No experience needed. Thonny, IDLE or any Python editor works.
  tags: [python for beginners, python for kids, learn python, hello world python, print function, coding for kids, fun skill builders]
---

<!-- Production notes are written in HTML comments like this one. They are never shown or spoken. -->
<!-- Source order: booklet section 1.4 (first program), 1.8 (smoke testing). Wording is original. -->

## INTRO
Hello, Happy Learners! It's Pip the Python, and today is a big day. You are going to write your very first computer program. It is a tradition that almost every programmer in the world follows. Let's begin!

## STUDY | What is a program?
@ point A program is a list of instructions
A program is a list of instructions for a computer. That's all it is. Imagine you are teaching a robot to make a jam sandwich. You can't just say, make a sandwich. You have to say: open the bread bag. Take out two slices. Pick up the knife. Spread the jam. Every step, in the right order.
@ point Computers do exactly what you say
Computers are like that robot. They are super fast, but they do exactly what you tell them, nothing more and nothing less. If you forget a step, the computer forgets it too. So a programmer's job is to write instructions that are clear and complete.
@ point Python is a language for writing instructions
Python is the language we use to write those instructions. It was designed to be easy for humans to read, which is why so many beginners start with it. And it is not just for beginners. People use Python to build websites, run science experiments, make games and train artificial intelligence.

## STUDY | Meet print
@ snippet print("Hello, World!")
Here is our first instruction. Let's look at it piece by piece.
@ point print means: show this on the screen
The word print is the name of a command. It tells Python: show something on the screen. It does not use a printer and paper. It just shows words in the output area.
@ point Round brackets hold what you want to show
After print come round brackets. Whatever you put inside the brackets is what gets shown. Think of the brackets as a pair of hands, holding the thing you want to give to print.
@ point "Quote marks" make text a string
Inside the brackets we have quote marks around our words. Quote marks tell Python: this is text, just show it exactly as it is. Programmers call a piece of text a string, because it is a string of letters joined together, like beads on a thread.
@ point Level up: print is a function
If you want to sound like a pro, print is called a function. A function is a named mini program that does one job. When we write its name with brackets, we call the function, and the thing inside the brackets is the value we pass to it.

## STUDY | Notes and order
@ point # starts a comment, a note for humans
Sometimes we want to leave a note in our code. A line that starts with a hash sign is a comment. Python skips it completely. Comments are for people, so they can understand what the code is for.
@ flow Line 1 > Line 2 > Line 3
Python reads your program like you read a book: from the top line to the bottom line, one line at a time. Line one finishes, then line two starts. This idea is called sequence, and it is the first big idea in programming.
@ point A smoke test: does it run at all?
Our first program is also a smoke test. When engineers build a new machine, they switch it on and check that no smoke comes out. For us, a smoke test means: does the program run, and does it show exactly what we expect?

## CODE | hello.py
```python
# My first program
print("Hello, World!")
print("I am learning Python.")
print()
print("Python reads from top to bottom.")
```
@ say
Now let's write it together. Open Thonny, IDLE, or any Python editor, and type along with me. Pause the video whenever you need to.
@ line 1 | # = a comment. Python skips it.
Line one is a comment. It starts with a hash sign, so Python will skip it. It just reminds us what this program is.
@ line 2 | print( "text" ) shows the text
Line two is the famous one. print, open bracket, quote mark, Hello comma World with an exclamation mark, quote mark, close bracket. Check that every bracket that opens also closes.
@ line 3 | Each print starts a new line
Line three is another print with a new sentence. Every print starts on a new line of the output.
@ line 4 | print() with nothing inside = an empty line
Line four is print with nothing inside the brackets. That shows an empty line, which is handy for spacing things out.
@ line 5
And line five is our last sentence. Now, what do you think the output will look like? Make a guess before we run it.
@ run | Output = exactly the text inside the quotes
Let's press Run. Look at the output panel. Hello, World. I am learning Python. An empty line. And then our last sentence, all in the same order as our code. Notice that the quote marks are not shown. They only tell Python where the text starts and ends. Our smoke test passed!

## REVISE | Quick revise
@ point A program is a list of instructions in order
A program is a list of instructions, and Python follows them in order, from top to bottom.
@ point print("...") shows text on the screen
print shows something on the screen. The text goes inside quote marks, inside round brackets.
@ point Text in quotes is called a string
Text inside quote marks is called a string.
@ point # makes a comment that Python skips
And a line starting with a hash sign is a comment, a note for humans.

## PRACTICE | Your turn
@ task Write a program that prints three lines: your name, your favourite food, and your favourite animal. Add a comment at the top.
Now it's your turn. Write a program that prints three lines: your name, your favourite food, and your favourite animal. Put a comment at the very top saying what the program does.
@ hint Use one print for each line. Don't forget the quote marks!
Here's a hint. Use one print for each line, and remember the quote marks and both brackets.
@ pause 10
Pause the video now and give it a try. When you're ready, play it again to see my answer.

## ANSWER | about_me.py
```python
# All about me
print("My name is Asha.")
print("I love mango.")
print("My favourite animal is the dolphin.")
```
@ line 1
Here's one way to do it. A comment at the top.
@ line 2-4
Then three prints, one for each line. Your words will be different, and that's perfect.
@ run
When we run it, we get three lines, in order. If yours worked too, give yourself a big high five!

## OUTRO
Amazing work today! You wrote and ran your first program. Next time, we'll make some mistakes on purpose and learn how to read Python's error messages like a detective. Like, share and subscribe, and keep coding. Happy Learning!
