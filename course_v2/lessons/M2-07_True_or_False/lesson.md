---
id: "2.7"
title: "True or False?"
module: 2
module_title: "Variables, Input and Output"
next: "Comments and Clean Code"
minutes: 5.4   # rendered video length
thumb_code: 'print(12 > 10)  # True'
goals: ["The bool type: True and False", "Comparing with == != < >", "= versus ==", "and, or, not + truth tables"]
youtube:
  title: "Python Lesson 2.7: Booleans, Comparisons and Logic (and, or, not) | Introduction to Python"
  description: |
    Every decision a computer makes comes down to True or False. Pip the Python explains booleans, the six comparison
    operators, the difference between = and ==, and how and, or and not combine conditions, with truth tables.
    Then you write a check for a warm day.
    For beginners aged 7 to 20.
  tags: [python boolean, true false python, comparison operators, logical operators, truth table, learn python, fun skill builders]
---

<!-- Booklet 2.2.4 Boolean, 2.2.5 Truth tables; 4.2.1 logical operators review. -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Today's values are the simplest of all. They can only be one of two things: True or False. But don't be fooled. These two little values are behind every decision a computer ever makes.

## STUDY | Yes or no values
@ point bool: a value that is True or False
In Python, a value that can only be True or False is called a boolean, or bool for short. It's named after George Boole, a mathematician who studied the logic of true and false, long before computers existed.
@ point Like a light switch: on or off
Think of a light switch. It's either on or off. There's no in between. Is it raining? Is the game over? Is the password correct? Each of these questions has a yes or no answer, a perfect job for a boolean.
@ snippet game_over = False
You can store a boolean in a variable, just like a number or a string. Notice that True and False start with capital letters and have no quote marks. They're special Python words.

## STUDY | Comparisons
@ table Operator | Asks ; == | equal to? ; != | not equal to? ; < | less than? ; > | greater than? ; <= | less than or equal? ; >= | greater than or equal?
A comparison asks a question about two values, and the answer is always True or False. Two equals signs ask: are these equal? An exclamation mark and an equals sign ask: are these different? And then we have less than, greater than, and the "or equal" versions.
@ point = stores. == compares.
Here's the number one beginner mix-up. One equals sign stores a value in a variable. Two equals signs compare two values. Score gets ten, versus: is score equal to ten?

## STUDY | and, or, not
@ table A | B | A and B | A or B ; True | True | True | True ; True | False | False | True ; False | True | False | True ; False | False | False | False
Sometimes we need to combine questions. And is True only when both sides are True. You can play outside if your homework is done and it's not dark. Or is True when at least one side is True. You'll get wet if it's raining or someone splashes you. This grid is called a truth table. It shows every possible combination.
@ point not flips it: not True is False
And not simply flips a value. Not True is False, and not False is True.
@ point Level up: 20 <= temp <= 35 checks a range in one go
A neat Python trick: you can chain comparisons. Twenty is less than or equal to temp, which is less than or equal to thirty five. That checks if a temperature is inside a range, in one tidy line.

## CODE | true_false.py
```python
age = 12
print(age > 10)
print(age == 15)
is_raining = False
has_umbrella = True
print(is_raining and has_umbrella)
print(is_raining or has_umbrella)
print(not is_raining)
```
@ line 1
Line one stores an age of twelve.
@ line 2 | Is 12 greater than 10?
Line two asks: is age greater than ten?
@ line 3 | == compares, it doesn't store
Line three asks: is age equal to fifteen? Two equals signs, because we're comparing, not storing.
@ line 4-5 | Booleans: capital T and F, no quotes
Lines four and five store two booleans: it is not raining, and we do have an umbrella.
@ line 6 | and: BOTH must be True
Line six asks: is it raining and do we have an umbrella? Both must be true.
@ line 7 | or: at least ONE must be True
Line seven uses or: at least one must be true.
@ line 8 | not flips the value
And line eight flips is raining with not.
@ run | Comparisons always answer True or False
Let's run it. Twelve is greater than ten: True. Twelve is not fifteen: False. Raining and umbrella: False, because it isn't raining. Raining or umbrella: True, because we have the umbrella. And not raining: True.

## CODE | password.py
```python
secret = "mango42"
guess = input("Password? ")
print(guess == secret)
print(len(guess) >= 6)
print(guess == secret and len(guess) >= 6)
```
@ input mango42
@ say
Comparisons work with text too. Let's check a password.
@ line 1-2 | Compare text with ==
We store a secret password, and ask the user to type a guess.
@ line 3 | Exactly the same? Capitals count!
Line three asks: is the guess exactly the same as the secret? Every letter must match, and capitals count.
@ line 4 | Long enough?
Line four checks the guess is at least six characters long.
@ line 5 | Both together with and
And line five combines both checks with and.
@ run | Correct AND long enough
Run it, and type mango forty two. True, true, and true. If you typed Mango with a capital M, the first check would be False. Soon we'll use answers like these to let the program decide what to do next.

## REVISE | Quick revise
@ point bool values: True and False (capitals, no quotes)
Booleans are True and False, with capital letters and no quotes.
@ point == != < > <= >= compare and give a bool
Comparison operators always give a True or False answer.
@ point = stores, == compares
One equals sign stores, two equals signs compare.
@ point and: both. or: at least one. not: flip.
And needs both, or needs at least one, and not flips the value.

## PRACTICE | Warm day checker
@ task temperature = 30\nPrint True if the temperature is from 20 to 35 (a warm day), otherwise False. Test it with 30, then with 40.
Your turn. Make a variable called temperature and set it to thirty. Print True if it's a warm day, which means from twenty up to thirty five. Then change it to forty and check you get False.
@ hint temperature >= 20 and temperature <= 35
Hint: you need two comparisons, joined with and.
@ pause 15
Pause the video and give it a try.

## ANSWER | warm_day.py
```python
temperature = 30
print(temperature >= 20 and temperature <= 35)
```
@ line 1
We store a temperature of thirty.
@ line 2
Then we check: is it at least twenty, and at most thirty five?
@ run
True! Now let's test it with forty.
@ edit 1 => temperature = 40
We change the temperature to forty.
@ run
False, because forty is too hot. Testing with different values like this is how programmers make sure their code is right. And if you used the chained version, twenty less than or equal to temperature less than or equal to thirty five, that's correct too.

## OUTRO
Awesome! You now speak the language of logic. Very soon, we'll use True and False to make programs choose what to do. But first, next time, we'll learn how to leave helpful notes in our code with comments. Like, share and subscribe, and keep coding. Happy Learning!
