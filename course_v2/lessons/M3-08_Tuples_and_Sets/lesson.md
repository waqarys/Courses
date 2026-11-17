---
id: "3.8"
title: "Tuples and Sets"
module: 3
module_title: "Data Structures"
next: "Mini-Project: Daily Task Planner"
minutes: 8.23
thumb_code: 'point = (3, 4)'
goals: ["Tuples: ordered values that can't change", "Unpacking a tuple", "Sets: no duplicates, no order", "Union, intersection and difference"]
youtube:
  title: "Python Lesson 3.8: Tuples and Sets - Fixed Values and No Duplicates | Introduction to Python"
  description: |
    Two more data structures! Ziggy the Python explains tuples, which are like sealed envelopes that can't be
    changed (perfect for coordinates and colours), and sets, which are bags of unique stickers with no duplicates.
    We unpack tuples, remove duplicate names with a set, and compare two groups' favourite fruits.
    For beginners aged 7 to 20.
  tags: [python tuples, python sets, tuple vs list, set union intersection python, learn python, fun skill builders]
---

<!-- Booklet chapter 3: tuples and sets. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. We know lists and dictionaries. Today we'll meet the last two of Python's built in data structures: tuples and sets. Each one has a special power. Tuples can't be changed, and sets never contain duplicates. Let's find out when each one is useful.

## STUDY | Tuples: sealed envelopes
@ snippet point = (3, 4)\nred = (255, 0, 0)
A tuple looks like a list, but with round brackets instead of square ones. Here's a point on a map, three across and four up, and the colour red, written as amounts of red, green and blue.
@ point Ordered, like a list: index from 0
Like a list, a tuple keeps its items in order, and you can use index numbers and slices to read them.
@ point But a tuple can NEVER be changed
But a tuple is immutable. Once it's made, you can't add, remove or change any items. Think of it as a sealed envelope. You can read what's written on the outside, but you can't change what's inside.
@ point Why? For values that belong together and shouldn't change
Why would you want that? Some values belong together and should never be changed by accident: the coordinates of a point, the date of your birthday, the red, green and blue parts of a colour. A tuple protects them.
@ point Unpacking: x, y = point
Tuples have a neat trick called unpacking. You can write x comma y equals point, and Python puts the first item into x and the second into y, all in one line.

## CODE | tuples.py
```python
point = (3, 4)
print(point[0], point[1])
x, y = point
print(f"x is {x}, y is {y}")
red = (255, 0, 0)
r, g, b = red
print("Red:", r, "Green:", g, "Blue:", b)
point[0] = 10
```
@ line 1 | Round brackets: a tuple
Line one makes a tuple for a point: three across, four up.
@ line 2 | Read items by index, like a list
Line two reads both items by index, just like a list.
@ line 3 | Unpacking: two variables at once
Line three unpacks the tuple into two variables, x and y.
@ line 4
And line four prints them.
@ line 5-6 | Unpack three values
Lines five and six make a colour tuple, and unpack it into r, g and b.
@ line 7
Line seven prints the three parts.
@ run | Indexes and unpacking
Run. Three and four. x is three, y is four. And red has two hundred and fifty five red, no green and no blue. Your screen mixes these three amounts to make every colour you see.
@ line 8 | Try to change a tuple...
Now line eight tries to change the first item of the point to ten.
@ predict 4 | Can we change a tuple?
Will this work, like it would with a list?
@ run | TypeError: tuples can't be changed
Run. TypeError: tuple object does not support item assignment. The envelope is sealed! If you need a different point, you make a new tuple instead.

## CODE | swap.py
```python
a = "left"
b = "right"
a, b = b, a
print(a, b)
size = (1920, 1080)
width, height = size
print(width * height, "pixels")
```
@ say
Unpacking gives us a famous Python trick: swapping two variables in one line.
@ line 1-2 | Two variables
Two variables: a holds left, b holds right.
@ line 3 | Swap them in one line
Line three says a comma b equals b comma a. Python builds a tuple from the right hand side first, then unpacks it into the left.
@ line 4
Print them.
@ predict 4 | Have they swapped?
Has the swap worked?
@ run | Swapped!
Run. Right left. They've swapped. In many other languages, you need a third, temporary variable to do this.
@ line 5-7 | Screen size as a tuple
Lines five to seven store a screen size as a tuple, unpack it into width and height, and multiply them.
@ run | 2,073,600 pixels
Run. Two million, seventy three thousand, six hundred pixels on a full HD screen. A tuple is perfect for a size like this, because the width and height always travel together.

## STUDY | Sets: a bag of unique stickers
@ snippet fruits = {"apple", "kiwi", "mango"}
A set uses curly brackets, like a dictionary, but it holds single values, not key value pairs.
@ point A set never holds duplicates
A set's special power is that it never contains duplicates. Imagine a sticker album where each sticker has its own space. If you get a second copy of a sticker you already have, it doesn't add anything new. A set is the same.
@ point A set has no order: no indexes
A set also has no order, so there are no index numbers. You can't ask for the first item. You can only ask whether something is in the set, add things, remove things, and loop through it.
@ point set(list) removes duplicates from a list
A really common use: turning a list into a set removes all its duplicates in one step.
@ table Operation | Code | Gives ; union | a.union(b), or the bar symbol | everything in either set ; intersection | a & b | only what's in both ; difference | a - b | in a but not in b
Sets can also be combined, like the circles in a Venn diagram from maths class. The union is everything in either set. The intersection is only the things in both sets. And the difference is the things in the first set, but not the second.

## CODE | unique_names.py
```python
sign_ups = ["Asha", "Leo", "Asha", "Mia", "Leo", "Asha"]
print(len(sign_ups), "sign-ups")
unique = set(sign_ups)
print(len(unique), "different people")
print("Mia" in unique)
unique.add("Tom")
unique.add("Mia")
print(sorted(unique))
```
@ say
Here's a common problem. People signed up for a club, but some of them signed up more than once.
@ line 1 | A list with repeats
A list of six sign ups, with lots of repeats.
@ line 2 | Count the sign-ups
Line two counts the sign ups.
@ line 3 | set() keeps one of each
Line three turns the list into a set, which keeps only one of each name.
@ line 4 | Count the unique people
Line four counts the different people.
@ predict 5 | 6 sign-ups. How many different people?
Six sign ups. How many different people are there?
@ line 5 | in works on sets too
Line five checks whether Mia is in the set.
@ line 6-7 | add a new name, and one that's already there
Lines six and seven add Tom, who's new, and Mia, who's already there.
@ line 8 | sorted() gives a sorted LIST
And line eight prints the set as a sorted list, because a set has no order of its own.
@ run | 6 sign-ups, 3 people; adding Mia again changes nothing
Run. Six sign ups, but only three different people. Mia is in the set: True. And the sorted names are Asha, Leo, Mia and Tom. Adding Mia a second time changed nothing at all.

## CODE | fruit_venn.py
```python
class_a = {"apple", "mango", "kiwi", "banana"}
class_b = {"mango", "grape", "banana", "pear"}
print("Both:", sorted(class_a & class_b))
print("Either:", sorted(class_a | class_b))
print("Only A:", sorted(class_a - class_b))
```
@ say
Now let's compare the favourite fruits of two classes, using set operations.
@ line 1-2 | Two classes' favourite fruits
Two sets: class A's favourite fruits and class B's.
@ line 3 | & : in BOTH
Line three finds the fruits in both sets, with the and symbol, which is the intersection.
@ line 4 | | : in EITHER
Line four finds the fruits in either set, with the straight line symbol, which is the union.
@ line 5 | - : in A but not B
And line five finds the fruits only class A chose, using minus, which is the difference.
@ predict 7 | Work out all three before Python does
Use the two lists to work out all three answers.
@ run | Both, either, only A
Run. Both: banana and mango. Either: six fruits altogether, with no repeats. Only A: apple and kiwi. These operations are used for things like finding friends in common on social media, or the songs two playlists share.

## STUDY | Which structure should I use?
@ table Structure | Brackets | Ordered? | Changeable? | Duplicates? ; list | [ ] | yes | yes | yes ; tuple | ( ) | yes | no | yes ; set | { } | no | yes | no ; dictionary | {key: value} | yes | yes | keys: no
Here's a summary of all four structures. Lists are ordered and changeable. Tuples are ordered, but can't be changed. Sets have no order and no duplicates. And dictionaries link unique keys to values. Choosing the right one makes your program simpler.
@ point Watch out: {} is an empty DICTIONARY. Use set() for an empty set
One trap: empty curly brackets make an empty dictionary, not an empty set. To make an empty set, write set with round brackets.

## REVISE | Quick revise
@ point Tuple ( ): ordered, can't be changed
A tuple uses round brackets, keeps order, and can't be changed.
@ point Unpack: x, y = point; swap: a, b = b, a
Unpacking puts each item into its own variable, and makes swapping easy.
@ point Set { }: no duplicates, no order
A set uses curly brackets, has no duplicates and no order.
@ point & both, | either, - only in the first
And sets combine with and, the straight line, and minus.

## PRACTICE | Unique fruits
@ task votes = ["kiwi", "apple", "kiwi", "pear", "apple", "fig"]\n1. Print how many votes there were\n2. Print the different fruits, sorted\n3. Make a tuple for today's date (day, month, year) and unpack it
Your turn. Here's a list of fruit votes with repeats. Print how many votes there were. Then use a set to print the different fruits, sorted. Finally, make a tuple for today's date with a day, month and year, unpack it into three variables, and print them.
@ hint len(votes); sorted(set(votes)); day, month, year = date
Hint: len for the count, sorted of set for the unique fruits, and unpacking for the date.
@ pause 15
Pause the video and give it a try.

## ANSWER | unique_fruits.py
```python
votes = ["kiwi", "apple", "kiwi", "pear", "apple", "fig"]
print(len(votes), "votes")
print(sorted(set(votes)))
date = (17, 11, 2026)
day, month, year = date
print(f"Day {day}, month {month}, year {year}")
```
@ line 1-2
The votes, and how many there are.
@ line 3
A set removes the repeats, and sorted puts them in order.
@ line 4-6
A date tuple, unpacked into three variables.
@ run
Run. Six votes. Apple, fig, kiwi, pear. And day seventeen, month eleven, year two thousand and twenty six. Well done!

## OUTRO
Brilliant! You now know all four of Python's main data structures. Next time, we'll put them to work in our Module Three project: a daily task planner. Like, share and subscribe, and keep coding. Happy Learning!
