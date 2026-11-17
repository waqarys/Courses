---
id: "4.1"
title: "Sequence and Flowcharts"
module: 4
module_title: "Making Decisions and Loops"
next: "if: Making a Choice"
minutes: 7.42
thumb_code: '# 1. Wake up'
goals: ["What an algorithm is", "The three building blocks: sequence, selection, iteration", "Flowchart shapes", "Turning a flowchart into code"]
youtube:
  title: "Python Lesson 4.1: Algorithms, Sequence and Flowcharts | Introduction to Python"
  description: |
    Module 4 begins! Ziggy the Python explains algorithms as recipes, the three building blocks of every program
    (sequence, selection and iteration), and the shapes used in flowcharts. Then we turn a morning routine and a
    sandwich-making flowchart into Python, step by step, and see why the order of steps matters.
    For beginners aged 7 to 20.
  tags: [algorithms for kids, flowcharts, sequence selection iteration, python for beginners, learn python, fun skill builders]
---

<!-- Booklet chapter 4 "Control Structures": sequence and flowcharts. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Welcome to Module Four, where our programs learn to make decisions and repeat things. Before we write that kind of code, we'll learn how programmers plan it, using algorithms and flowcharts. Planning first makes the coding much easier.

## STUDY | What is an algorithm?
@ point An algorithm = a set of steps to solve a problem
An algorithm is a set of steps that solves a problem or completes a task. That's all. You use algorithms every day without calling them that.
@ point Recipes, directions, the rules of a game
A recipe is an algorithm for making a meal. Directions to a friend's house are an algorithm for getting there. The rules for tying your shoelaces are an algorithm too.
@ point Good algorithms are clear, exact and in the right order
A good algorithm is clear, so nobody has to guess. It's exact, so every step means one thing. And its steps are in the right order. If you put your shoes on before your socks, the algorithm has a bug!
@ point A program is an algorithm written in a programming language
A program is simply an algorithm written in a language a computer can follow. So programmers often design the algorithm first, in plain words or pictures, and then translate it into code.

## STUDY | Three building blocks
@ table Building block | Means | Python ; sequence | steps run one after another | lines, top to bottom ; selection | choose which steps to run | if, elif, else, match ; iteration | repeat steps | for, while
Here's an amazing fact. Every program ever written, from a calculator to a video game, is built from just three building blocks. Sequence means steps run one after another, in order. Selection means choosing which steps to run, depending on a question. And iteration means repeating steps.
@ point We've used sequence since lesson 1
We've been using sequence since our very first program: Python runs lines from top to bottom.
@ point We met iteration with for loops in lesson 3.4
We met iteration in lesson three point four, with for loops.
@ point This module: selection, and more iteration
In this module, we'll learn selection, which lets programs make decisions, and we'll go much deeper into iteration.

## STUDY | Flowchart shapes
@ table Shape | Used for ; oval (rounded) | Start and Stop ; rectangle | a process: do something ; parallelogram (slanted) | input or output ; diamond | a decision: a yes/no question ; arrow | which step comes next
A flowchart is a picture of an algorithm. Each kind of step has its own shape. An oval, with rounded ends, marks the start and the end. A rectangle is a process, an action like add the cheese. A slanted box, called a parallelogram, means input or output, like ask for a name, or show the score. A diamond is a decision: a question with a yes or no answer. And arrows show which step comes next.
@ flow Start > Input: ask name > Process: make greeting > Output: show greeting > Stop
Here's a tiny flowchart for a greeting program. Start. Input: ask for the name. Process: make the greeting. Output: show it. Stop. Each box becomes roughly one line of code.
@ point A diamond has two arrows out: Yes and No
A decision diamond always has two arrows coming out of it, one labelled yes and one labelled no. That's where the program can go two different ways. Next lesson, we'll turn those diamonds into if statements.

## CODE | morning.py
```python
# Morning routine: a sequence
print("1. Wake up")
print("2. Brush teeth")
print("3. Get dressed")
print("4. Eat breakfast")
print("5. Pack school bag")
print("Ready for school!")
```
@ say
Let's code a pure sequence: a morning routine. In a flowchart, this would be a start oval, five rectangles joined by arrows, and a stop oval.
@ line 1 | A comment names the algorithm
A comment names the algorithm.
@ line 2-6 | Five steps in order
Five steps, one per line, in the order they should happen.
@ line 7 | The end
And a final message.
@ run | Sequence: top to bottom, every step once
Run. Every step, once, in order. That's sequence.
@ edit 4 => print("3. Eat breakfast")
Now let's swap two steps. Line four becomes eat breakfast.
@ edit 5 => print("4. Get dressed")
And line five becomes get dressed.
@ predict 4 | Is the new order still OK?
Is the routine still fine with these two steps swapped?
@ run | Some steps can swap, others can't
Run. Eating breakfast before getting dressed is fine. But what if we swapped brushing teeth with waking up? Brushing your teeth while asleep is impossible! When you design an algorithm, ask: which steps must come before others? Programmers call these dependencies.

## CODE | sandwich.py
```python
# Algorithm: make a cheese sandwich
bread = 2
print("Take", bread, "slices of bread")
filling = input("Which cheese? ")
print("Spread butter on one side of each slice")
print(f"Add the {filling}")
print("Put the slices together")
bread = bread - 2
print("Slices of bread left over:", bread)
print("Enjoy!")
```
@ input cheddar
@ say
Here's a bigger sequence, with all the shape types. Imagine the flowchart: start, a process box for taking the bread, an input box asking which cheese, more process boxes, an output box, and stop.
@ line 1 | The algorithm's name
The algorithm's name as a comment.
@ line 2-3 | Process: take two slices
Lines two and three: a process. Take two slices of bread.
@ line 4 | Input: a slanted box
Line four is an input step, the slanted box in the flowchart. Which cheese?
@ line 5-7 | Process steps
Lines five to seven are processes: spread, add the filling, put together.
@ line 8 | Update a variable: the bread is used
Line eight updates the bread variable, because we used two slices.
@ line 9-10 | Output, then stop
And lines nine and ten are output steps before we stop.
@ predict 4 | How many slices are left?
How many slices of bread will be left over?
@ run | Each flowchart box became a line of code
Run. I'll choose cheddar. Take two slices, which cheese, cheddar, spread, add the cheddar, put together, zero slices left, enjoy! Every box from our flowchart became a line of code, in the same order. That's why flowcharts are so useful: once the plan is right, the code follows.

## STUDY | Tips for drawing flowcharts
@ point Use paper, a whiteboard, or a free online tool
You can draw flowcharts on paper, on a whiteboard, or with a free online diagram tool. They don't need to be beautiful. They need to be clear.
@ point One action per box, written as a short instruction
Write one action per box, as a short instruction, like add the cheese, rather than a whole paragraph.
@ point Follow it with your finger to test it
And test your flowchart by following the arrows with your finger, pretending to be the computer. If you get stuck, or a step is missing, you've found a bug before writing any code. That's the cheapest kind of bug to fix.
@ point Pseudocode: plan in plain English instead
Some programmers prefer pseudocode instead: the algorithm written as numbered plain English steps that look a bit like code. Our comment stubs from lesson two point eight are a kind of pseudocode.

## REVISE | Quick revise
@ point An algorithm is a clear set of steps in the right order
An algorithm is a clear set of steps, in the right order.
@ point Sequence, selection, iteration build every program
Sequence, selection and iteration build every program.
@ point Oval = start/stop, rectangle = process, parallelogram = input/output, diamond = decision
Ovals start and stop, rectangles are processes, parallelograms are input and output, and diamonds are decisions.
@ point Plan with a flowchart or pseudocode, then code it
Plan with a flowchart or pseudocode, then turn it into code.

## PRACTICE | An everyday algorithm
@ task Draw a flowchart for a task you do every day (brushing teeth, making a drink, feeding a pet). Use at least one input or output box. Then code it as a sequence of print() lines.
Your turn. Choose a task you do every day, like brushing your teeth, making a drink, or feeding a pet. Draw a flowchart for it with the correct shapes, including at least one input or output box. Then turn it into a Python program, one line per box.
@ hint Start oval → boxes joined by arrows → Stop oval. One print per box.
Hint: start with an oval, join your boxes with arrows, and finish with another oval. Then write one line of code per box.
@ pause 15
Pause the video, draw it, and code it.

## ANSWER | hot_chocolate.py
```python
# Algorithm: make a hot chocolate
print("Boil the kettle")
spoons = input("How many spoons of chocolate? ")
print(f"Put {spoons} spoons of chocolate in a mug")
print("Pour in hot water and stir")
print("Add a splash of milk")
print("Drink carefully!")
```
@ input 2
@ line 1
Here's my version: a hot chocolate.
@ line 2
A process: boil the kettle.
@ line 3
An input: how many spoons?
@ line 4-7
Then processes and an output.
@ run
Run, with two spoons. Each box from the flowchart became one line. Your algorithm might be about something completely different, and that's great. If it has a clear order, and each step is exact, it's a good algorithm.

## OUTRO
Great planning! You now know what algorithms are and how to draw them. Next time, we'll turn the decision diamond into code, with the if statement. Like, share and subscribe, and keep coding. Happy Learning!
