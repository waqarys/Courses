---
id: "2.5"
title: "Numbers: int and float"
module: 2
module_title: "Variables, Input and Output"
next: "Maths with Python"
minutes: 8.8
thumb_code: 'age = int(input())'
goals: ["Whole numbers (int)", "Decimal numbers (float)", "Checking a type with type()", "Converting with int(), float() and str()"]
youtube:
  title: "Python Lesson 2.5: Numbers in Python - int, float and Type Conversion | Introduction to Python"
  description: |
    Python has different kinds of numbers. Ziggy the Python explains integers and floats, how to check the type of any value,
    and how to convert text from input into a real number with int and float. We fix last lesson's TypeError
    line by line, then you build a pet calculator.
    For beginners aged 7 to 20.
  tags: [python int float, type conversion python, python numbers, data types python, learn python, fun skill builders]
---

<!-- Booklet 2.2 Data types, 2.2.2 Numeric data types. Date/time (2.2.3) moves to lesson 5.3 (modules). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Last time, Python refused to add one to our age, because the age was text. Today we'll fix that. We'll meet Python's two main kinds of numbers and learn how to turn text into numbers and back again.

## STUDY | Kinds of values
@ point Every value has a type
Every value in Python has a type. The type tells Python what kind of thing the value is, and what you can do with it. You can add numbers, and you can make text upper case, but you can't make a number upper case.
@ table Value | Type | Kind ; "hello" | str | text (string) ; 7 | int | whole number ; 3.5 | float | decimal number ; True | bool | yes or no
So far we've met strings, which Python calls s t r. Today we meet two kinds of numbers: int and float. And next lesson we'll meet bool, for true and false.
@ point int: whole numbers like 7, 0 and -3
An int, short for integer, is a whole number with no decimal point. Like the number of people in your class, or the number of goals in a match. You can't have half a person!
@ point float: numbers with a decimal point, like 1.42
A float is a number with a decimal point, like your height in metres, or the price of an ice cream. It's called a float because the decimal point can float to different places in the number.

## STUDY | Converting between types
@ snippet age = int("11")
To turn text into a number, we use conversion functions. int turns text into a whole number. float turns text into a decimal number. And str turns a number back into text.
@ flow "11" (text) > int( ) > 11 (number)
Think of int as a machine. You put the text eleven in one end, and out comes the real number eleven, ready for maths.
@ point type(value) tells you the type
And if you're ever unsure what type something is, the type function will tell you.
@ point Level up: int("eleven") fails. int("3.5") fails too.
Conversion only works when it makes sense. int can't understand the word eleven spelled out in letters, and it won't accept a decimal point either. Both cause a ValueError. For decimal text, use float instead.

## CODE | numbers.py
```python
age_text = input("How old are you? ")
age = int(age_text)
print(type(age_text), type(age))
next_year = age + 1
print(f"Next year you will be {next_year}.")
height = 1.42
print(type(height))
```
@ input 11
@ line 1 | input() gives text
Line one asks for an age. Remember, the answer arrives as text, so let's call the variable age text.
@ line 2 | int() turns text into a whole number
Line two passes age text into int, and stores the real number in a variable called age.
@ line 3 | Check both types
Line three prints the type of each one, so we can see the difference.
@ line 4 | Now maths works!
Line four adds one to age. This time it's a real number, so the maths will work.
@ line 5
Line five shows the answer in an F string.
@ line 6 | A decimal = float
Line six stores a height with a decimal point.
@ line 7
And line seven prints its type.
@ run | str -> int, then maths works
Run it, and type eleven. The first line of output says class str, then class int. Same eleven, two different types. Next year you will be twelve. The error from last lesson is gone! And the height is a float.

## CODE | shopping.py
```python
price_text = input("Price of one ice cream? ")
price = float(price_text)
count = 3
total = price * count
print(f"{count} ice creams cost {total}")
print("As text: " + str(total))
```
@ input 2.5
@ say
Now an example with decimals, using float.
@ line 1 | The answer is text again
We ask for the price of one ice cream. The answer arrives as text.
@ line 2 | float() for decimal numbers
This time we use float, because prices can have a decimal point. int would fail on two point five.
@ line 3-4 | float * int = float
Three ice creams, and the total is price times count. A float times an int gives a float.
@ line 5
We show the total in an F string.
@ line 6 | str() turns a number back into text
And line six joins the total to some text with a plus. That only works if both sides are text, so str turns the number back into a string.
@ run | 2.5 * 3 = 7.5
Run it, and type two point five. Three ice creams cost seven point five. Text into a number with float, maths, and back into text with str. You've just used all three conversion functions!

## CODE | type_detective.py
```python
print(type(5))
print(type(5.0))
print(type("5"))
print(type(10 / 2))
print(5 == 5.0)
```
@ say
Time to be a type detective. For each line, try to predict the type before Python tells us.
@ line 1 | A whole number
Line one: the type of five.
@ line 2 | A decimal point
Line two: the type of five point zero.
@ line 3 | In quote marks
Line three: the type of five in quote marks.
@ line 4 | The result of a division
Line four: the type of ten divided by two.
@ predict 6 | int, float or str? Decide for each line
Pause and decide: int, float or s t r, for each of the four lines.
@ run | int, float, str, float
Run. Five is an int. Five point zero is a float, because of the decimal point, even though it's a whole number. Five in quotes is a string. And ten divided by two is a float! Python's normal division always gives a float, even when the answer is whole, so the answer is five point zero.
@ line 5 | Are 5 and 5.0 equal?
One last question. Line five asks whether five is equal to five point zero. The double equals sign means: is this the same as? We'll learn all about it in lesson two point seven.
@ run | True: same value, different types
Run. True. They have different types, but they have the same value.

## CODE | conversions.py
```python
print(int(3.7))
print(int(float("3.7")))
print(float(5))
print(str(42) + "!")
print(int("007") + 1)
```
@ say
Let's practise converting, with some surprises along the way.
@ line 1 | int() of a float: what happens to .7?
Line one turns the float three point seven into an int.
@ line 2 | Text with a decimal: float first, then int
Line two has text with a decimal point. int can't read that directly, so we convert it to a float first, and then to an int.
@ line 3 | float() of a whole number
Line three turns the whole number five into a float.
@ line 4 | str() so we can join with +
Line four turns forty two into text, so it can be joined to an exclamation mark.
@ line 5 | Leading zeros in text
And line five converts the text zero zero seven into a number, and adds one.
@ predict 7 | Does int(3.7) round up to 4?
Here's the big question. Does int of three point seven round up to four? And what happens to the zeros in zero zero seven?
@ run | int() chops off the decimals, it doesn't round
Run. Three! int doesn't round, it simply chops off everything after the decimal point. If you want proper rounding, use the round function instead. The second line also gives three. Then five point zero, forty two with an exclamation mark, and eight, because the leading zeros simply disappear when text becomes a number. Secret agents beware!

## CODE | value_error.py
```python
age = int(input("How old are you? "))
print(f"In 5 years you will be {age + 5}.")
```
@ input eleven
@ say
Now let's see what happens when a conversion goes wrong, because users don't always type what we expect.
@ line 1 | input inside int: one line
Line one asks for an age and converts it to an int, all in one line.
@ line 2
Line two works out the age in five years.
@ predict 5 | What if the user types the WORD eleven?
This time, the user types the word eleven, spelled out with letters. What will happen?
@ run | ValueError: int() can't read words
Run. ValueError: invalid literal for int. That's Python's way of saying: I can't turn this text into a whole number. int only understands digits. A ValueError means the type was right, it was a string, but the value inside it didn't make sense.
@ say | Type digits: 11, not eleven
If the user types the digits one one instead, the program works: in five years you will be sixteen. Try both in your own editor. In Module Four, we'll learn how to check an answer before converting it, so the program can politely ask again instead of crashing.

## STUDY | Common mistakes
@ table Code | What goes wrong ; input("Age? ") + 1 | TypeError: text + number ; int("3.5") | ValueError: use float() for decimals ; int("eleven") | ValueError: digits only ; "Total: " + 7.5 | TypeError: use str() or an f-string
Here are the number mistakes you'll meet most. Forgetting to convert an input answer gives a TypeError when you do maths. int can't read a decimal point or a word, so both give a ValueError. And joining a number to text with plus needs str, or better, an F string.

## REVISE | Quick revise
@ point int = whole numbers, float = decimals, str = text
int is for whole numbers, float is for decimals, and s t r is for text.
@ point type(x) tells you a value's type
The type function tells you the type of any value.
@ point int("11") and float("1.5") turn text into numbers
int and float turn text into numbers, so you can do maths.
@ point Wrap input() with int() when you need a number
So whenever you ask for a number with input, convert it before doing maths.

## PRACTICE | Pet calculator
@ task Ask how many pets the user has. Then print how many pets they would have if the number doubled, like: Double trouble: 6 pets!
Your turn. Ask the user how many pets they have. Then print how many they would have if the number doubled. In Python, times is the star symbol.
@ hint pets = int(input("...")) does both steps in one line!
Hint: you can put input inside int, all on one line. Python works from the inside out: first it asks the question, then it converts the answer.
@ pause 12
Pause the video and try it.

## ANSWER | pets.py
```python
pets = int(input("How many pets do you have? "))
print(f"Double trouble: {pets * 2} pets!")
```
@ input 3
@ line 1
One line does it all. input asks the question, and int converts the answer into a number.
@ line 2
Then an F string with the maths right inside the curly brackets: pets times two.
@ run
Run it, and type three. Double trouble: six pets! If you did it in two lines, with a separate conversion, that's perfectly correct too.

## OUTRO
Excellent! You now understand types, the secret behind so many beginner errors. Next time, we'll turn Python into a super calculator, with division, remainders, powers and the order of operations. Like, share and subscribe, and keep coding. Happy Learning!
