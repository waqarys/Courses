---
id: "2.7"
title: "True or False?"
module: 2
module_title: "Variables, Input and Output"
next: "Comments and Clean Code"
minutes: 8.43
thumb_code: 'print(12 > 10)  # True'
goals: ["The bool type: True and False", "Comparing with == != < >", "= versus ==", "and, or, not + truth tables"]
youtube:
  title: "Python Lesson 2.7: Booleans, Comparisons and Logic (and, or, not) | Introduction to Python"
  description: |
    Every decision a computer makes comes down to True or False. Ziggy the Python explains booleans, the six comparison
    operators, the difference between = and ==, and how and, or and not combine conditions, with truth tables.
    Then you write a check for a warm day.
    For beginners aged 7 to 20.
  tags: [python boolean, true false python, comparison operators, logical operators, truth table, learn python, fun skill builders]
---

<!-- Booklet 2.2.4 Boolean, 2.2.5 Truth tables; 4.2.1 logical operators review. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Today's values are the simplest of all. They can only be one of two things: True or False. But don't be fooled. These two little values are behind every decision a computer ever makes.

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
@ predict 7 | Predict all five: True or False?
Before we run, go through the five print lines and predict True or False for each one. Write them down if you like.
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

## CODE | compare_more.py
```python
print("apple" < "banana")
print("Zebra" < "apple")
print("5" == 5)
print(7 != 7.0)
```
@ say
Comparisons can surprise you. Let's test a few tricky ones and predict each answer.
@ line 1 | Comparing words: alphabetical order
Line one asks if the word apple is less than the word banana. With strings, less than means: comes earlier in alphabetical order.
@ line 2 | A capital letter vs a small letter
Line two compares Zebra, with a capital Z, to apple, with a small a.
@ line 3 | Text vs number
Line three asks if the string five equals the number five.
@ line 4 | int vs float
And line four asks if seven is not equal to seven point zero.
@ predict 7 | Four questions: predict each answer
Here's the challenge. Predict all four. Line two is the trickiest.
@ run | True, True, False, False
Run. Apple comes before banana: True. Zebra comes before apple: True! That's because Python compares letters by their computer codes, and all the capital letters come before all the small letters. So when you compare words, it's often a good idea to use dot lower on both first. The string five and the number five are not equal: False. Text is never equal to a number. And seven is equal to seven point zero, so asking if they're different gives False.

## CODE | ride_check.py
```python
age = 7
height = 125
with_adult = True
tall_enough = height >= 120
old_enough = age >= 8 or with_adult
print("Tall enough:", tall_enough)
print("Old enough:", old_enough)
print("Can ride:", tall_enough and old_enough)
```
@ say
Let's use booleans for something real: the rules for a theme park ride. The rules are: you must be at least one hundred and twenty centimetres tall, and either at least eight years old, or riding with an adult.
@ line 1-3 | The rider's details
Our rider is seven years old, one hundred and twenty five centimetres tall, and is with an adult.
@ line 4 | Store a comparison in a named boolean
Line four stores the answer to a comparison in a variable called tall enough. Giving a boolean a clear name makes the rules easy to read.
@ line 5 | 8 or older, OR with an adult
Line five works out old enough: age at least eight, or with an adult.
@ line 6-7
Lines six and seven print both.
@ line 8 | Both rules together
And line eight combines them with and.
@ predict 6 | Seven years old, but with an adult. Can they ride?
Our rider is only seven, but they're with an adult. Can they ride? Think it through using the rules.
@ run | Tall enough AND (old enough OR with an adult)
Run. Tall enough: True. Old enough: True, because even though age is not at least eight, with adult is True, and or only needs one. Can ride: True. Splitting a big rule into small, well named booleans like this is how programmers keep complicated rules readable.

## STUDY | Common mistakes
@ table Mistake | Fix ; age = 12 when you mean to compare | use == to compare ; "True" in quotes | True is a value, not text ; true or TRUE | it must be True with a capital T only ; 10 < age < 5 | impossible range: check the order of your numbers
Here are the mistakes to watch out for. Using one equals sign when you mean to compare. Putting True in quotes, which makes it a string, not a boolean. Writing true with a small t, which Python doesn't know. And writing an impossible range with the numbers the wrong way round, which is always False.

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
