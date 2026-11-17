---
id: "2.4"
title: "Asking Questions with input()"
module: 2
module_title: "Variables, Input and Output"
next: "Numbers: int and float"
minutes: 4.9   # rendered video length
thumb_code: 'name = input("Name? ")'
goals: ["Input, process, output", "How input() waits for an answer", "Storing answers in variables", "input() always gives text"]
youtube:
  title: "Python Lesson 2.4: The input() Function - Programs That Ask Questions | Introduction to Python"
  description: |
    Make your programs interactive! Pip the Python explains input, process and output, how the input function pauses
    and waits for the user, and why the answer always arrives as text. We build a chatty program line by line,
    meet a surprising error, and you build a mini quiz of your own.
    For beginners aged 7 to 20.
  tags: [python input, input function python, interactive python, python for beginners, learn python, fun skill builders]
---

<!-- Booklet chapter 2 "Input and Output". -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Until now, our programs have done all the talking. Today, they'll start a conversation. They'll ask you questions, listen to your answers, and reply. Let's meet the input function!

## STUDY | Input, process, output
@ flow Input: get information > Process: work with it > Output: show the result
Almost every program in the world follows the same three steps. Input: get some information. Process: do something with it. Output: show the result. A calculator takes the numbers you press, adds them up, and shows the answer. A game reads your button presses, moves your character, and draws the new picture.
@ point print() is output. input() is input.
We already know the output part. That's print. Today we learn the input part, using a function called input.

## STUDY | How input() works
@ snippet name = input("What is your name? ")
Here's what it looks like. A variable, the equals sign, then input with a question inside the brackets.
@ point 1. Python shows the question and WAITS
When Python reaches this line, it shows the question and then waits. It's like a waiter in a restaurant standing at your table with a notepad. Nothing else happens until you answer.
@ point 2. You type an answer and press Enter
You type your answer and press the Enter key. Enter is how you say: I'm finished.
@ point 3. The answer is stored in the variable
Then Python takes whatever you typed and stores it in the variable on the left. Now the program can use your answer as many times as it likes.
@ point Add a space at the end of the question
A small tip: put a space just before the closing quote mark of your question. Otherwise, the answer appears squashed right up against the question mark.
@ point Level up: input() ALWAYS returns a string
And here's something that surprises everyone. Whatever you type, even a number, input gives it back as a string, as text. We'll see why that matters in just a moment.

## CODE | chat.py
```python
name = input("What is your name? ")
food = input("What is your favourite food? ")
print(f"Hi {name}! I love {food} too.")
age = input("How old are you? ")
print(age + 1)
```
@ input Asha | pizza | 11
@ line 1 | Shows the question, waits, stores the answer
Line one asks for a name. The answer will be stored in a variable called name.
@ line 2 | A second question, a second box
Line two asks for a favourite food, and stores it in food.
@ line 3 | Use the answers in an f-string
Line three replies, using an F string to put both answers into a friendly sentence.
@ run | Yellow = what the user typed
Let's run it. Python asks for a name and waits. I'll type Asha and press Enter. Then the food question: pizza. And the reply uses both answers: Hi Asha! I love pizza too.
@ line 4 | Ask for an age...
Now let's try something. Line four asks for an age.
@ line 5 | ...and add 1 to it?
And line five tries to add one to the age, to work out next year's age. What do you think will happen?
@ run | TypeError: you can't add text and a number
Run it again, with the same answers, and eleven for the age. Error! A TypeError. It says we can only join a string to another string, not a number. Remember, input always gives us text. So age is the text eleven, not the number eleven. Python doesn't know how to add text and a number. Next lesson, we'll learn how to turn text into a real number.

## CODE | robot.py
```python
robot = input("Name your robot: ")
power = input("Its super power? ")
print("=" * 30)
print(f"Meet {robot.upper()}!")
print(f"{robot} can {power}.")
print("=" * 30)
```
@ input zippy | fly
@ say
Here's one more, just for fun: a robot card that combines input with the string tricks we already know.
@ line 1-2 | Two questions, two answers
Two questions: a name for your robot, and its super power.
@ line 3 | A border of 30 equals signs
A border of thirty equals signs.
@ line 4 | .upper() on the answer
Then the name, shouted in capitals, using dot upper on the answer.
@ line 5-6
A sentence with both answers, and the bottom border.
@ run | Every user gets their own card
Run it. I'll call my robot zippy, and its power is to fly. Meet ZIPPY! zippy can fly. Every person who runs this program gets a different card, made from their own answers.

## REVISE | Quick revise
@ point Programs follow input, process, output
Programs follow three steps: input, process, output.
@ point input("question ") shows the question and waits
input shows a question and waits for the user to press Enter.
@ point Store the answer: answer = input("...")
Store the answer in a variable so you can use it later.
@ point input() always gives back text
And input always gives back text, even when you type a number.

## PRACTICE | Mini quiz
@ task Write a program that asks for the user's favourite colour and favourite animal, then prints: Imagine a blue elephant!
Your turn. Write a program that asks for the user's favourite colour, then their favourite animal. Then print a fun sentence that puts them together, like: imagine a blue elephant!
@ hint Two input lines, two variables, then one f-string.
Hint: you'll need two input lines, each stored in its own variable, and one F string at the end.
@ pause 12
Pause the video and give it a try.

## ANSWER | imagine.py
```python
colour = input("Favourite colour? ")
animal = input("Favourite animal? ")
print(f"Imagine a {colour} {animal}!")
```
@ input blue | elephant
@ line 1-2
Two questions, each stored in a variable: colour and animal.
@ line 3
Then one F string with both blanks.
@ run
Let's run it with blue and elephant. Imagine a blue elephant! Try it with your own answers. What's the silliest one you can make?

## OUTRO
Well done! Your programs can now listen as well as talk. Next time, we'll fix that TypeError by learning about numbers: whole numbers, decimal numbers, and how to convert text into numbers. Like, share and subscribe, and keep coding. Happy Learning!
