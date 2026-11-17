---
id: "3.1"
title: "Lists: Many Things in One Box"
module: 3
module_title: "Data Structures"
next: "Indexes and Slices"
minutes: 8.29
thumb_code: 'snacks = ["apple", "mango"]'
goals: ["Why we need lists", "Making a list with [ ] and commas", "Printing a list and counting it with len()", "Lists and arrays"]
youtube:
  title: "Python Lesson 3.1: Lists - Store Many Things in One Variable | Introduction to Python"
  description: |
    Module 3 begins! Ziggy the Python introduces lists: one variable that holds a whole collection. We see why
    lists beat lots of separate variables, how to write them with square brackets and commas, how to print and
    count them, adding lists together, and how Python lists compare with arrays in other languages.
    For beginners aged 7 to 20.
  tags: [python lists, python list for beginners, data structures python, python arrays, learn python, fun skill builders]
---

<!-- Booklet chapter 3 "Data Structures": arrays and lists. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Welcome to Module Three, all about data structures. That sounds technical, but it just means ways of organising lots of information. Today we meet the most useful one of all: the list. One variable, holding a whole collection of things.

## STUDY | Why do we need lists?
@ snippet game1 = "Minecraft"\ngame2 = "Tetris"\ngame3 = "Mario Kart"\ngame4 = "Roblox"
Imagine storing your favourite games. With what we know so far, we'd need a separate variable for each one: game one, game two, game three, game four.
@ point What about 100 games? Or 1,000?
That works for four games. But what about a hundred? Or a thousand songs in a playlist? Or every player in an online game? We'd need thousands of variables, and we couldn't easily count them or go through them.
@ point A list stores many values in ONE variable
A list solves this. A list stores many values, in order, in one single variable. Your music app's playlist is a list. A class register is a list. Your shopping list is, well, a list.
@ point Like a train: carriages joined in order
Think of a list as a train. The train has one name, and it pulls a line of carriages. Each carriage carries one value, and the carriages stay in order. You can add carriages, remove them, and count them.

## STUDY | Making a list
@ snippet snacks = ["apple", "banana", "mango"]
Here's how you write a list in Python. Square brackets at the start and end. Inside, the values, which we call items, separated by commas.
@ point [ ] square brackets, items separated by commas
Square brackets are the keys next to the letter P on most keyboards. The commas go between items, not after the last one.
@ point Items can be any type: strings, numbers, booleans
Items can be any type: strings, numbers, booleans, and even other lists, which we'll meet in lesson three point five.
@ point [] is an empty list, ready to fill later
And two square brackets with nothing between them make an empty list. That's useful when you want to start with nothing and fill the list up later, like an empty shopping basket.
@ point len(list) counts the items
And the len function, which counted characters in a string, counts the items in a list.

## CODE | snacks.py
```python
snacks = ["apple", "banana", "mango"]
print(snacks)
print(len(snacks))
scores = [12, 7, 30, 18]
print(scores)
print(sum(scores))
mixed = ["Ziggy", 10, True, 2.5]
print(mixed)
```
@ line 1 | Square brackets, commas between items
Line one makes a list of three snacks. Each snack is a string, so each one has quote marks, and commas separate them.
@ line 2 | print shows the whole list
Line two prints the whole list.
@ line 3 | len() counts the items
Line three prints the length of the list.
@ predict 5 | What will print(snacks) look like?
When we print a list, will we see just the words, or something else? And what will len say?
@ run | Python shows the brackets and quotes
Run. Python shows the list exactly the way we'd write it in code: square brackets, quote marks and commas. And len says three, because there are three items. Not the number of letters, the number of items.
@ line 4 | A list of numbers
Line four makes a list of four scores. Numbers don't need quotes.
@ line 5
Line five prints it.
@ line 6 | sum() adds up a list of numbers
And line six uses a new function, sum, which adds up every number in a list.
@ predict 5 | 12 + 7 + 30 + 18 = ?
Can you add up twelve, seven, thirty and eighteen before Python does?
@ run | sum() = 67
Run. The scores, and their total: sixty seven.
@ line 7-8 | A list can mix types
Lines seven and eight make a list that mixes types: a string, an int, a boolean and a float.
@ run | Python lists are flexible
Run. Python is happy to store all of them together. Usually, though, a list holds things of the same kind, because that makes it easier to work with.

## CODE | games.py
```python
games = ["Minecraft", "Tetris", "Mario Kart"]
more = ["Roblox", "Chess"]
all_games = games + more
print(all_games)
print(f"I have {len(all_games)} favourite games.")
print("Tetris" in all_games)
print("Zelda" in all_games)
print(["ha"] * 3)
```
@ say
Lists have some of the same tricks as strings. Let's see.
@ line 1-2 | Two lists
Two lists: three games, and two more.
@ line 3 | + joins two lists into a new one
Line three joins them with a plus sign, making a brand new list.
@ line 4-5 | Print it, and count it in an f-string
Line four prints it, and line five counts it inside an F string.
@ line 6-7 | in asks: is this item in the list?
Lines six and seven use the word in, to ask whether an item is in the list. Is Tetris in it? Is Zelda in it?
@ line 8 | * repeats a list
And line eight repeats a list, just like repeating a string.
@ predict 6 | Predict all four outputs
Pause and predict. How many games in total? Which in checks are True? And what does the last line make?
@ run | Join, count, check, repeat
Run. All five games in one list. I have five favourite games. Tetris is in the list: True. Zelda isn't: False. And the last line makes a list with ha three times. Joining, counting, checking and repeating: the same ideas we used with strings, now working with whole collections.

## CODE | weather.py
```python
temps = [18, 21, 25, 19, 23, 27, 22]
print("Days recorded:", len(temps))
print("Hottest:", max(temps))
print("Coldest:", min(temps))
total = sum(temps)
average = total / len(temps)
print("Average:", round(average, 1))
```
@ say
Here's a real use for a list: a week of weather. Scientists and weather apps do exactly this kind of thing, just with far more data.
@ line 1 | Seven temperatures, one list
Line one stores the temperature for each day of the week, in degrees Celsius. Seven numbers, one list.
@ line 2 | How many days?
Line two prints how many days we recorded, using len.
@ line 3 | max() finds the biggest
Line three uses max, which finds the biggest item in the list.
@ line 4 | min() finds the smallest
Line four uses min, which finds the smallest.
@ line 5 | Add them all up
Line five adds up all the temperatures with sum.
@ line 6 | Average = total ÷ how many
Line six works out the average: the total, divided by the number of days. This is the same formula you use in maths class.
@ line 7 | Round to 1 decimal place
And line seven prints the average, rounded to one decimal place.
@ predict 6 | Hottest, coldest, and a guess at the average?
Look at the numbers. Which is the hottest day, and which is the coldest? And roughly what do you think the average will be?
@ run | Seven days: 27 max, 18 min, average 22.1
Run. Seven days recorded. Hottest: twenty seven. Coldest: eighteen. Average: twenty two point one. Imagine doing that for a whole year of weather. With a list, the code would be exactly the same length, whether there were seven numbers or seven thousand. That's the real power of lists.

## STUDY | Lists and arrays
@ table | Python list | Array (many languages) ; size | grows and shrinks | often fixed ; item types | any mix | usually all one type ; memory | flexible | items side by side ; speed | fast enough for most jobs | very fast for numbers
The booklet talks about arrays, so let's compare. Many languages use arrays: a row of boxes side by side in the computer's memory, usually all of the same type, and often with a fixed size. Python's list is more flexible: it can grow and shrink, and hold any mix of types. For most programs, a list is exactly what you need. Scientists who crunch millions of numbers use special arrays from extra libraries, because they're even faster.
@ point In this course: list = Python's version of an array
So in this course, whenever the booklet says array, you can use a Python list.

## STUDY | Common mistakes
@ table Code | What goes wrong ; snacks = ("apple", "pear") | round brackets make a tuple, not a list ; ["apple" "pear"] | missing comma: becomes "applepear" ; [apple, pear] | missing quotes: NameError ; len(snacks) expecting letters | len counts items, not letters
A few common slips. Round brackets make something called a tuple, which we'll meet later, so use square brackets for a list. Forgetting a comma between two strings silently glues them into one item! Forgetting quote marks around text gives a NameError. And remember that len counts items, not letters.

## REVISE | Quick revise
@ point A list stores many items in order, in one variable
A list stores many items, in order, in one variable.
@ point [ ] with commas between items; [] is empty
Use square brackets with commas between items. Empty brackets make an empty list.
@ point len() counts, sum() adds up, in checks membership
len counts the items, sum adds up numbers, and in checks if something is in the list.
@ point + joins lists, * repeats them
Plus joins lists, and star repeats them.

## PRACTICE | My games
@ task Make a list of your 4 favourite games (or films). Print:\n1. the whole list\n2. how many there are, in a sentence\n3. True or False: is a game you choose in the list?
Your turn. Make a list of your four favourite games, or films if you prefer. Print the whole list. Then print a sentence saying how many there are. Then check whether one particular title is in your list.
@ hint len(my_list) inside an f-string, and "title" in my_list
Hint: put len inside an F string, and use the word in for the check.
@ pause 15
Pause the video and give it a try.

## ANSWER | my_games.py
```python
films = ["Moana", "Coco", "Up", "Frozen"]
print(films)
print(f"I have {len(films)} favourite films.")
print("Up" in films)
```
@ line 1
Here's my version, with films. Four titles, in quotes, separated by commas.
@ line 2-3
Print the list, and a sentence with len inside an F string.
@ line 4
And check whether Up is in the list.
@ run
Run. The list, I have four favourite films, and True. Try checking for something that isn't in your list, and you should get False.

## OUTRO
Great job! You've made your first data structure. Next time, we'll learn how to pick out single items from a list using index numbers, and how to slice out parts of it. Like, share and subscribe, and keep coding. Happy Learning!
