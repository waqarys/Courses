---
id: "2.1"
title: "Variables: Labelled Boxes"
module: 2
module_title: "Variables, Input and Output"
next: "Good Names and Constants"
minutes: 8.85
thumb_code: 'score = 0'
goals: ["What a variable is", "= means store, not equals", "Changing a variable's value", "Printing variables with text"]
youtube:
  title: "Python Lesson 2.1: Variables - Labelled Boxes for Your Data | Introduction to Python"
  description: |
    Variables let a program remember things. Ziggy the Python explains variables as labelled boxes, why = means
    "store" and not "equals", how values change while a program runs, and how to print variables with text.
    We build a pet profile and a game score tracker line by line, predict outputs, and fix common mistakes.
    For beginners aged 7 to 20.
  tags: [python variables, variables for beginners, python assignment, python for kids, learn python, fun skill builders]
---

<!-- Booklet chapter 2: variables. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Welcome to Module Two. So far, our programs forget everything the moment they print it. Today, we'll give them a memory, using variables. Variables are in almost every program ever written, so this is a really important lesson.

## STUDY | What is a variable?
@ boxes name = "Asha" | age = 11 | pet = "cat"
A variable is like a box with a label on it. The label is the variable's name, and inside the box is a value. Here we have three boxes: one labelled name with Asha inside, one labelled age with eleven inside, and one labelled pet with the word cat inside.
@ point A variable = a name + a value
So a variable has two parts: a name and a value. The name lets us find the box later. The value is the thing we're storing.
@ point The value is stored in the computer's memory
Behind the scenes, the value is stored in the computer's memory, and Python keeps track of which label goes with which box. We never have to know where in the memory it is. We just use the name.
@ point Why bother? Store once, use many times
Why bother? Because you can store something once and use it many times. If your name appears in ten places in a program, you only need to change it in one place.

## STUDY | = means "store"
@ snippet age = 11
Here's how you make a variable in Python. The name, an equals sign, and the value.
@ point Read it as: "age stores 11"
In maths, the equals sign means two things are the same. In Python, it means store. So read this line as: age stores eleven. Or: put eleven into the box called age.
@ point The name always goes on the LEFT
The name always goes on the left, and the value on the right. Python works out the right hand side first, then puts the result into the box on the left.
@ point Making a variable is called assignment
Programmers call this assignment. We assign the value eleven to the variable age. The first time you assign a variable, Python creates the box.
@ point Change it later: age = 12
And you can put a new value into the box at any time. The old value is thrown away and replaced. That's why they're called variables: their values can vary, which means change.

## CODE | variables.py
```python
name = "Asha"
age = 11
pet = "cat"
print(name)
print("Hi,", name)
print(name, "is", age, "and has a", pet)
age = 12
print(name, "is now", age)
```
@ say
Let's build a little profile program, line by line.
@ line 1 | Store text: quotes, like before
Line one stores the string Asha in a variable called name. Text still needs quote marks.
@ line 2 | Store a number: no quotes
Line two stores the number eleven in age. Numbers don't need quotes.
@ line 3
And line three stores the word cat in pet.
@ predict 3 | Three lines of code. What will be printed?
Here's a question. We've written three lines. What will appear in the output if we run it now?
@ run | Nothing! Storing doesn't print
Run. Nothing at all! Storing a value doesn't show anything. The values are safely in their boxes, but we haven't asked Python to print them.
@ line 4 | No quotes: print what's IN the box
Line four prints name. Notice there are no quote marks. Without quotes, Python looks inside the box called name and prints what it finds.
@ line 5 | Text and a variable, with a comma
Line five prints the text Hi, then a comma, then the variable.
@ line 6 | Mix text and variables in one print
Line six mixes text and all three variables in one print, separated by commas.
@ run | Python swaps each name for its value
Run. Asha. Hi, Asha. Asha is eleven and has a cat. Every time Python sees a variable name, it swaps in the value from the box.
@ line 7 | Put a new value in the box
Now it's Asha's birthday. Line seven puts twelve into age. The eleven is replaced.
@ line 8
And line eight prints the new age.
@ run | The last value stored is the one used
Run. The last line says Asha is now twelve. The lines above still printed eleven, because when they ran, the box still held eleven. Python always uses the value that's in the box at that moment.

## CODE | game_score.py
```python
score = 0
print("Start:", score)
score = score + 10
print("Found a coin:", score)
score = score + 25
print("Beat a boss:", score)
lives = 3
lives = lives - 1
print("Lives left:", lives)
```
@ say
Here's a second example. Games use variables all the time, for scores, lives and levels.
@ line 1-2 | Start the score at 0
We start the score at zero and print it.
@ line 3 | Take the old value, add 10, store it back
Line three is very important, and it looks strange in maths. Score equals score plus ten. Remember, Python works out the right side first. It takes the old score, zero, adds ten, and stores the result back in the score box.
@ line 4
Then we print it.
@ line 5-6 | Add 25 to whatever is in the box
Line five adds twenty five to whatever is in the box now, and line six prints it.
@ predict 5 | What will the score be after the boss?
What will the score be after beating the boss? Work it out before the run.
@ run | 0, then 10, then 35
Run. Start, zero. Found a coin, ten. Beat a boss, thirty five. Ten plus twenty five.
@ line 7-8 | Subtract works the same way
Lives works the same way. We start with three lives, then lose one: lives equals lives minus one.
@ line 9
And print the lives left.
@ run | Two lives left
Run. Lives left: two. This pattern, take the old value, change it, store it back, is used in almost every game ever made.

## CODE | copy_boxes.py
```python
apples = 5
pears = apples
print(apples, pears)
apples = 10
print(apples, pears)
total = apples + pears
print("Total fruit:", total)
```
@ say
Here's a puzzle that even older students often get wrong. What happens when one variable is made from another?
@ line 1 | apples stores 5
Line one: apples stores five.
@ line 2 | pears gets a COPY of what's in apples
Line two: pears equals apples. Python looks in the apples box, finds five, and puts five into the pears box as well.
@ line 3
Line three prints both.
@ line 4 | Change apples only
Now line four changes apples to ten.
@ line 5 | Print both again
And line five prints both again.
@ predict 6 | Will pears change to 10 as well?
Here's the puzzle. Pears was made from apples. So when apples changes to ten, does pears change too? Pause and decide.
@ run | pears keeps its own 5
Run. First line, five and five. Second line, ten and five! Pears did not change. Line two copied the value five into pears at that moment. After that, the two boxes are completely separate. Changing one box doesn't touch the other.
@ line 6 | Make a new variable from a calculation
Line six makes a new variable, total, from a calculation: apples plus pears.
@ line 7
And line seven prints it.
@ run | 10 + 5 = 15
Run. Total fruit, fifteen. Ten apples plus five pears. You can store the result of any calculation in a variable, and use it again later.

## STUDY | Variables are everywhere
@ table App | Some of its variables ; a game | score, lives, level, player_name ; a music app | song_title, volume, is_playing ; a weather app | city, temperature, chance_of_rain ; a school app | student_name, homework_due
Variables are in every app you use. A game remembers your score, lives, level and name. A music app remembers the song title and the volume. A weather app stores the city and the temperature. When you look at any app now, try to imagine the labelled boxes hiding inside it, and how their values change as you use it.
@ point Values change while the program runs
Notice that most of these change while the app runs. The volume goes up and down. The score goes up. That's exactly what variables are for.

## STUDY | Common mistakes
@ table Code | What goes wrong ; print("name") | prints the word name, not the value ; print(nme) | NameError: a typo in the name ; print(score) before score = 0 | NameError: the box doesn't exist yet ; 10 = score | SyntaxError: the name must be on the left
Let's look at four common mistakes. Putting quotes around a variable name prints the word itself, not the value inside. A spelling mistake in the name gives a NameError, because there's no box with that label. Using a variable before you've created it also gives a NameError, because Python runs from top to bottom. And writing the value on the left, like ten equals score, is a SyntaxError. The name always goes on the left.

## REVISE | Quick revise
@ point A variable is a labelled box: name + value
A variable is a labelled box with a name and a value.
@ point = means store: the name goes on the left
The equals sign means store, and the name goes on the left.
@ point No quotes around a name: Python uses the value
Without quotes, Python uses the value inside the box.
@ point score = score + 10 updates a value
And score equals score plus ten updates the value in the box.

## PRACTICE | Pet profile
@ task Make a pet profile:\n1. Variables for a pet's name, type and age\n2. Print one sentence using all three\n3. Add 1 to the age (a birthday!) and print the new age
Your turn. Make a pet profile for a real or imaginary pet. Store its name, what kind of animal it is, and its age, in three variables. Print one sentence that uses all three. Then the pet has a birthday: add one to the age, and print the new age.
@ hint pet_age = pet_age + 1 updates the age. Use commas in print.
Hint: to add one to the age, use the age equals age plus one pattern. And use commas to mix text and variables in print.
@ pause 15
Pause the video and try it.

## ANSWER | pet_profile.py
```python
pet_name = "Biscuit"
pet_type = "dog"
pet_age = 4
print(pet_name, "is a", pet_type, "aged", pet_age)
pet_age = pet_age + 1
print("Happy birthday!", pet_name, "is now", pet_age)
```
@ line 1-3
Here's my answer. Three variables: Biscuit, dog, and four.
@ line 4
One sentence using all three.
@ line 5-6
Then the birthday. Age equals age plus one, and print the new age.
@ run
Run. Biscuit is a dog aged four. Happy birthday! Biscuit is now five. If yours works, fantastic. You've just built a program with a memory.

## OUTRO
Brilliant work! You now know what variables are and how to change them. Next time, we'll learn the rules for naming variables, and how to choose names that make your code easy to read. Like, share and subscribe, and keep coding. Happy Learning!
