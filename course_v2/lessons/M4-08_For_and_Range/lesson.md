---
id: "4.8"
title: "for Loops and range()"
module: 4
module_title: "Making Decisions and Loops"
next: "Loop Control and Validation"
minutes: 7.98
thumb_code: 'for i in range(1, 11):'
goals: ["Repeat an exact number of times", "range(stop), range(start, stop), range(start, stop, step)", "Looping over strings", "Loops inside loops"]
youtube:
  title: "Python Lesson 4.8: for Loops and range() - Repeat an Exact Number of Times | Introduction to Python"
  description: |
    Ziggy the Python shows how for loops and range() repeat code an exact number of times. We learn range with one,
    two and three numbers, print a times table, count down in steps, loop over the letters of a word, compare for
    and while, and draw a star triangle with a loop inside a loop.
    For beginners aged 7 to 20.
  tags: [python for loop, python range, times table python, nested loops python, learn python, fun skill builders]
---

<!-- Booklet chapter 4: iteration (for, counted loops). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Last time, while loops repeated until something changed. But often you know exactly how many times you want to repeat: ten times, a hundred times, once for every letter in a word. Today we'll learn to do that with for loops and a handy function called range.

## STUDY | Counting with range()
@ snippet for i in range(5):\n    print(i)
We already know for item in a list. Range gives the for loop a sequence of numbers to go through, without making a list ourselves.
@ point range(5) → 0, 1, 2, 3, 4
Range of five gives the numbers zero, one, two, three and four. That's five numbers, starting from zero, and stopping before five. Just like slices: up to, but not including, the stop.
@ point range(1, 6) → 1, 2, 3, 4, 5
With two numbers, you choose the start and the stop. Range of one to six gives one, two, three, four, five. Again, the stop number is not included.
@ point range(0, 20, 5) → 0, 5, 10, 15
With three numbers, the third is the step: how much to jump each time. Range zero, twenty, five gives zero, five, ten and fifteen.
@ point range(10, 0, -1) → 10, 9, ..., 1
And a negative step counts backwards. Range ten, zero, minus one gives ten down to one.
@ point i is the traditional name for a counting variable
Programmers often call the counting variable i, short for index. You can use any name, but i is the tradition, and you'll see it everywhere.

## CODE | range_demo.py
```python
for i in range(5):
    print("Hello number", i)
print(list(range(1, 6)))
print(list(range(0, 20, 5)))
print(list(range(10, 0, -2)))
```
@ line 1-2 | range(5): repeat 5 times
Lines one and two loop over range of five, printing a greeting with the number.
@ predict 5 | Which numbers will i take?
Which numbers will i take? Does it start at one?
@ run | 0 to 4: five times
Run. Hello number zero, up to hello number four. Five times, starting from zero.
@ line 3 | list(range(...)) shows the numbers
Line three turns a range into a list, so we can see all its numbers at once.
@ line 4 | A step of 5
Line four uses a step of five.
@ line 5 | Counting backwards in 2s
And line five counts backwards in twos, from ten.
@ predict 6 | Predict all three lists
Predict all three lists. Remember, the stop number is never included.
@ run | 1-5; 0, 5, 10, 15; 10, 8, 6, 4, 2
Run. One to five. Zero, five, ten, fifteen, but not twenty. And ten, eight, six, four, two, but not zero. The stop value is always left out, whichever direction you go.

## CODE | times_table.py
```python
number = int(input("Which times table? "))
for i in range(1, 11):
    answer = number * i
    print(f"{i:>2} x {number} = {answer}")
print("Done!")
```
@ input 7
@ say
Let's use range for something useful: a times table.
@ line 1 | Which table?
Line one asks which times table to print.
@ line 2 | range(1, 11): 1 to 10
Line two loops from one up to, but not including, eleven. So one to ten.
@ line 3 | Work out the answer
Line three works out the answer.
@ line 4 | :>2 lines the numbers up on the right
Line four prints the line. The colon, greater than sign and two after i pads the number to two characters, lined up on the right, so ten doesn't push the line out of place.
@ line 5 | After the loop
And after the loop, done.
@ predict 4 | The 7 times table: what's the last line?
I'll choose seven. What will the last line say?
@ run | 1 x 7 up to 10 x 7 = 70
Run. One times seven is seven, all the way to ten times seven is seventy. Ten lines from just four lines of code, and it works for any times table. Want to go up to twelve? Just change the eleven to thirteen.

## CODE | letters.py
```python
word = input("Type a word: ")
for letter in word:
    print(letter.upper(), end=" ")
print()
vowels = 0
for letter in word.lower():
    if letter in "aeiou":
        vowels += 1
print(f"{word} has {len(word)} letters and {vowels} vowels")
```
@ input banana
@ say
For loops can go through any sequence, and a string is a sequence of characters. So we can loop over the letters of a word.
@ line 1 | Ask for a word
Line one asks for a word.
@ line 2-3 | One letter at a time, on one line
The first loop takes one letter at a time, and prints it in capitals. The end equals a space trick, from lesson one point two, keeps everything on one line, with spaces between.
@ line 4 | Finish the line
Line four is an empty print, to finish that line.
@ line 5 | A vowel counter
Line five starts a vowel counter at zero.
@ line 6-8 | Count the vowels
The second loop goes through the word in lower case. If the letter is in the string a e i o u, it's a vowel, so we add one.
@ line 9 | Report
And line nine reports the results.
@ predict 5 | banana: how many vowels?
I'll type banana. How many vowels does it have?
@ run | B A N A N A; 3 vowels
Run. B A N A N A, spread out in capitals. Banana has six letters and three vowels. Three a's. Loops plus if statements let you analyse any text, letter by letter.

## STUDY | for or while?
@ table Use for when... | Use while when... ; you know how many times: 10 times, every item | you don't know how many: until it's right ; going through a list, string or range | waiting for something to change ; counting is automatic | you change the variable yourself
So which loop should you use? Use for when you know how many times to repeat, or you want to go through every item in a list, string or range. The counting is done for you, so it can't accidentally loop forever. Use while when you don't know in advance, and you're waiting for something to change, like a correct password.

## CODE | triangle.py
```python
rows = 5
for row in range(1, rows + 1):
    line = ""
    for star in range(row):
        line = line + "*"
    print(line)
```
@ say
Finally, a loop inside a loop. These are called nested loops, and they're perfect for patterns and grids. Let's draw a triangle of stars.
@ line 1 | How many rows?
Line one sets the number of rows: five.
@ line 2 | Outer loop: one time per row
The outer loop goes from one to rows plus one, so row will be one, two, three, four, five.
@ line 3 | Start each row empty
For each row, we start with an empty string.
@ line 4-5 | Inner loop: add 'row' stars
Then the inner loop runs row times, adding one star each time. On row one, it runs once. On row five, it runs five times.
@ line 6 | Print the finished row
After the inner loop finishes, we print the row. It's indented once, so it's inside the outer loop but not the inner one.
@ predict 6 | What shape? How many stars on the last row?
What shape will appear, and how many stars will the last row have?
@ run | A triangle: 1 to 5 stars
Run. One star, two stars, three, four, five. A triangle! The inner loop ran fifteen times in total: one plus two plus three plus four plus five. You could also write star times row, using string repetition, but nested loops can draw patterns that repetition can't, like chessboards and multiplication grids.

## STUDY | Common mistakes
@ table Mistake | What happens ; range(1, 10) for 1 to 10 | stops at 9: use range(1, 11) ; range(10, 0) to count down | nothing happens: add the step -1 ; for i in 5: | TypeError: an int isn't a sequence, use range(5) ; changing i inside the loop | the next repeat resets it anyway
The classic range mistakes. Forgetting that the stop isn't included, so range one to ten stops at nine. Counting down without a negative step, which gives an empty range and nothing happens. Looping over a plain number instead of range. And changing i inside the loop, expecting it to skip ahead. The for loop simply gives i the next value anyway.

## REVISE | Quick revise
@ point range(stop), range(start, stop), range(start, stop, step)
Range takes a stop, or a start and a stop, or a start, a stop and a step.
@ point The stop value is never included
The stop value is never included.
@ point for works on lists, strings and ranges
For loops work on lists, strings and ranges.
@ point for: a known number of repeats. while: until something changes
Use for for a known number of repeats, and while for repeating until something changes.

## PRACTICE | Stars triangle
@ task 1. Print the even numbers from 2 to 20 using range with a step.\n2. Print a countdown from 10 to 1, then "Blast off!"\n3. Bonus: print an upside-down triangle of stars (5 down to 1)
Your turn, with three small challenges. First, print the even numbers from two to twenty using range with a step. Second, print a countdown from ten to one, then blast off. And for a bonus, print an upside down triangle of stars, starting with five and going down to one.
@ hint range(2, 21, 2); range(10, 0, -1); "*" * n with range(5, 0, -1)
Hint: range two, twenty one, two. Range ten, zero, minus one. And for the bonus, star times n, with n counting down.
@ pause 15
Pause the video and give them a go.

## ANSWER | ranges.py
```python
for n in range(2, 21, 2):
    print(n, end=" ")
print()
for n in range(10, 0, -1):
    print(n, end=" ")
print("Blast off!")
for n in range(5, 0, -1):
    print("*" * n)
```
@ line 1-3
The even numbers, all on one line, then a new line.
@ line 4-6
The countdown with a negative step, then blast off.
@ line 7-8
And the upside down triangle, using string repetition.
@ run
Run. Two to twenty in twos. Ten down to one, blast off. And five stars down to one. Brilliant!

## OUTRO
Excellent! You can now repeat code exactly as many times as you need. Next time, we'll learn to take control of loops with break and continue, and use loops to check that the user's input makes sense. Like, share and subscribe, and keep coding. Happy Learning!
