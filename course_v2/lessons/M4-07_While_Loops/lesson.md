---
id: "4.7"
title: "while Loops"
module: 4
module_title: "Making Decisions and Loops"
next: "for Loops and range()"
minutes: 7.91
thumb_code: 'while count > 0:'
goals: ["Iteration with a condition", "while condition: repeat the block", "Counters that change each time round", "Avoiding infinite loops"]
youtube:
  title: "Python Lesson 4.7: while Loops - Keep Going While It's True | Introduction to Python"
  description: |
    Make your program repeat until something changes! Ziggy the Python explains while loops, how the condition is
    checked before every repeat, and why something inside the loop must change. We build a rocket countdown,
    a savings goal tracker and a password prompt that keeps asking, and learn how to stop a runaway infinite loop.
    For beginners aged 7 to 20.
  tags: [python while loop, loops in python, infinite loop python, countdown python, learn python, fun skill builders]
---

<!-- Booklet chapter 4: iteration (while, pre-test loops). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. In lesson three point four, we used a for loop to visit every item in a list. But sometimes we don't know in advance how many times to repeat. Keep stirring while the sauce is lumpy. Keep asking until the password is right. Today we'll learn while loops, which repeat for as long as a condition stays True.

## STUDY | Keep going while...
@ point while = repeat as long as the condition is True
A while loop repeats its block as long as its condition is True. As soon as the condition becomes False, the loop stops, and the program carries on after it.
@ snippet while count > 0:\n    print(count)\n    count = count - 1
It looks a lot like an if statement. The word while, a condition, a colon, and an indented block.
@ point Like an if that keeps coming back
In fact, you can think of a while loop as an if that keeps coming back. After running the block, Python jumps back up to the while line and checks the condition again. True? Run the block again. False? Move on.
@ flow Check the condition > True: run the block, then check again > False: carry on after the loop
As a flowchart, it's a decision diamond with an arrow that loops back. That loop back arrow is where the name comes from.
@ point The condition is checked BEFORE each repeat
The condition is checked before every repeat, including the very first one. So if the condition is False to begin with, the block never runs at all. That's why the booklet calls this a pre test loop.

## STUDY | Something must change
@ point Something inside the loop must change the condition
Here's the golden rule of while loops: something inside the loop must eventually make the condition False. Usually, that means changing a variable, like counting down, or asking the user a new question.
@ point If nothing changes: an infinite loop
If nothing changes, the condition stays True forever, and the loop never ends. That's called an infinite loop. The program looks frozen, or prints the same thing endlessly.
@ point Stuck? Press Ctrl + C to stop the program
If that happens to you, don't panic. Press control and C together to stop the program. In many editors, there's also a stop button. Every programmer has written an infinite loop at some point. It's a rite of passage!

## CODE | countdown.py
```python
count = 5
while count > 0:
    print(count, "...")
    count = count - 1
print("Lift off!")
print("count is now", count)
```
@ line 1 | Start the counter at 5
Line one starts a counter at five.
@ line 2 | Keep going while count > 0
Line two is the while loop: keep going while count is greater than zero.
@ line 3 | Print the number
Inside the loop, line three prints the current number.
@ line 4 | Count down: this makes the loop end
And line four counts down by one. This is the line that changes the condition. Without it, count would stay five forever.
@ line 5-6 | After the loop
After the loop, we print lift off, and the value of count.
@ predict 6 | How many numbers? What is count at the end?
How many numbers will be printed? And what will count be after the loop?
@ run | 5, 4, 3, 2, 1, lift off; count ends at 0
Run. Five, four, three, two, one, lift off! And count is zero. When count reached zero, the condition count greater than zero was False, so the loop stopped. Notice that zero itself was never printed.
@ edit 1 => count = 0
What if count starts at zero?
@ predict 4 | count starts at 0. Does the loop run at all?
Will the loop run at all?
@ run | False at the start: the loop never runs
Run. Straight to lift off. The condition was False the very first time it was checked, so the block never ran. That's what pre test means.

## CODE | savings.py
```python
savings = 0
goal = 50
weekly = 8
weeks = 0
while savings < goal:
    savings = savings + weekly
    weeks = weeks + 1
    print(f"Week {weeks}: {savings} coins")
print(f"Goal reached in {weeks} weeks!")
```
@ say
Here's a while loop where we don't know the answer in advance. You're saving for a game that costs fifty coins, and you save eight coins a week. How many weeks will it take?
@ line 1-4 | Savings, goal, weekly amount, and a week counter
We start with zero savings, a goal of fifty, eight coins a week, and a week counter at zero.
@ line 5 | Keep saving while we haven't reached the goal
Keep going while savings is less than the goal.
@ line 6-7 | Save, and count the week
Each time round, we add the weekly amount, and add one to the weeks.
@ line 8 | Show progress
Then we show the progress.
@ line 9 | After the loop: the answer
After the loop, we announce the number of weeks.
@ predict 6 | 8 coins a week, goal 50. How many weeks?
Before we run it, how many weeks will it take? Six weeks is forty eight coins. Is that enough?
@ run | 7 weeks: 56 coins
Run. Week one, eight coins. Up to week six, forty eight, which is still less than fifty. So the loop runs once more: week seven, fifty six. Goal reached in seven weeks! We didn't have to work out the number of repeats. The loop kept going until the job was done. That's exactly when to choose a while loop.

## CODE | password_loop.py
```python
SECRET = "mango"
guess = input("Password: ")
tries = 1
while guess != SECRET:
    print("Wrong, try again.")
    guess = input("Password: ")
    tries = tries + 1
print(f"Welcome! You got in after {tries} tries.")
```
@ input apple | banana | mango
@ say
Now a loop that keeps asking until the user gets it right.
@ line 1 | The secret password
A secret password.
@ line 2-3 | Ask once BEFORE the loop
We ask once before the loop, so that guess has a value to check. And we count that as try number one.
@ line 4 | Repeat while the guess is wrong
The loop repeats while the guess is not equal to the secret.
@ line 5-7 | Inside: ask again (this changes the condition)
Inside the loop, we say it's wrong, ask again, and add one to the tries. Asking again is what changes the condition, so the loop can end.
@ line 8 | After the loop, the guess must be right
After the loop, the guess must be right, otherwise we'd still be inside it.
@ predict 6 | apple, banana, mango. How many tries?
The user will try apple, then banana, then mango. How many times will we see wrong, try again?
@ run | Two wrong guesses, then in after 3 tries
Run. Apple: wrong, try again. Banana: wrong, try again. Mango: welcome! You got in after three tries. In lesson four point nine, we'll add a limit, so nobody can keep guessing forever.

## CODE | halving.py
```python
number = 100
steps = 0
while number > 1:
    number = number // 2
    steps = steps + 1
    print(number)
print("Steps:", steps)
```
@ say
One more example: how many times can you halve a hundred before you get down to one?
@ line 1-2 | Start at 100, no steps yet
We start with a hundred, and zero steps.
@ line 3 | Keep going while number > 1
Keep going while the number is bigger than one.
@ line 4-6 | Halve it (whole numbers), count, print
Each time, halve it with floor division, count the step, and print the new number.
@ line 7
And print the number of steps.
@ predict 6 | 100 → 50 → 25 → ...? How many steps?
A hundred, fifty, twenty five... What comes next, and how many steps will it take?
@ run | 50, 25, 12, 6, 3, 1: six steps
Run. Fifty, twenty five, twelve, six, three, one. Six steps. Twenty five halved with floor division is twelve. Halving like this is the secret behind a clever search method. If you play a guessing game and always guess the middle, you can find any number from one to a hundred in seven guesses or fewer. We'll use that in our Guess the Number project.

## STUDY | Common mistakes
@ table Mistake | What happens ; forgetting count = count - 1 | infinite loop: press Ctrl+C ; while count > 0 (no colon) | SyntaxError ; using = instead of == or != | SyntaxError ; the variable isn't set before the loop | NameError on the while line
Common while loop mistakes. Forgetting to change the variable, which causes an infinite loop. Forgetting the colon. Using one equals sign in the condition. And forgetting to give the variable a value before the loop, so Python can't check the condition the first time.

## REVISE | Quick revise
@ point while condition: repeats while it's True
A while loop repeats while its condition is True.
@ point The condition is checked before every repeat
The condition is checked before every repeat, even the first.
@ point Something inside must change, or it loops forever
Something inside the loop must change, or it loops forever.
@ point Use while when you don't know how many repeats
And use while when you don't know in advance how many repeats you'll need.

## PRACTICE | Keep asking
@ task Ask "What is 9 x 8?" and keep asking until the user types 72.\nThen print how many attempts it took.
Your turn. Ask the user what nine times eight is. Keep asking until they type seventy two. Then print how many attempts it took.
@ hint Ask once before the loop; while answer != "72": ask again and count
Hint: ask once before the loop. While the answer is not seventy two, ask again, and add one to the attempts.
@ pause 15
Pause the video and try it.

## ANSWER | keep_asking.py
```python
answer = input("What is 9 x 8? ")
attempts = 1
while answer != "72":
    answer = input("Not quite. What is 9 x 8? ")
    attempts += 1
print(f"Correct in {attempts} attempts!")
```
@ input 64 | 72
@ line 1-2
Ask once, and count one attempt.
@ line 3-5
While the answer isn't seventy two, ask again and add one, using plus equals.
@ line 6
Then celebrate.
@ run
Run. Sixty four: not quite. Seventy two: correct in two attempts! Well done!

## OUTRO
Great looping! Your programs can now keep going until a job is done. Next time, we'll go deeper into for loops, and learn range, which repeats something an exact number of times. Like, share and subscribe, and keep coding. Happy Learning!
