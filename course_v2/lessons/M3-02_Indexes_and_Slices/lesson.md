---
id: "3.2"
title: "Indexes and Slices"
module: 3
module_title: "Data Structures"
next: "Changing Lists"
minutes: 8.53
thumb_code: 'planets[0]'
goals: ["Index numbers start at 0", "Negative indexes count from the end", "Slices: from... up to but not including", "Reading an IndexError"]
youtube:
  title: "Python Lesson 3.2: List Indexes and Slices - Why Counting Starts at 0 | Introduction to Python"
  description: |
    How do you pick one item out of a list? Ziggy the Python explains index numbers (starting from zero!),
    negative indexes, and slices that cut out part of a list. We explore the planets line by line, predict every
    output, trigger an IndexError on purpose, and see that strings can be indexed and sliced too.
    For beginners aged 7 to 20.
  tags: [python list index, python slicing, indexerror python, zero based indexing, learn python, fun skill builders]
---

<!-- Booklet chapter 3: arrays/lists, accessing elements. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Last time, we stored lots of things in one list. But how do we get just one thing back out? Today we'll learn about index numbers, which let us pick any item, and slices, which let us cut out a whole section. And we'll discover why programmers start counting from zero.

## STUDY | Every item has a position
@ table Index | 0 | 1 | 2 | 3 ; Item | "Mercury" | "Venus" | "Earth" | "Mars"
Every item in a list has a position number, called its index. Here's a list of the first four planets. Mercury is at index zero. Venus is at index one. Earth is at index two. And Mars is at index three.
@ point Counting starts at 0, not 1!
Yes, the first item is at index zero, not one. This surprises everyone at first. Python, and most programming languages, start counting from zero.
@ point Index = how many steps from the start
Here's a way to think about it. The index tells you how many steps to take from the start of the list. Mercury is right at the start, so it's zero steps away. Venus is one step away. Earth is two steps away.
@ point Like floors in a lift: Ground, 1, 2, 3
It's like the buttons in a lift in many countries: the ground floor comes first, then floor one, floor two, and so on. The ground floor is floor zero.
@ snippet planets[2]   # "Earth"
To get an item, write the list's name, then the index in square brackets. Planets, square bracket, two, gives us Earth.

## STUDY | Counting backwards
@ table Index | 0 | 1 | 2 | 3 ; Item | "Mercury" | "Venus" | "Earth" | "Mars" ; From the end | -4 | -3 | -2 | -1
Python has a handy extra trick. You can also count backwards from the end, using negative numbers. Minus one is always the last item. Minus two is the second to last, and so on.
@ point [-1] is always the LAST item
Minus one is really useful, because you often want the last item, and you don't always know how long the list is. The last song added to a playlist. The latest message in a chat. The most recent score.
@ point The last positive index is len - 1
And here's an important fact: in a list of four items, the last positive index is three, which is the length minus one. There is no index four. Ask for one, and Python gives you an IndexError.

## CODE | planets.py
```python
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets[0])
print(planets[2])
print(planets[-1])
print(planets[-2])
print(len(planets))
print(planets[8])
```
@ line 1-2 | Eight planets (one list over two lines)
Lines one and two make a list of all eight planets, in order from the Sun. A list can continue onto the next line, as long as the square bracket is still open.
@ line 3 | Index 0 = the first item
Line three prints index zero.
@ line 4 | Index 2 = the third item
Line four prints index two.
@ predict 5 | Which planets are [0] and [2]?
Which planets will those be? Remember where counting starts.
@ run | [0] = Mercury, [2] = Earth
Run. Mercury, the first planet, and Earth, the third planet. Our home is at index two.
@ line 5 | -1 = the last item
Line five prints index minus one.
@ line 6 | -2 = second from the end
Line six prints index minus two.
@ line 7 | How many planets?
And line seven prints the length of the list.
@ run | Neptune, Uranus, and 8 items
Run. Neptune is last, and Uranus is second from the end. And there are eight planets.
@ line 8 | There are 8 planets... so is there an index 8?
Now, there are eight planets. So line eight asks for index eight. What do you think will happen?
@ predict 4 | 8 items. Does index 8 exist?
Think carefully about where counting starts.
@ run | IndexError: list index out of range
Run. IndexError: list index out of range. With eight items, the indexes go from zero to seven. Index eight would be a ninth planet, and there isn't one! This is one of the most common errors in all of programming. Whenever you see it, check whether you started counting at one instead of zero.

## STUDY | Slices: cutting out a section
@ snippet planets[1:4]   # Venus, Earth, Mars
A slice gives you a section of the list, as a new, smaller list. Inside the square brackets, write a start index, a colon, and a stop index.
@ point Start is included, stop is NOT
Here's the rule: the start index is included, but the stop index is not. It means: from index one, up to but not including index four. So we get indexes one, two and three: Venus, Earth and Mars.
@ point Like a ruler: stop BEFORE the number
Think of the stop number as a fence. You walk up to the fence, but you don't go past it.
@ point Leave one side empty: [:3] from the start, [5:] to the end
You can leave out the start, and the slice begins at the beginning. Leave out the stop, and it goes all the way to the end. Colon three means the first three items. Five colon means everything from index five onwards.
@ point Stop - start = how many items you get
And a handy check: stop minus start tells you how many items you'll get. Four minus one is three items.

## CODE | slices.py
```python
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
rocky = planets[0:4]
giants = planets[4:]
print(rocky)
print(giants)
print(planets[:2])
print(planets[-3:])
print(planets[2:3])
```
@ line 1-2 | The same eight planets
The same eight planets.
@ line 3 | The rocky planets: index 0 up to (not including) 4
Line three slices out the rocky planets: from index zero, up to but not including four.
@ line 4 | The giants: index 4 to the end
Line four slices out the giant planets: from index four, all the way to the end.
@ line 5-6
Lines five and six print both lists.
@ predict 6 | Which planets are in each slice?
Which planets end up in each slice? Count them out on your fingers, starting from zero.
@ run | Four rocky planets, four giants
Run. The rocky planets: Mercury, Venus, Earth and Mars. And the giants: Jupiter, Saturn, Uranus and Neptune. Our eight planets, split neatly in two.
@ line 7 | The first two
Line seven: colon two, the first two planets.
@ line 8 | The last three
Line eight: minus three, colon. From the third to last, to the end.
@ line 9 | 2:3 gives just one item, but still a list
And line nine: two colon three.
@ predict 5 | What do [:2], [-3:] and [2:3] give?
Predict these three. The last one is tricky: is it a planet, or a list?
@ run | A slice is always a list
Run. Mercury and Venus. Saturn, Uranus and Neptune. And the last one is Earth, inside square brackets. A slice always gives you a list, even if it only has one item in it. An index gives you the item itself.

## CODE | word_slices.py
```python
word = "PYTHON"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[2:])
print(word[::-1])
```
@ say
Here's a bonus. Strings are sequences of characters, so you can index and slice them too!
@ line 1 | A string is a sequence of characters
We store the word Python in capitals.
@ line 2-3 | First and last letters
Line two prints the first letter, and line three the last.
@ line 4-5 | Slices of a string
Line four slices from zero up to three. Line five slices from two to the end.
@ line 6 | Level up: [::-1] reverses
And line six is a famous trick: two colons and minus one. This slice steps through the string backwards.
@ predict 6 | Predict all five, especially the last!
Predict all five outputs, especially the last one.
@ run | P, N, PYT, THON, NOHTYP
Run. P and N. P Y T, and T H O N. And the last one is the word reversed: N O H T Y P. This also works on lists. Programmers use it to check whether a word is a palindrome, a word that reads the same backwards, like level or racecar.

## STUDY | Common mistakes
@ table Mistake | Fix ; planets[1] for the first item | the first item is planets[0] ; planets[8] in a list of 8 | the last is planets[7] or planets[-1] ; planets[1:3] expecting 3 items | stop is not included: 3 - 1 = 2 items ; planets(0) | use square brackets for indexes
Here are the classic slip ups. Using one for the first item, when it should be zero. Using the length as an index, which is always one too far. Expecting the stop index of a slice to be included. And using round brackets instead of square brackets.

## REVISE | Quick revise
@ point Indexes start at 0; the last is len - 1
Indexes start at zero, and the last one is the length minus one.
@ point [-1] is the last item, [-2] the one before
Minus one is the last item, minus two the one before it.
@ point [start:stop] includes start, stops BEFORE stop
A slice includes the start, and stops before the stop.
@ point IndexError = you asked for a position that doesn't exist
An IndexError means you asked for a position that doesn't exist. Strings can be indexed and sliced too.

## PRACTICE | First and last
@ task days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]\nPrint:\n1. the first 3 days (a slice)\n2. the last day (a negative index)\n3. the weekend: Sat and Sun (a slice)
Your turn. Make a list of the seven days of the week. Print the first three days with a slice. Print the last day using a negative index. Then print just the weekend, Saturday and Sunday, with another slice.
@ hint days[:3], days[-1], days[5:]
Hint: one slice from the start, one negative index, and one slice that goes to the end.
@ pause 15
Pause the video and try it.

## ANSWER | days.py
```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[:3])
print(days[-1])
print(days[5:])
```
@ line 1
The seven days.
@ line 2
Colon three gives the first three.
@ line 3
Minus one gives the last day.
@ line 4
And five colon gives everything from Saturday to the end. Minus two colon would work too.
@ run
Run. Monday, Tuesday, Wednesday. Sunday. And the weekend: Saturday and Sunday. Brilliant!

## OUTRO
Excellent work! You can now find any item in a list, and slice out any section. Next time, we'll change lists while the program runs: adding items, removing them and sorting them. Like, share and subscribe, and keep coding. Happy Learning!
