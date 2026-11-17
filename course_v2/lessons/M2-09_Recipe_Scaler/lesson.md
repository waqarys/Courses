---
id: "2.9"
title: "Mini-Project: Recipe Scaler"
module: 2
module_title: "Variables, Input and Output"
next: "Lists: Many Things in One Box"
minutes: 4.2   # rendered video length
thumb_code: 'scale = people / SERVES'
goals: ["Plan a real program", "Constants, variables and input together", "Maths with floats", "round() for neat answers"]
youtube:
  title: "Python Lesson 2.9: Mini-Project - Pancake Recipe Scaler | Introduction to Python"
  description: |
    Module 2 mini-project! Pip the Python builds a recipe scaler that works out pancake ingredients for any number of
    people, using constants, variables, input, int, float maths, round and f-strings, all planned with comments.
    Then you add a new ingredient yourself.
    For beginners aged 7 to 20.
  tags: [python project for beginners, python recipe calculator, python input int, round python, learn python, fun skill builders]
---

<!-- Booklet 2.7.2 pancake recipe calculator (idea only; code and wording original). -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. It's mini-project time. We're going to build a recipe scaler. You tell it how many people are eating, and it works out exactly how much of each ingredient you need. Let's make some pancakes!

## STUDY | The problem
@ point A recipe serves 4. But what if 6 people are hungry?
Our pancake recipe serves four people. It needs two cups of flour, one and a half cups of milk, and two eggs. But what if six people are hungry? Or ten? Or just one?
@ flow Input: how many people? > Process: scale every ingredient > Output: the new amounts
Let's use input, process, output. Input: ask how many people are eating. Process: scale every ingredient. Output: show the new amounts.
@ point Scale = people / people the recipe serves
The secret is a scale number. Divide the number of people eating by the number the recipe serves. For six people, that's six divided by four, which is one point five. Then multiply every ingredient by one point five.

## STUDY | Tools we'll use
@ table Tool | Job in our program ; RECIPE_SERVES = 4 | a constant ; input() + int() | ask for people ; / and * | the scaling maths ; round() | whole eggs only ; f-strings | neat output
This project uses almost everything from Module Two. A constant for the number the recipe serves, because that never changes. Input and int to ask for the number of people. Division and multiplication for the scaling. And F strings for neat output.
@ snippet round(4.5)  # 4 eggs
There's one new tool: round. You can't crack one and a half eggs! round turns a decimal into the nearest whole number.
@ point Level up: Python rounds exact halves to the even number
A detail for the curious: when a number is exactly halfway, Python rounds to the nearest even number. So round of two point five is two, and round of three point five is four. This is called banker's rounding, and it keeps big totals fair.

## CODE | recipe_scaler.py
```python
# Pancake recipe scaler
RECIPE_SERVES = 4
flour_cups = 2.0
milk_cups = 1.5
eggs = 2

people = int(input("How many people are eating? "))
scale = people / RECIPE_SERVES

print(f"Pancakes for {people}:")
print(f"Flour: {flour_cups * scale} cups")
print(f"Milk:  {milk_cups * scale} cups")
print(f"Eggs:  {round(eggs * scale)}")
```
@ input 6
@ line 1 | What the program is
A title comment first.
@ line 2 | Constant = never changes
Line two is our constant. The recipe always serves four.
@ line 3-5 | The original amounts
Lines three to five store the original amounts. Flour and milk are floats, and eggs is an int.
@ line 7 | Input -> int in one line
After a blank line for tidiness, line seven asks how many people are eating and converts the answer to a whole number.
@ line 8 | The scale number
Line eight works out the scale: people divided by recipe serves.
@ line 10 | Output starts here
Line ten starts the output with a heading.
@ line 11-12 | Multiply each amount by scale
Lines eleven and twelve multiply the flour and the milk by the scale, right inside the F strings.
@ line 13 | round() = whole eggs
And line thirteen rounds the eggs, so we get a whole number.
@ run | 6 people: scale = 1.5
Let's run it for six people. Pancakes for six. Three cups of flour, two point two five cups of milk, and three eggs. Every amount was multiplied by one point five. Our scaler works!

## REVISE | Quick revise
@ point Plan with input, process, output
We planned with input, process and output.
@ point Constants for fixed values, variables for the rest
We used a constant for a fixed value, and variables for everything else.
@ point Convert input with int() before doing maths
We converted the input to a number before doing maths.
@ point round() gives the nearest whole number
And round gave us whole eggs.

## PRACTICE | Add an ingredient
@ task Add sugar to the scaler: the recipe uses 3 spoons of sugar for 4 people. Print the scaled sugar, rounded to a whole spoon.
Your turn. Add sugar to our scaler. The original recipe uses three spoons of sugar for four people. Add a variable for it, and print the scaled amount, rounded to a whole spoon.
@ hint One new variable near the top, one new print at the bottom.
Hint: you need one new variable near the top, and one new print line at the end.
@ pause 15
Pause the video and add the sugar.

## ANSWER | recipe_scaler.py
```python
RECIPE_SERVES = 4
sugar_spoons = 3
people = int(input("How many people are eating? "))
scale = people / RECIPE_SERVES
print(f"Sugar: {round(sugar_spoons * scale)} spoons")
```
@ input 6
@ line 1-2
Here are just the important lines. We add a sugar variable: three spoons.
@ line 3-4
The input and the scale stay the same.
@ line 5
And a new print rounds the scaled sugar.
@ run
For six people, three times one point five is four point five, which rounds to four spoons, because of banker's rounding. Well done if you added it to the full program!

## OUTRO
Congratulations, you've finished Module Two! You can store values, ask questions, do maths, compare things and write clean code. Next time, Module Three begins with lists, which let one variable hold a whole collection of things. Like, share and subscribe, and keep coding. Happy Learning!
