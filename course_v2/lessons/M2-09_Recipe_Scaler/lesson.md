---
id: "2.9"
title: "Mini-Project: Recipe Scaler"
module: 2
module_title: "Variables, Input and Output"
next: "Lists: Many Things in One Box"
minutes: 8.99
thumb_code: 'scale = people / SERVES'
goals: ["Plan a real program", "Constants, variables and input together", "Maths with floats", "round() for neat answers"]
youtube:
  title: "Python Lesson 2.9: Mini-Project - Pancake Recipe Scaler | Introduction to Python"
  description: |
    Module 2 mini-project! Ziggy the Python builds a recipe scaler that works out pancake ingredients for any number of
    people, using constants, variables, input, int, float maths, round and f-strings, all planned with comments.
    Then you add a new ingredient yourself.
    For beginners aged 7 to 20.
  tags: [python project for beginners, python recipe calculator, python input int, round python, learn python, fun skill builders]
---

<!-- Booklet 2.7.2 pancake recipe calculator (idea only; code and wording original). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. It's mini project time! We're going to build a recipe scaler. You tell it how many people are eating, and it works out exactly how much of each ingredient you need. We'll build it in stages, test it like real programmers, and even find and fix a bug that the first version hides. Let's make some pancakes!

## STUDY | The problem
@ point A recipe serves 4. But what if 6 people are hungry?
Our pancake recipe serves four people. It needs two cups of flour, one and a half cups of milk, and two eggs. But what if six people are hungry? Or ten? Or just one? Working it out by hand every time is slow, and it's easy to make mistakes.
@ flow Input: how many people? > Process: scale every ingredient > Output: the new amounts
Let's plan with input, process, output. Input: ask how many people are eating. Process: scale every ingredient. Output: show the new amounts.
@ point Scale = people ÷ people the recipe serves
The secret is a scale number. Divide the number of people eating by the number the recipe serves. For six people, that's six divided by four, which is one point five. Then multiply every ingredient by one point five. For two people, the scale is a half, so everything halves.
@ point Build in stages, test after each one
And we'll build it in stages. Version one with a fixed number of people. Version two that asks the user. Then we'll test it with different numbers, and improve it.

## STUDY | Tools we'll use
@ table Tool | Job in our program ; RECIPE_SERVES = 4 | a constant ; input() + int() | ask for people ; / and * | the scaling maths ; round() | tidy numbers, whole eggs ; f-strings | neat output
This project uses almost everything from Module Two. A constant for the number the recipe serves, because that never changes. Input and int to ask for the number of people. Division and multiplication for the scaling. Round to tidy up numbers. And F strings for neat output.
@ snippet round(4.5)  # 4
round(2.678, 1)  # 2.7
Round turns a decimal into the nearest whole number. And if you give it a second number, it rounds to that many decimal places.
@ point Level up: Python rounds exact halves to the even number
A detail for the curious: when a number is exactly halfway, Python rounds to the nearest even number. So round of two point five is two, and round of three point five is four. This is called banker's rounding, and it keeps big totals fair.

## CODE | scaler_v1.py
```python
# Pancake recipe scaler - version 1
RECIPE_SERVES = 4
flour_cups = 2.0
people = 6
scale = people / RECIPE_SERVES
print("Scale:", scale)
print("Flour:", flour_cups * scale, "cups")
```
@ say
Version one. Just one ingredient, and a fixed number of people, so we can check the maths works.
@ line 1 | A title comment
A title comment first.
@ line 2 | The recipe always serves 4: a constant
Line two is our constant. The recipe always serves four.
@ line 3 | The original flour
Line three stores the original flour: two cups.
@ line 4 | Fixed for now: 6 people
For now, we fix the number of people at six.
@ line 5 | The scale number
Line five works out the scale.
@ line 6-7 | Check the scale, then the flour
Line six prints the scale, so we can check it, and line seven prints the scaled flour.
@ predict 5 | Scale for 6 people? How much flour?
What will the scale be? And how many cups of flour for six people?
@ run | Smoke test: 1.5 and 3.0 cups
Run. Scale: one point five. Flour: three point zero cups. Two cups times one point five is three. The maths works, so we can build on it.

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
@ say
Version two: all three ingredients, and the program asks how many people are eating.
@ line 1 | What the program is
A title comment.
@ line 2 | Constant = never changes
The constant.
@ line 3-5 | The original amounts
Lines three to five store the original amounts. Flour and milk are floats, and eggs is an int.
@ line 7 | Input -> int in one line
After a blank line for tidiness, line seven asks how many people are eating and converts the answer to a whole number.
@ line 8 | The scale number
Line eight works out the scale.
@ line 10 | Output starts here
Line ten starts the output with a heading.
@ line 11-12 | Multiply each amount by scale
Lines eleven and twelve multiply the flour and the milk by the scale, right inside the F strings.
@ line 13 | round() = whole eggs
And line thirteen rounds the eggs, because you can't crack half an egg.
@ run | 6 people: scale = 1.5
Let's run it for six people. Pancakes for six. Three cups of flour, two point two five cups of milk, and three eggs. Every amount was multiplied by one point five.

## CODE | test_one_person.py
```python
RECIPE_SERVES = 4
eggs = 2
people = 1
scale = people / RECIPE_SERVES
print("Eggs:", round(eggs * scale))
```
@ say
Now, real programmers don't just test the easy case. They try unusual values too. What about pancakes for just one person?
@ line 1-3 | Test with just 1 person
Here's the egg part on its own, with people set to one.
@ line 4-5
The same scale and the same rounding.
@ predict 6 | 1 person: scale 0.25. How many eggs?
For one person, the scale is zero point two five. Two eggs times zero point two five is half an egg. What will round give us?
@ run | Bug: zero eggs!
Run. Eggs: zero! Half an egg rounds to zero, because of banker's rounding. Pancakes with no eggs at all. That's a bug, and our first test with six people would never have found it.
@ edit 5 => print("Eggs:", (eggs * people + RECIPE_SERVES - 1) // RECIPE_SERVES)
Let's fix it with the round up trick from the pizza party lesson. Eggs times people, plus three, floor divided by four. This always rounds up to the next whole egg.
@ run | Round UP: at least 1 egg
Run. Eggs: one. Much better. And for six people, it gives twelve plus three, which is fifteen, floor divided by four, which is three eggs, just like before. Testing with an unusual value found a real bug.

## CODE | tidy_output.py
```python
RECIPE_SERVES = 4
milk_cups = 1.5
people = 5
scale = people / RECIPE_SERVES
milk = milk_cups * scale
print(f"Milk: {milk} cups")
print(f"Milk: {round(milk, 1)} cups")
print(f"Scale used: {scale}")
```
@ say
One more improvement. Some amounts come out with lots of decimal places, which looks messy on a recipe card. Let's try five people.
@ line 1-4 | Five people this time
The same constant and milk, but now five people, so the scale is five divided by four.
@ line 5 | Store the scaled milk in a variable
This time we store the scaled milk in its own variable, so we can use it twice.
@ line 6 | Print it exactly
Line six prints the milk exactly as it is.
@ line 7 | round(milk, 1): one decimal place
Line seven rounds it to one decimal place first.
@ line 8
And line eight shows the scale we used.
@ predict 6 | 1.5 × 1.25 = ? And rounded to 1 place?
One point five times one point two five. What's the exact answer, and what is it rounded to one decimal place?
@ run | 1.875 → 1.9 cups
Run. Milk: one point eight seven five cups. Then milk: one point nine cups, which is much easier to measure. And the scale was one point two five. Nobody has a measuring cup marked in thousandths, so rounding to one decimal place makes the program more useful for real cooks.

## STUDY | Make it your own
@ point Change the recipe: biscuits, smoothies, pizza dough
Here are some ideas to take this project further. Change the recipe to something you actually like making: biscuits, a smoothie, or pizza dough. Only the constant and the ingredient variables need to change.
@ point Ask for the recipe's servings too
You could also ask the user how many people the original recipe serves, instead of fixing it at four. Then it works for any recipe at all.
@ point Print a neat card with a border
And use what you learned in Module One to print a neat recipe card, with a border made of repeated characters around the ingredients.

## STUDY | Common mistakes
@ table Mistake | What happens ; forgot int() on the input | TypeError: text / number ; scale = 4 / people | upside down: more people, less food! ; round(x) on milk | 2.25 becomes 2: use round(x, 2) or leave it ; only testing one value | bugs hide in unusual cases
Let's review the mistakes people make with this project. Forgetting to convert the input gives a TypeError. Dividing the wrong way round makes the food shrink as more people arrive. Rounding the milk to a whole number throws away useful detail. And only testing with one value lets bugs hide, just like our zero eggs.

## REVISE | Quick revise
@ point Plan with input, process, output
We planned with input, process and output.
@ point Build in stages and smoke test each one
We built the program in stages, and tested each one.
@ point Constants for fixed values; convert input before maths
We used a constant for a fixed value, and converted the input before doing maths.
@ point Test unusual values too: they find hidden bugs
And testing an unusual value found a hidden bug.

## PRACTICE | Add an ingredient
@ task Add sugar to the scaler: the recipe uses 3 spoons of sugar for 4 people. Print the scaled sugar, rounded to a whole spoon. Test it with 6 people and with 1 person.
Your turn. Add sugar to our scaler. The original recipe uses three spoons of sugar for four people. Add a variable for it, and print the scaled amount, rounded to a whole spoon. Then test it with six people and with one person.
@ hint One new variable near the top, one new print at the bottom.
Hint: you need one new variable near the top, and one new print line at the end.
@ pause 15
Pause the video and add the sugar.

## ANSWER | add_sugar.py
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
For six people, three times one point five is four point five, which rounds to four spoons, because of banker's rounding. For one person, it's zero point seven five, which rounds to one spoon. Well done if you added it to the full program and tested both!

## OUTRO
Congratulations, you've finished Module Two! You can store values, ask questions, do maths, compare things and write clean code. Next time, Module Three begins with lists, which let one variable hold a whole collection of things. Like, share and subscribe, and keep coding. Happy Learning!
