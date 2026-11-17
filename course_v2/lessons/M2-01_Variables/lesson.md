---
id: "2.1"
title: "Variables: Labelled Boxes"
module: 2
module_title: "Variables, Input and Output"
next: "Good Names and Constants"
minutes: 5.5   # rendered video length
thumb_code: 'score = 10'
goals: ["What a variable is", "Storing a value with =", "Changing a value", "Printing variables and text together"]
youtube:
  title: "Python Lesson 2.1: Variables Explained - Labelled Boxes | Introduction to Python"
  description: |
    Variables let your programs remember things. Pip the Python explains variables as labelled boxes, shows what the
    equals sign really means in Python, and how a value can change while the name stays the same.
    Code along line by line, then try the pet profile exercise.
    For beginners aged 7 to 20.
  tags: [python variables, variables for kids, learn python, python for beginners, assignment python, fun skill builders]
---

<!-- Booklet 2.1.1 Variables. Analogy: labelled storage box. -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Welcome to Module Two. So far our programs have only shown words. Today, they learn to remember things, using one of the most important ideas in all of programming: variables.

## STUDY | What is a variable?
@ point A variable is a labelled box that stores a value
Imagine a cardboard box with a label stuck on the front. The label says score, and inside the box is the number zero. That's a variable! The label is the variable's name, and the thing inside is its value.
@ boxes score = 0 | player = "Asha"
We can have lots of boxes, each with its own label. One box called score holds zero. Another called player holds the text Asha. Whenever we use the name, Python looks inside the box and uses whatever value it finds.
@ point Why bother? So programs can remember and reuse things
Why is this useful? Think of a game. It has to remember your score, your lives and your name, and it keeps changing them as you play. Variables are how programs remember things while they run.

## STUDY | The equals sign means store
@ snippet score = 0
Here's how we make a variable in Python. The name, an equals sign, then the value.
@ point = means "store this value in this box"
In maths, the equals sign means both sides are the same. In Python it means something different. It means: put the value on the right into the box on the left. A good way to read it aloud is: score gets zero.
@ point Right side first, then it goes into the left
Python always works out the right side first, and then stores the answer in the box on the left. So you could even write score gets five plus five, and the box would hold ten.
@ boxes score = 10
And here's the best part. A box can be emptied and refilled. If we later write score gets ten, the old zero is thrown away and ten goes in. The label stays the same, but the value changes. That's why it's called a variable: its value can vary.
@ point Level up: this is called assignment
Programmers call this assignment: we assign a value to a variable. Behind the scenes, Python stores the value in the computer's memory, and the name points to it, like a label pointing to a box on a shelf.

## CODE | variables.py
```python
score = 0
print(score)
score = 10
print(score)
player = "Asha"
print(player, "has", score, "points")
```
@ say
Let's try it. Type along with me, line by line.
@ line 1 | score gets 0
Line one creates a box called score and puts zero inside.
@ line 2 | No quotes: show what's IN the box
Line two prints score. Notice there are no quote marks. That means: don't show the word score, show what's inside the score box.
@ line 3 | Same box, new value
Line three puts ten in the same box. The zero is replaced.
@ line 4
And line four prints it again.
@ line 5 | Text values need quotes
Line five makes a new box called player, holding the text Asha. Text values still need quote marks.
@ line 6 | Commas join things in one print, with spaces
Line six shows something new. We can give print several things, separated by commas. Python shows them all on one line, with a space between each. Some are variables, and some are text in quotes.
@ run | Same name, different values over time
Let's run it. First zero, then ten: the same variable, showing different values at different moments. And the last line mixes variables and text: Asha has ten points.

## CODE | game_score.py
```python
coins = 0
print("Start:", coins)
coins = coins + 5
print("Found a treasure chest:", coins)
coins = coins - 2
print("Bought a snack:", coins)
```
@ say
Here's one more example, and it shows a pattern you'll use all the time: changing a variable using its own value.
@ line 1-2 | Start with 0 coins
We start a game with zero coins, and print it.
@ line 3 | Right side first: 0 + 5, then store
Line three looks strange at first: coins gets coins plus five. Remember, Python works out the right side first. It looks in the box, finds zero, adds five, and then puts the five back into the same box.
@ line 4
Then we print the new amount.
@ line 5-6 | Same idea, take away 2
Lines five and six spend two coins the same way: coins gets coins minus two.
@ run | 0 -> 5 -> 3
Run it. Zero, then five, then three. The box kept the same label the whole time, but its value went up and down, just like a real game score.

## REVISE | Quick revise
@ point A variable is a name for a stored value
A variable is a name that stores a value, like a labelled box.
@ point name = value  means "name gets value"
The equals sign means store: the name on the left gets the value on the right.
@ point A variable's value can change
You can change the value at any time, and the name stays the same.
@ point print(score) shows the value, print("score") shows the word
And print with the name shows the value, while print with quote marks shows the word itself.

## PRACTICE | Pet profile
@ task Make three variables: pet_name, pet_type and pet_age. Then print one sentence using all three, like: Bruno is a dog who is 3 years old
Your turn. Make three variables: pet name, pet type and pet age. Use a real pet, or invent one. Then print one sentence that uses all three, separated by commas.
@ hint pet_name = "Bruno"  ...  print(pet_name, "is a", ...)
Hint: text values need quote marks, but numbers don't. And when you print, put commas between each part.
@ pause 12
Pause the video now and try it.

## ANSWER | pet_profile.py
```python
pet_name = "Bruno"
pet_type = "dog"
pet_age = 3
print(pet_name, "is a", pet_type, "who is", pet_age, "years old")
```
@ line 1-2
Here's my answer. Two text variables, with quote marks.
@ line 3
One number variable, without quote marks.
@ line 4
Then one print that mixes variables and text, with commas in between.
@ run
And it says: Bruno is a dog who is three years old. Now try changing pet age to four and running it again. One small change, and the sentence updates by itself. That's the power of variables!

## OUTRO
Brilliant work! You can now make programs that remember things. Next time, we'll learn how to choose great names for variables, the rules Python insists on, and a special kind of variable called a constant. Like, share and subscribe, and keep coding. Happy Learning!
