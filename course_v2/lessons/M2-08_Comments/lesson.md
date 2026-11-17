---
id: "2.8"
title: "Comments and Clean Code"
module: 2
module_title: "Variables, Input and Output"
next: "Mini-Project: Recipe Scaler"
minutes: 7.31
thumb_code: '# TODO: plan first!'
goals: ["Why comments matter", "Three rules for good comments", "Planning with comment stubs", "TODO notes"]
youtube:
  title: "Python Lesson 2.8: Comments, Clean Code and Planning with Stubs | Introduction to Python"
  description: |
    Code is read far more often than it is written. Ziggy the Python explains how to write helpful comments, three rules
    for good comments, and a pro trick: planning a program as comment stubs first, then filling in the code.
    Then you plan and write a screen-time calculator.
    For beginners aged 7 to 20.
  tags: [python comments, clean code, pseudocode, planning code, python for beginners, learn python, fun skill builders]
---

<!-- Booklet 2.4 Comments and code maintenance: principles, examples, stubs. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Here's a fact that surprises people: code is read far more often than it's written. Today we'll learn how to leave helpful notes in our code, and a clever trick for planning a program before we write it.

## STUDY | Why comments?
@ snippet # This is a comment. Python skips it.
We met comments in our first program. A comment starts with a hash sign, and Python skips everything after it on that line.
@ point Comments are notes for humans
Comments are for humans: your teammates, your teacher, and especially future you. Imagine opening a program you wrote three months ago. Without notes, it can feel like reading someone else's diary in code!
@ snippet total = price * 2  # two tickets
A comment can sit on its own line, or at the end of a line of code. Everything after the hash is ignored.

## STUDY | Three rules for good comments
@ point 1. Explain WHY, not just what
Rule one: explain why, not just what. The code already shows what happens. A comment like "add one to score" just repeats the code. A comment like "bonus point for finishing early" explains the reason.
@ point 2. Keep comments short and up to date
Rule two: keep comments short and up to date. If you change the code, change the comment too. A wrong comment is worse than no comment at all.
@ point 3. Good names need fewer comments
Rule three: good names reduce the need for comments. A variable called seconds per day explains itself.
@ flow Write the plan as comments > Fill in code under each step > Test it
And now a pro trick: stubs. Before writing any code, write your plan as a list of comments, one for each step. Then fill in the code under each comment, one step at a time. The comments become your to-do list, and they stay behind as documentation.
@ point Level up: # TODO marks unfinished work
Programmers often write TODO in a comment to mark something they still need to do. Many editors can even list all your TODOs for you.

## CODE | pocket_money.py
```python
# Pocket money planner
# Step 1: store the weekly pocket money
weekly = 50
# Step 2: work out a whole year (52 weeks)
yearly = weekly * 52
# Step 3: show the result
print(f"In a year you get {yearly} coins.")
# TODO: ask how much to save each week
```
@ say
Let's write a program the stub way. We'll type the plan first, then fill it in.
@ line 1 | The title comment: what this program is
Line one is a title comment. It says what the whole program is for.
@ line 2 | Step 1 of the plan
Line two is step one of our plan.
@ line 3 | Code for step 1
And line three is the code for step one: fifty coins a week.
@ line 4 | WHY 52? It's in the comment.
Line four is step two. Notice that it explains where the fifty two comes from: there are fifty two weeks in a year.
@ line 5
Line five does the multiplication.
@ line 6-7
Step three, and the code to show the result.
@ line 8 | TODO = an idea for later
And line eight is a TODO: an idea we'll add later.
@ predict 4 | Five comment lines. How many lines of output?
This program has eight lines, and five of them are comments. How many lines will appear in the output?
@ run | Comments don't change the output at all
Run it. Just one line: in a year you get two thousand six hundred coins. The comments didn't appear in the output at all. They're only for the people reading the code.

## CODE | turn_off.py
```python
print("Step 1: get ready")
print("Step 2: jump")
print("Step 3: land")
```
@ say
Comments have another superpower. Programmers use them to switch lines off for a moment, without deleting them. It's called commenting out.
@ line 1-3 | Three steps
Three print lines: get ready, jump, and land.
@ run | All three steps
Run. All three steps appear.
@ edit 2 => # print("Step 2: jump")
Now let's put a hash at the start of line two.
@ predict 4 | What will we see now?
The line is still there, but it starts with a hash. What will the output look like now?
@ run | Line 2 is switched off
Run. Only steps one and three! Python skipped line two, because it's now a comment.
@ edit 2 => print("Step 2: jump")
Remove the hash to switch it back on.
@ run | Back on again
And it's back. This is really handy when you're hunting a bug. You can switch off a few lines to see whether they cause the problem, then switch them back on, without retyping anything. Most editors have a keyboard shortcut for it, often control and forward slash.

## CODE | clean_up.py
```python
# x
x = 3
# y
y = 4
# z
z = x * y
print(z)
```
@ say
Now let's look at some bad comments, and clean them up.
@ line 1-6 | These comments add nothing
This program has a comment above every line, but look at them. Hash x. Hash y. Hash z. They tell us nothing at all.
@ line 7
And then it prints z.
@ run | 12... but 12 what?
Run. Twelve. But twelve what? The comments didn't help, and the names didn't help either.
@ edit 1 => # Garden planner: area of a rectangular flower bed
Let's fix it. The first comment now explains what the whole program is for.
@ edit 2 => width_m = 3
x becomes width in metres.
@ edit 3 => 
We delete the useless comment.
@ edit 4 => length_m = 4
y becomes length in metres.
@ edit 5 => # area = width x length (square metres)
This comment explains the formula and the units, which the code alone doesn't tell you.
@ edit 6 => area = width_m * length_m
z becomes area.
@ edit 7 => print(f"Flower bed area: {area} square metres")
And we print it with a label.
@ run | Same answer, now it explains itself
Run. Flower bed area: twelve square metres. Same answer, but now the program explains itself. One good title comment, one comment explaining the formula, and clear names. That's much better than a comment on every line.

## STUDY | Clean code habits
@ point Blank lines separate the steps
Comments are one part of clean code. Here are a few more habits. Use blank lines to separate the different steps of your program, like paragraphs in a story.
@ point Spaces around = and operators: total = a + b
Put a space on each side of equals signs and maths operators. Total equals a plus b, with spaces, is much easier to read than everything squashed together.
@ point Keep lines short
Keep your lines fairly short, so nobody has to scroll sideways to read them.
@ point Level up: """triple quotes""" for longer notes
And a level up: for a longer note, such as a description at the top of a program, you can use three quote marks at the start and three at the end. Everything between them can go over several lines. Programmers call these docstrings when they describe what a program or function does.

## REVISE | Quick revise
@ point # starts a comment; Python skips it
A hash sign starts a comment, and Python skips it.
@ point Explain why, keep it short, keep it current
Good comments explain why, and they're short and up to date.
@ point Good names need fewer comments
Good names mean you need fewer comments.
@ point Plan with comment stubs, then fill in the code
And you can plan a program with comment stubs, then fill in the code.

## PRACTICE | Screen time planner
@ task Plan with comments first, then code: a person uses a tablet for 45 minutes a day. Print how many minutes that is in a week, and how many whole hours.
Your turn, and use the stub method. First write your plan as comments. Then fill in the code. Someone uses a tablet for forty five minutes a day. Print how many minutes that is in a week, and how many whole hours.
@ hint Steps: store daily minutes, times 7, then // 60 for whole hours
Hint: step one, store the daily minutes. Step two, multiply by seven. Step three, floor divide by sixty for the whole hours. Step four, print.
@ pause 15
Pause the video and plan it out.

## ANSWER | screen_time.py
```python
# Screen time planner
# Step 1: minutes per day
daily = 45
# Step 2: minutes per week
weekly = daily * 7
# Step 3: whole hours per week
hours = weekly // 60
# Step 4: show the results
print(f"{weekly} minutes a week, about {hours} whole hours.")
```
@ line 1-2
A title, then step one of the plan.
@ line 3
Forty five minutes a day.
@ line 4-5
Step two: times seven for a week.
@ line 6-7
Step three: floor divide by sixty for whole hours.
@ line 8-9
And step four prints it all.
@ run
Three hundred and fifteen minutes a week, about five whole hours. Your comments might use different words, and that's fine. What matters is that someone else could read your plan and understand it.

## OUTRO
Nicely done! Your code is now clean and easy to understand. Next time, we'll put all of Module Two together in a mini-project: a recipe scaler that works out ingredients for any number of people. Like, share and subscribe, and keep coding. Happy Learning!
