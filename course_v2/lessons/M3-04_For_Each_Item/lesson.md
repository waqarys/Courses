---
id: "3.4"
title: "Going Through a List with for"
module: 3
module_title: "Data Structures"
next: "Grids: Lists Inside Lists"
minutes: 8.89
thumb_code: 'for snack in snacks:'
goals: ["What a loop is", "for item in list: the loop variable", "Indentation shows what belongs to the loop", "Counting and totals with a loop"]
youtube:
  title: "Python Lesson 3.4: The for Loop - Go Through Every Item in a List | Introduction to Python"
  description: |
    Your first loop! Ziggy the Python explains how a for loop visits every item in a list, what the loop variable
    is, and why indentation matters so much. We number a snack list with a counter, add up scores with a running
    total, build a new list inside a loop, and fix the indentation mistakes everyone makes.
    For beginners aged 7 to 20.
  tags: [python for loop, loop through list python, python indentation, running total python, learn python, fun skill builders]
---

<!-- Booklet chapter 3/4: iteration over a list (full loop detail in 4.8). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Today is an exciting day, because we're learning our first loop. Loops let a computer repeat things, and repeating things is what computers are best at. By the end of this lesson, you'll be able to do something with every item in a list, whether it has three items or three million.

## STUDY | The problem with lots of prints
@ snippet print(snacks[0])\nprint(snacks[1])\nprint(snacks[2])
Imagine we want to print every snack in a list, one per line. We could print index zero, then index one, then index two.
@ point What if the list has 500 items?
But what if the list had five hundred items? We'd need five hundred lines. And if someone added a new snack, we'd have to add another line. That's slow, boring and easy to get wrong.
@ point A loop repeats code for us
A loop solves this. A loop is a piece of code that repeats. Instead of writing the same thing many times, we write it once, and tell Python to repeat it.
@ point "For each snack in the bag, take it out and say its name"
Imagine a bag of snacks. You could say: for each snack in the bag, take it out, and say its name. That one instruction works whether the bag holds three snacks or three hundred. That's exactly how a for loop works.

## STUDY | How a for loop works
@ snippet for snack in snacks:\n    print(snack)
Here it is in Python. The word for, a name for the loop variable, the word in, the list, and a colon at the end. Then, on the next line, indented by four spaces, the code to repeat.
@ point The loop variable holds ONE item each time round
The loop variable, here called snack, is a temporary box. The first time round the loop, it holds the first item. The second time, the second item. And so on, until there are no items left.
@ point Indented lines BELONG to the loop
The indented lines are called the body of the loop. Indentation means the spaces at the start of the line. Every indented line belongs to the loop, and repeats. The first line that isn't indented is outside the loop, and runs once, after the loop has finished.
@ point Don't forget the colon!
And don't forget the colon at the end of the for line. The colon means: here comes the body. Forgetting it is the most common loop mistake of all.
@ point Choose a name that fits: for planet in planets
A good habit is to name the list with a plural, and the loop variable with the singular. For snack in snacks. For planet in planets. For score in scores. It makes the loop read like an English sentence.

## CODE | snacks_loop.py
```python
snacks = ["apple", "banana", "mango", "grapes"]
for snack in snacks:
    print("I like", snack)
print("All done!")
```
@ line 1 | A list of four snacks
Line one is our list of four snacks.
@ line 2 | for each snack in snacks:
Line two starts the loop. For snack in snacks, colon.
@ line 3 | Indented: this line repeats
Line three is indented by four spaces, so it's inside the loop. It prints I like, and the current snack.
@ line 4 | Not indented: runs once, after the loop
Line four is not indented, so it's outside the loop.
@ predict 6 | How many times will each line print?
How many times will I like be printed? And how many times will all done be printed?
@ run | The body ran 4 times, then the loop ended
Run. I like apple. I like banana. I like mango. I like grapes. Four times, once for each snack. Then all done, just once, because it's outside the loop. Python did all the work. If we added ten more snacks to the list, the loop would handle them without changing a single other line.

## CODE | numbered.py
```python
snacks = ["apple", "banana", "mango", "grapes"]
number = 1
for snack in snacks:
    print(f"{number}. {snack}")
    number = number + 1
print(f"That's {number - 1} snacks.")
```
@ say
Now let's number the list, using a counter variable.
@ line 1 | The same snacks
The same four snacks.
@ line 2 | A counter starts at 1, BEFORE the loop
Line two creates a counter, starting at one. It's created before the loop, so it only happens once.
@ line 3 | The loop
Then the loop.
@ line 4 | Print the number and the snack
Inside the loop, line four prints the number, a dot, and the snack, using an F string.
@ line 5 | Add 1 to the counter each time round
And line five adds one to the counter. It's indented, so it happens every time round the loop.
@ line 6 | After the loop
After the loop, line six says how many snacks there were. Why number minus one? Think about it.
@ predict 6 | What will the counter be when the loop ends?
After the last snack, the counter gets one more added. So what will number be when the loop finishes?
@ run | A numbered list, made automatically
Run. One, apple. Two, banana. Three, mango. Four, grapes. And: that's four snacks. When the loop finished, number was five, because we added one after the last snack too. That's why we subtract one. Counting like this is called keeping a count, and it's used in programs everywhere.

## CODE | total.py
```python
scores = [12, 7, 30, 18]
total = 0
for score in scores:
    total = total + score
    print("Added", score, "-> total", total)
print("Final total:", total)
```
@ say
Here's another pattern you'll use all the time: a running total.
@ line 1-2 | The total starts at 0
We have four scores, and a total that starts at zero, before the loop.
@ line 3-4 | Add each score to the total
The loop goes through each score, and adds it to the total.
@ line 5 | Show the total growing
Line five is inside the loop too, so we can watch the total grow.
@ line 6
And after the loop, we print the final total.
@ predict 6 | Follow the total: 0, then...?
Follow the total in your head. Zero, add twelve, add seven, add thirty, add eighteen.
@ run | 12, 19, 49, 67
Run. Twelve, nineteen, forty nine, sixty seven. A running total, just like a shop till adding up your shopping. Python's sum function does this for us, but now you know how it works inside. And this pattern can do things sum can't, like adding only certain scores, which we'll learn in Module Four.

## CODE | reset_bug.py
```python
scores = [12, 7, 30, 18]

for score in scores:
    total = 0
    total = total + score
print("Final total:", total)
```
@ say
Now let's look at a bug that catches almost everyone with running totals. Spot the difference from the last program.
@ line 1 | The same scores
The same four scores.
@ line 3 | The loop
The loop.
@ line 4 | total = 0 is INSIDE the loop this time
But this time, total equals zero is inside the loop, indented.
@ line 5 | Add the score
Then we add the score.
@ line 6
And print the final total after the loop.
@ predict 6 | Will it still say 67?
Will we still get sixty seven? Think about what happens to the total each time round.
@ run | Bug: only the last score!
Run. Final total: eighteen. That's just the last score! Every time round the loop, total was reset to zero, then one score was added. So at the end, it only holds the last one. No error message, just a wrong answer: a logic error.
@ edit 2 => total = 0
Let's fix it. We create the total once, before the loop, on line two.
@ edit 4 => 
And we delete the reset inside the loop.
@ run | Fixed: create the total before the loop
Run. Final total: sixty seven. The rule to remember: anything that should happen once goes before the loop. Anything that should happen for every item goes inside it.

## CODE | shout_list.py
```python
names = ["asha", "leo", "mia"]
loud = []
for name in names:
    loud.append(name.upper())
print(names)
print(loud)
```
@ say
One more pattern: building a new list inside a loop.
@ line 1 | Names in small letters
A list of names, in small letters.
@ line 2 | An empty list to fill
An empty list called loud, ready to be filled.
@ line 3-4 | Append a changed version of each name
The loop takes each name, makes a capital letter version with dot upper, and appends it to loud.
@ line 5-6 | Print both lists
Then we print both lists.
@ run | A new list, built one item at a time
Run. The original names are unchanged, and loud has all three in capitals. Start with an empty list, loop, append. You'll see this pattern in nearly every program that works with data.

## STUDY | Common mistakes
@ table Mistake | What happens ; for snack in snacks (no colon) | SyntaxError: expected ':' ; body not indented | IndentationError: expected an indented block ; total = 0 inside the loop | total resets every time ; print(snacks) instead of print(snack) | prints the whole list each time
Here are the loop mistakes everyone makes. Forgetting the colon gives a SyntaxError. Forgetting to indent the body gives an IndentationError. Putting total equals zero inside the loop resets the total every time round, so you only ever get the last score. And printing the list instead of the loop variable prints the whole list, again and again.

## REVISE | Quick revise
@ point for item in list: repeats the body for every item
For item in list repeats the body once for every item.
@ point The loop variable holds one item each time
The loop variable holds one item each time round.
@ point Indented lines repeat; the next unindented line runs after
Indented lines repeat. The next line that isn't indented runs once, after the loop.
@ point Counters and totals start BEFORE the loop
Counters and totals start before the loop, and change inside it.

## PRACTICE | Score adder
@ task scores = [5, 9, 3, 8, 10]\nUse a for loop to add up the scores, then print the total and the average.
Your turn. Here's a list of five scores. Use a for loop to add them up, then print the total, and the average. Don't use the sum function. Make the loop do the work!
@ hint total = 0 before the loop; average = total / len(scores)
Hint: start a total at zero before the loop. Add each score inside the loop. Then the average is the total divided by the length of the list.
@ pause 15
Pause the video and give it a go.

## ANSWER | score_adder.py
```python
scores = [5, 9, 3, 8, 10]
total = 0
for score in scores:
    total = total + score
print("Total:", total)
print("Average:", total / len(scores))
```
@ line 1-2
The scores, and a total starting at zero.
@ line 3-4
The loop adds each score to the total.
@ line 5-6
After the loop, not indented, print the total and the average.
@ run
Run. Total: thirty five. Average: seven point zero. If your prints were indented, they'd appear five times, so check your indentation if your output looks different.

## OUTRO
You did it! You've written your first loops, and that's a huge step. Next time, we'll put lists inside lists to make grids, like a game board. Like, share and subscribe, and keep coding. Happy Learning!
