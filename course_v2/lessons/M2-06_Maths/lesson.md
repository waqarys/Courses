---
id: "2.6"
title: "Maths with Python"
module: 2
module_title: "Variables, Input and Output"
next: "True or False?"
minutes: 9.48
thumb_code: '17 // 5   # 3'
goals: ["The 7 maths operators", "/ versus //", "Remainders with %", "Order of operations and brackets"]
youtube:
  title: "Python Lesson 2.6: Maths Operators - Division, Remainder, Powers | Introduction to Python"
  description: |
    Python is a super calculator. Ziggy the Python explains all seven arithmetic operators with a sharing-sweets story:
    normal division, whole-number division, remainders and powers, plus the order of operations and brackets.
    Then you convert minutes into hours and minutes.
    For beginners aged 7 to 20.
  tags: [python operators, python maths, modulo python, floor division, learn python, python for kids, fun skill builders]
---

<!-- Booklet 2.3 Arithmetic operations. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Today, Python becomes your super calculator. We'll learn all seven maths operators, including two that might be new to you, and find out why brackets can completely change an answer.

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
Line seven is two plus three times four.
@ predict 5 | 20 or 14?
Is the answer twenty, or fourteen? Make a guess before we go on.
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
@ predict 4 | 14 % 2 = ?
What's the remainder when fourteen sweets are shared between two friends?
@ line 3 | Remainder 0 means even
Line three asks a question: is that remainder zero? If it is, the number is even. We'll learn more about questions like this next lesson.
@ line 4-5 | // and % together
Then two hundred seconds. Floor division by sixty gives the whole minutes, and modulo sixty gives the seconds left over.
@ run | 200 s = 3 min 20 s
Run it. Zero, so fourteen divides evenly by two. True, it's even. And two hundred seconds is three minutes and twenty seconds. Floor division and modulo make a great team.

## CODE | shortcuts.py
```python
coins = 10
coins += 5
print(coins)
coins -= 3
print(coins)
coins *= 2
print(coins)
coins //= 4
print(coins)
```
@ say
Programmers change variables so often that Python has shortcuts for it. Let's look at them.
@ line 1 | Start with 10 coins
We start with ten coins.
@ line 2 | += means: add to what's already there
Line two says coins, plus equals, five. That's a shortcut for coins equals coins plus five. Add five to whatever is already in the box.
@ line 3
Print it.
@ line 4-5 | -= takes away
Line four uses minus equals to take away three, and line five prints the result.
@ line 6-7 | *= multiplies
Line six uses times equals to double the coins.
@ line 8-9 | //= floor-divides
And line eight uses floor division equals to share them between four.
@ predict 7 | Follow the coins: what are the four outputs?
Follow the coins in your head. Ten, plus five, minus three, times two, floor divided by four. What will each line print?
@ run | 15, 12, 24, 6
Run. Fifteen. Twelve. Twenty four. And six, because twenty four shared between four is exactly six. These shortcuts do exactly the same thing as the long versions. You'll see plus equals in almost every game, for scores and timers.

## CODE | pizza_party.py
```python
PEOPLE = 13
SLICES_EACH = 3
SLICES_PER_PIZZA = 8
slices = PEOPLE * SLICES_EACH
print("Slices needed:", slices)
print("Full pizzas:", slices // SLICES_PER_PIZZA)
print("Extra slices:", slices % SLICES_PER_PIZZA)
pizzas = (slices + SLICES_PER_PIZZA - 1) // SLICES_PER_PIZZA
print("Pizzas to order:", pizzas)
```
@ say
Let's use everything together to plan a pizza party.
@ line 1-3 | Constants for our party
Three constants: thirteen people, three slices each, and eight slices in every pizza.
@ line 4-5 | Total slices
Line four works out how many slices we need: people times slices each. Line five prints it.
@ line 6 | // : how many FULL pizzas
Line six uses floor division to find how many full pizzas those slices make.
@ line 7 | % : slices left over
Line seven uses modulo to find how many slices are left over after the full pizzas.
@ predict 6 | 39 slices, 8 per pizza: full pizzas and extras?
Thirteen times three is thirty nine slices. How many full pizzas is that, and how many slices are left over?
@ run | 39 slices = 4 full pizzas + 7 slices
Run. Thirty nine slices needed. Four full pizzas, which is thirty two slices, and seven extra slices. But we can't order seven slices! We need to round up to a whole pizza.
@ line 8 | A classic trick for rounding UP
Line eight is a classic programmer's trick for rounding up. Add one less than a pizza's worth of slices, which is seven, before floor dividing. Thirty nine plus seven is forty six, and forty six floor divided by eight is five.
@ line 9
Line nine prints the answer.
@ run | Round up: order 5 pizzas
Run. Pizzas to order: five. Nobody goes hungry! Change the number of people at the top, and the whole plan updates automatically.

## CODE | surprises.py
```python
print(2 ** 100)
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))
```
@ say
Here are two surprises that show how computers really handle numbers.
@ line 1 | A HUGE number
Line one: two to the power of one hundred. That's two, multiplied by itself one hundred times.
@ line 2 | A tiny decimal sum
Line two: zero point one plus zero point two.
@ predict 5 | Will Python cope with the huge number? Is 0.1 + 0.2 = 0.3?
Will Python cope with such a huge number? And surely zero point one plus zero point two is zero point three? Predict both.
@ run | Huge whole numbers: no problem. Decimals: tiny errors!
Run. A thirty one digit number! Python's whole numbers can be as big as you like. But look at the second line: zero point three, followed by lots of zeros and a four at the end. Computers store decimals in binary, using ones and zeros, and some decimals can't be stored exactly. So floats can be off by a tiny amount.
@ line 3 | round(value, 2): two decimal places
The fix for showing it neatly is round. Round, with the value, a comma, and two, rounds to two decimal places.
@ run | round() tidies it up
Run. Zero point three. Much better. We'll use round again in our recipe scaler project.

## STUDY | Common mistakes
@ table Code | What goes wrong ; 10 / 0 | ZeroDivisionError: you can't divide by zero ; 7 / 2 expecting 3 | / gives 3.5: use // for whole numbers ; 2 + 3 * 4 expecting 20 | * happens first: write (2 + 3) * 4 ; 5 ^ 2 for a power | ^ is not power in Python: use **
Here are the classic maths slips. Dividing by zero gives a ZeroDivisionError, because it makes no sense, even in maths. A single slash always gives a decimal answer, so use double slash when you want whole numbers. Forgetting the order of operations gives the wrong answer with no error at all, so add brackets. And if you've used a calculator that uses the little hat symbol for powers, remember that in Python, power is two stars.

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
