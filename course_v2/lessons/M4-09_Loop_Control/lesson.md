---
id: "4.9"
title: "Loop Control and Validation"
module: 4
module_title: "Making Decisions and Loops"
next: "Mini-Project: Guess the Number"
minutes: 7.88
thumb_code: 'while True:'
goals: ["break: leave a loop early", "continue: skip to the next repeat", "while True + break (do-while / repeat-until)", "Validating input with .isdigit()"]
youtube:
  title: "Python Lesson 4.9: break, continue and Input Validation | Introduction to Python"
  description: |
    Take control of your loops! Ziggy the Python explains break and continue, how Python writes do-while and
    repeat-until loops with while True and break, and how to validate input so a program asks again instead of
    crashing. We search a list, skip unwanted items, build a menu that quits on q, and check numbers with isdigit.
    For beginners aged 7 to 20.
  tags: [python break continue, input validation python, while true python, isdigit python, learn python, fun skill builders]
---

<!-- Booklet chapter 4: post-test loops (do-while, repeat-until) and validation. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Sometimes you want to leave a loop early, the moment you've found what you're looking for. Sometimes you want to skip one item and carry on. And very often, you want to keep asking the user until they type something sensible. Today we'll learn all three: break, continue and input validation.

## STUDY | break and continue
@ point break: leave the loop immediately
The word break, inside a loop, stops the loop immediately. Python jumps straight to the first line after the loop. It's like finding your lost keys in the second drawer: you stop searching the other drawers.
@ point continue: skip the rest of this repeat, go to the next
The word continue skips the rest of the current repeat, and goes straight back to the top of the loop for the next one. It's like sorting fruit: if this one's bruised, put it aside and move on to the next.
@ point Both are usually inside an if
Both are almost always inside an if statement, because you only want to break or skip in a certain situation.
@ point They work in for loops and while loops
And they work in both for loops and while loops.

## CODE | find_it.py
```python
lockers = ["books", "shoes", "keys", "lunch", "ball"]
for i in range(len(lockers)):
    print("Checking locker", i)
    if lockers[i] == "keys":
        print("Found the keys in locker", i)
        break
print("Search over.")
```
@ line 1 | Five lockers
Five lockers, each holding something.
@ line 2 | Loop over the locker numbers
Line two loops over the locker numbers, from zero up to the length of the list.
@ line 3 | Check each locker
Line three says which locker we're checking.
@ line 4-6 | Found it? Say so, then break
If this locker holds the keys, we say so, and break out of the loop.
@ line 7 | Runs after the loop ends, or after break
Line seven runs after the loop, whether it finished normally or with break.
@ predict 5 | Which lockers get checked?
The keys are in locker two. Which lockers will be checked?
@ run | Stops at locker 2: lockers 3 and 4 are never checked
Run. Checking locker zero, one, two. Found the keys in locker two. Search over. Lockers three and four were never checked, because break stopped the loop as soon as the keys were found. With a list of a million items, that could save a lot of time.

## CODE | skip_it.py
```python
scores = [8, -1, 6, 10, -1, 7]
total = 0
for score in scores:
    if score < 0:
        print("Skipping a missing score")
        continue
    total += score
print("Total of real scores:", total)
```
@ say
Now continue. In this list of scores, minus one means a player missed that round. We want to add up only the real scores.
@ line 1 | -1 means "missing"
The scores, with two minus ones meaning missing.
@ line 2-3 | A total, and the loop
A total at zero, and the loop.
@ line 4-6 | Negative? Skip to the next score
If the score is negative, we print a message, then continue, which jumps straight to the next score.
@ line 7 | Only reached for real scores
So line seven, adding to the total, is only reached for real scores.
@ line 8
After the loop, the total.
@ predict 5 | Add up only the real scores
Add up the real scores: eight, six, ten and seven. What's the total?
@ run | 31: the -1s were skipped
Run. Two skipping messages, and a total of thirty one. Without continue, the two minus ones would have been subtracted, giving twenty nine, which would be wrong.

## STUDY | do-while and repeat-until
@ point Some loops must run at least ONCE
A normal while loop checks its condition first, so it might never run. But some loops must run at least once. A menu should be shown at least once. A question should be asked at least once.
@ point Other languages: do ... while, and repeat ... until
Some languages have special loops for this, called do while, and repeat until. They check the condition at the end of each repeat, instead of the beginning. The booklet calls these post test loops.
@ snippet while True:\n    answer = input("Again? ")\n    if answer == "no":\n        break
Python doesn't have those, but it has a simple pattern that does the same job. While True makes a loop that would go on forever. Then, inside it, an if with break gives the exit. The check happens at the end, after the work is done.
@ point while True + break = run first, check after
So remember: while True, do the work, and then if it's time to stop, break.

## CODE | menu.py
```python
while True:
    print("1) Say hello  2) Tell a joke  q) Quit")
    choice = input("Choose: ").lower()
    if choice == "q":
        print("Bye!")
        break
    elif choice == "1":
        print("Hello there!")
    elif choice == "2":
        print("Why did the snake learn Python? To get ahead!")
    else:
        print("Please choose 1, 2 or q.")
```
@ input 2 | 7 | Q
@ say
Let's build a menu that keeps showing until the user quits.
@ line 1 | while True: loop until we break
Line one: while True. This loop will keep going until we break out.
@ line 2-3 | Show the menu, ask for a choice
Lines two and three show the menu and ask for a choice, in lower case.
@ line 4-6 | q: say bye and break
If the choice is q, say bye and break out of the loop. This is our exit.
@ line 7-10 | 1 and 2: do something, then loop again
For one and two, we do something, and then the loop goes round again, showing the menu.
@ line 11-12 | Anything else: a friendly hint
Anything else gets a friendly hint.
@ predict 6 | Choices: 2, then 7, then Q. How many times is the menu shown?
The user chooses two, then seven, then capital Q. How many times will the menu be shown?
@ run | Joke, hint, then Q quits
Run. The menu, and the choice two tells a joke. The menu again: seven gets the hint. The menu a third time: capital Q becomes small q, and we see bye. Three times, and the program ended cleanly. Almost every game and app has a main loop like this inside.

## CODE | validate.py
```python
while True:
    text = input("Pick a number from 1 to 10: ")
    if not text.isdigit():
        print("That's not a whole number.")
        continue
    number = int(text)
    if 1 <= number <= 10:
        break
    print("That's outside 1 to 10.")
print("Thanks! You chose", number)
```
@ input seven | 15 | 7
@ say
Now the most useful pattern of all: validation, which means checking input before we use it. Remember the ValueError we got in lesson two point five, when someone typed a word instead of a number? Let's make that impossible.
@ line 1 | Keep asking until the input is valid
A while True loop, to keep asking until the input is valid.
@ line 2 | Get the answer as text first
Line two gets the answer as text first. We don't convert it yet.
@ line 3 | .isdigit(): only digits?
Line three uses dot isdigit, which is True if the text is made only of digits. If it's not, we have a problem.
@ line 4-5 | Not digits: complain, ask again
So we print a message, and continue, which goes back to the top and asks again.
@ line 6 | Safe to convert now
By line six, we know the text is all digits, so converting it with int is safe.
@ line 7-8 | In range? Then it's valid: break
If the number is from one to ten, it's valid, so we break.
@ line 9 | Otherwise: out of range, loop again
Otherwise, we say it's out of range, and the loop goes round again.
@ line 10 | After the loop: a valid number
After the loop, we're guaranteed to have a valid number.
@ predict 6 | Answers: "seven", 15, then 7. What happens each time?
The user types the word seven, then fifteen, then seven as a digit. What happens each time?
@ run | Word rejected, 15 rejected, 7 accepted
Run. The word seven: that's not a whole number. Fifteen: that's outside one to ten. Seven: thanks, you chose seven. No crashes, just friendly messages. This is what professional programs do. One thing to know: isdigit is False for negative numbers and decimals, because the minus sign and the dot aren't digits.

## STUDY | Common mistakes
@ table Mistake | What happens ; while True: with no break | infinite loop: press Ctrl+C ; break outside a loop | SyntaxError ; continue before the counter update | the counter never changes: infinite loop ; int(text) before checking | ValueError for words
Common mistakes. A while True loop with no break that can be reached runs forever. Break can only be used inside a loop. Putting continue before the line that updates a while loop's counter can cause an infinite loop. And converting with int before checking, which brings back the ValueError.

## REVISE | Quick revise
@ point break leaves the loop; continue skips to the next repeat
Break leaves a loop. Continue skips to the next repeat.
@ point while True + break = do-while / repeat-until in Python
While True with break is Python's version of do while and repeat until.
@ point Validate: check the text, then convert, then check the range
To validate, check the text, convert it, then check the range.
@ point Ask again instead of crashing
And always ask again instead of crashing.

## PRACTICE | Quit on q
@ task Keep asking for numbers and add them up.\n- Skip anything that isn't a whole number (continue)\n- Stop when the user types q (break)\n- Then print the total
Your turn. Keep asking the user for numbers, and add them up. If they type something that isn't a whole number, skip it with continue. When they type q, stop with break. Then print the total.
@ hint while True: text = input(); if text == "q": break; if not text.isdigit(): continue
Hint: inside while True, check for q first, then check isdigit, then add.
@ pause 15
Pause the video and give it a go.

## ANSWER | adder.py
```python
total = 0
while True:
    text = input("Number (q to quit): ")
    if text == "q":
        break
    if not text.isdigit():
        print("Skipping", text)
        continue
    total += int(text)
print("Total:", total)
```
@ input 5 | ten | 12 | q
@ line 1-3
A total, a while True loop, and a question.
@ line 4-5
Q breaks out.
@ line 6-8
Anything that isn't digits is skipped.
@ line 9-10
Valid numbers are added, and after the loop we print the total.
@ run
Run. Five is added. Ten, as a word, is skipped. Twelve is added. Q stops the loop. Total: seventeen. Fantastic!

## OUTRO
Wonderful! You can now control loops and protect your programs from unexpected input. Next time, we'll put all of Module Four together in a full game: Guess the Number. Like, share and subscribe, and keep coding. Happy Learning!
