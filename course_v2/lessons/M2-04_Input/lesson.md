---
id: "2.4"
title: "Asking Questions with input()"
module: 2
module_title: "Variables, Input and Output"
next: "Numbers: int and float"
minutes: 8.35
thumb_code: 'name = input("Name? ")'
goals: ["Input, process, output", "How input() waits for an answer", "Storing answers in variables", "input() always gives text"]
youtube:
  title: "Python Lesson 2.4: The input() Function - Programs That Ask Questions | Introduction to Python"
  description: |
    Make your programs interactive! Ziggy the Python explains input, process and output, how the input function
    pauses and waits for the user, and why the answer always arrives as text. We build a chat program, a robot
    card and a silly story maker line by line, meet a surprising error, and you build a mini quiz of your own.
    For beginners aged 7 to 20.
  tags: [python input, input function python, interactive python, python for beginners, learn python, fun skill builders]
---

<!-- Booklet chapter 2 "Input and Output". -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Until now, our programs have done all the talking. Today, they'll start a conversation. They'll ask you questions, listen to your answers, and reply. Every app that lets you type something, from a search box to a game's name screen, uses this idea. Let's meet the input function!

## STUDY | Input, process, output
@ flow Input: get information > Process: work with it > Output: show the result
Almost every program in the world follows the same three steps. Input: get some information. Process: do something with it. Output: show the result.
@ point A calculator: buttons in, sum worked out, answer shown
A calculator takes the numbers you press, which is the input. It adds them up, which is the process. And it shows the answer, which is the output.
@ point A game: button presses in, character moves, new picture
A game reads your button presses, moves your character, and draws the new picture on the screen, many times every second. Input, process, output, over and over again.
@ point print() is output. input() is input.
We already know the output part. That's print. Today we learn the input part, using a function called input.

## STUDY | How input() works
@ snippet name = input("What is your name? ")
Here's what it looks like. A variable, the equals sign, then input with a question inside the brackets. The question is called a prompt, because it prompts the user to type something.
@ point 1. Python shows the question and WAITS
When Python reaches this line, it shows the question and then waits. It's like a waiter in a restaurant standing at your table with a notepad. Nothing else happens until you answer.
@ point 2. You type an answer and press Enter
You type your answer and press the Enter key. Enter is how you tell Python: I'm finished.
@ point 3. The answer is stored in the variable
Then Python takes whatever you typed and stores it in the variable on the left. Now the program can use your answer as many times as it likes.
@ point Tip: add a space at the end of the question
A small tip: put a space just before the closing quote mark of your question. Otherwise, the answer appears squashed right up against the question mark.
@ point In this video, the answers appear in yellow
In these videos, Ziggy types the answers for you, and they appear in yellow, so you can tell the difference between what the program printed and what the user typed.

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
And line five tries to add one to the age, to work out next year's age.
@ predict 5 | What do you think will happen?
What do you think will happen? Will it print twelve?
@ run | TypeError: you can't add text and a number
Run it again, with the same answers, and eleven for the age. Error! A TypeError. It says we can only join a string to another string, not a number. Remember, input always gives us text. So age is the text eleven, not the number eleven. Python doesn't know how to add text and a number. Next lesson, we'll learn how to turn text into a real number.

## CODE | robot.py
```python
robot = input("Name your robot: ")
power = input("Its super power? ")
print("=" * 30)
print(f"Meet {robot.upper()}!")
print(f"{robot} can {power}.")
print(f"Name length: {len(robot)}")
print("=" * 30)
```
@ input zippy | fly
@ say
Here's another one, just for fun: a robot card that combines input with the string tricks from last lesson.
@ line 1-2 | Two questions, two answers
Two questions: a name for your robot, and its super power.
@ line 3 | A border of 30 equals signs
A border of thirty equals signs.
@ line 4 | .upper() on the answer
Then the name, shouted in capitals, using dot upper on the answer.
@ line 5 | A sentence with both answers
A sentence with both answers.
@ line 6 | len() works on answers too
Line six counts the letters in the robot's name with len. The answer is a string, so every string tool works on it.
@ line 7
And the bottom border.
@ run | Every user gets their own card
Run it. I'll call my robot zippy, and its power is to fly. Meet ZIPPY! zippy can fly. Name length: five. Every person who runs this program gets a different card, made from their own answers.

## CODE | story.py
```python
animal = input("An animal: ")
place = input("A place: ")
food = input("A food: ")
print()
print(f"Once upon a time, a {animal}")
print(f"walked all the way to {place}")
print(f"and ate a mountain of {food}.")
```
@ input penguin | the moon | spaghetti
@ say
Now a silly story maker. The program asks for words without saying what they're for, then puts them into a story.
@ line 1-3 | Three questions, three variables
Three questions: an animal, a place and a food.
@ line 4 | A blank line before the story
A blank line, to separate the questions from the story.
@ line 5-7 | Three f-strings tell the story
Then three F strings tell the story, each with one blank to fill.
@ predict 4 | Penguin, the moon, spaghetti. What story will we get?
I'll answer penguin, the moon and spaghetti. Can you picture the story before it appears?
@ run | Same program, a different story every time
Run. Once upon a time, a penguin walked all the way to the moon and ate a mountain of spaghetti. Run it again with different answers, and you get a completely different story. That's the magic of input: one program, endless results.

## CODE | empty_answer.py
```python
name = input("What is your name? ")
print(f"Hello, {name}!")
print(f"Your name has {len(name)} letters.")
```
@ input 
@ say
Here's an interesting question. What happens if the user doesn't type anything, and just presses Enter?
@ line 1 | Ask for a name
Line one asks for a name, as usual.
@ line 2-3 | Greet them, and count the letters
Line two says hello, and line three counts the letters in the name.
@ predict 5 | The user just presses Enter. What happens?
This time, I'm going to press Enter without typing anything. Will Python wait forever? Will it crash? Or something else? Make your prediction.
@ run | An empty answer is an empty string
Run. Hello, comma, exclamation mark, with nothing in between. And: your name has zero letters. Pressing Enter on its own gives an empty string, a string with nothing inside it. Python is perfectly happy with that, but our program looks a bit silly. Real programs check answers like this, and ask again if something is missing. We'll learn how to do that with if statements and loops in Module Four.

## STUDY | Asking good questions
@ point Make the question clear: what should the user type?
Writing good questions is a real skill, and it's part of designing a program that people enjoy using. First, make it clear what the user should type. How old are you is clearer than just: age.
@ point Give an example or the choices: (yes/no), (1-10)
If there are choices, show them. For example: do you want to play again, yes or no, written in brackets. Or: rate your day from one to ten.
@ point Be friendly: people are using your program
And be friendly. Real people are going to use your program, maybe your friends or your family. A cheerful question and a kind reply make a program fun to use. Programmers call this user experience.

## STUDY | Common mistakes
@ table Code | What goes wrong ; input("Name? ") | the answer is not stored, so it is lost ; input("Name?") | no space: the answer is squashed ; print("Hi name") | prints the word name, not the answer ; input("Age? ") + 1 | TypeError: the answer is text
Let's look at the common mistakes. If you call input without storing the answer in a variable, the answer disappears straight away. Forgetting the space makes the answer squash against the question. Putting the variable inside normal quotes prints the word, not the answer, so use an F string. And trying to do maths with an answer gives a TypeError, because input always gives text.

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
@ pause 15
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
