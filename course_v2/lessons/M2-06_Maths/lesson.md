---
id: "2.6"
title: "Maths with Python"
module: 2
module_title: "Variables, Input and Output"
next: "True or False?"
minutes: 5.0   # rendered video length
thumb_code: '17 // 5   # 3'
goals: ["The 7 maths operators", "/ versus //", "Remainders with %", "Order of operations and brackets"]
youtube:
  title: "Python Lesson 2.6: Maths Operators - Division, Remainder, Powers | Introduction to Python"
  description: |
    Python is a super calculator. Pip the Python explains all seven arithmetic operators with a sharing-sweets story:
    normal division, whole-number division, remainders and powers, plus the order of operations and brackets.
    Then you convert minutes into hours and minutes.
    For beginners aged 7 to 20.
  tags: [python operators, python maths, modulo python, floor division, learn python, python for kids, fun skill builders]
---

<!-- Booklet 2.3 Arithmetic operations. -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Today, Python becomes your super calculator. We'll learn all seven maths operators, including two that might be new to you, and find out why brackets can completely change an answer.

## STUDY | The maths operators
@ table Symbol | Meaning | Example ; + | add | 5 + 2 = 7 ; - | subtract | 5 - 2 = 3 ; * | multiply | 5 * 2 = 10 ; / | divide | 5 / 2 = 2.5 ; ** | power | 5 ** 2 = 25
Here are the operators you'll use most. Plus adds. Minus subtracts. The star multiplies. The slash divides. And two stars mean to the power of, so five, two stars, two, means five times five, which is twenty five.
@ point / always gives a float, even 10 / 2 = 5.0
One thing to notice: a single slash always gives a decimal answer, a float. Even ten divided by two gives five point zero.

## STUDY | Sharing sweets
@ point 17 sweets shared between 5 friends...
Now for the two new operators. Imagine you have seventeen sweets to share equally between five friends. No cutting sweets in half!
@ snippet 17 // 5   # 3 each
Each friend gets three sweets, because five times three is fifteen. Two slashes do exactly this. It's called floor division: divide, then throw away anything after the decimal point.
@ snippet 17 % 5    # 2 left over
And how many sweets are left over? Two. The percent sign gives you the remainder. It's called modulo. It's surprisingly useful. For example, a number is even if its remainder when divided by two is zero.
@ point Order: brackets, powers, * and /, then + and -
When there are several operators in one line, Python follows the same order you learn in maths class: brackets first, then powers, then multiply and divide, and finally add and subtract. Some people remember this as BODMAS or PEMDAS.
@ point Level up: brackets make your meaning clear
Even when you don't strictly need them, brackets can make your code easier for humans to read. If in doubt, add brackets.

## CODE | maths.py
```python
sweets = 17
friends = 5
print(sweets / friends)
print(sweets // friends)
print(sweets % friends)
print(2 ** 3)
print(2 + 3 * 4)
print((2 + 3) * 4)
```
@ line 1-2 | Our sharing story
Lines one and two store our story: seventeen sweets and five friends.
@ line 3 | / normal division
Line three uses normal division.
@ line 4 | // how many each
Line four uses floor division: how many sweets each friend gets.
@ line 5 | % how many left over
Line five uses modulo: how many are left over.
@ line 6 | ** power
Line six is two to the power of three: two times two times two.
@ line 7 | Which happens first?
Line seven is two plus three times four. Is the answer twenty, or fourteen? Make a guess.
@ line 8 | Brackets go first
And line eight is the same, but with brackets around two plus three.
@ run | Same numbers, different order, different answers
Let's run it. Seventeen divided by five is three point four. Floor division gives three each. Modulo gives two left over. Two to the power of three is eight. Line seven gives fourteen, because multiplying happens before adding. And with brackets, the adding happens first, so we get twenty.

## CODE | even_odd.py
```python
number = 14
print(number % 2)
print(number % 2 == 0)
seconds = 200
print(seconds // 60, "min", seconds % 60, "sec")
```
@ say
Here's one more example to show how useful the remainder operator is.
@ line 1-2 | Remainder when dividing by 2
We take the number fourteen and find its remainder when divided by two.
@ line 3 | Remainder 0 means even
Line three asks a question: is that remainder zero? If it is, the number is even. We'll learn more about questions like this next lesson.
@ line 4-5 | // and % together
Then two hundred seconds. Floor division by sixty gives the whole minutes, and modulo sixty gives the seconds left over.
@ run | 200 s = 3 min 20 s
Run it. Zero, so fourteen divides evenly by two. True, it's even. And two hundred seconds is three minutes and twenty seconds. Floor division and modulo make a great team.

## REVISE | Quick revise
@ point + - * / and ** (power)
Plus, minus, star, slash, and two stars for powers.
@ point // = whole-number division, % = remainder
Two slashes give whole-number division, and the percent sign gives the remainder.
@ point / always gives a float
A single slash always gives a float.
@ point Brackets first, then powers, then * /, then + -
And Python follows the order of operations, with brackets first.

## PRACTICE | Minutes to hours
@ task A film lasts 135 minutes. Write a program that prints: 2 hours and 15 minutes
Your turn. A film lasts one hundred and thirty five minutes. Write a program that prints how many hours and minutes that is.
@ hint There are 60 minutes in an hour. Use // for hours and % for minutes.
Hint: there are sixty minutes in an hour. Floor division gives the hours, and modulo gives the minutes left over.
@ pause 15
Pause the video and work it out.

## ANSWER | film_time.py
```python
minutes = 135
hours = minutes // 60
left = minutes % 60
print(hours, "hours and", left, "minutes")
```
@ line 1
We store the film length in minutes.
@ line 2
Hours is minutes, floor divided by sixty.
@ line 3
Left is the remainder: minutes, modulo sixty.
@ line 4
Then we print them with some text.
@ run
Two hours and fifteen minutes. Try changing minutes to ninety, or two hundred, and run it again. Your program works for any film!

## OUTRO
Superb! You can now do any calculation in Python. Next time, we'll learn about a special type of value that has only two possibilities: true or false. It's the secret behind every decision a computer makes. Like, share and subscribe, and keep coding. Happy Learning!
