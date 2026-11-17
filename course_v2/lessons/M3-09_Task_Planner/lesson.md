---
id: "3.9"
title: "Mini-Project: Daily Task Planner"
module: 3
module_title: "Data Structures"
next: "Sequence and Flowcharts"
minutes: 8.05
thumb_code: 'tasks.append(task)'
goals: ["Choose the right data structure", "Store tasks as a list of records", "Totals and counts with a loop", "Build and test a project in stages"]
youtube:
  title: "Python Lesson 3.9: Mini-Project - Daily Task Planner with Lists and Dictionaries | Introduction to Python"
  description: |
    Module 3 project! Ziggy the Python designs a daily task planner: choosing the right data structure, storing
    tasks as a list of dictionaries, printing a checklist, totalling the minutes, counting finished jobs, adding a
    new task from input, and working out the time left in the day.
    For beginners aged 7 to 20.
  tags: [python project for beginners, python list of dictionaries project, task planner python, learn python, fun skill builders]
---

<!-- Booklet chapter 3 case study: Daily Tasks. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. It's project time again! We're going to build a daily task planner, a small program that keeps track of the jobs you need to do today, how long each one takes, and which ones are finished. It uses lists, dictionaries, loops and input, all working together.

## STUDY | The design brief
@ point Store today's tasks: name, minutes, done or not
Every project starts with a brief: a description of what the program must do. Our planner must store today's tasks. For each task, it needs a name, how many minutes it will take, and whether it's done yet.
@ point Show a checklist with ticks
It should show a checklist, with a mark for each finished task.
@ point Total time, tasks done, time left
It should work out the total time for all the tasks, how many are done, and how much time is left today.
@ point Let the user add a new task
And it should let the user add a new task by typing it in.

## STUDY | Choosing a data structure
@ table Option | Good? ; three separate lists: names, minutes, done | easy to get out of step ; one dictionary: name → minutes | nowhere to store done ; a list of dictionaries | each task is one record ✔
Before writing any code, we need to choose how to store the data. We could use three separate lists, one for names, one for minutes and one for done. But it's easy to get them out of step: delete a name and forget the minutes, and everything's wrong. We could use one dictionary of names and minutes, but then there's nowhere to store whether a task is done.
@ point Each task is a record: {"name": ..., "minutes": ..., "done": ...}
The best choice is the one from lesson three point seven: a list of records. Each task is a dictionary with three fields: name, minutes and done. And the list holds all the tasks, in order.
@ point Plan the steps as comments first
And just like in lesson two point eight, we'll plan the steps as comments, then build and test one step at a time.

## CODE | planner_v1.py
```python
# Daily task planner - step 1: the data
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Practise piano", "minutes": 20, "done": False},
    {"name": "Walk the dog", "minutes": 30, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
for task in tasks:
    mark = "x" if task["done"] else " "
    print(f"[{mark}] {task['name']} ({task['minutes']} min)")
```
@ line 1 | Step 1: the data
Step one: the data. A title comment says what this program is.
@ line 2-7 | A list of four task records
Lines two to seven make a list of four tasks. Each task is a dictionary with a name, the minutes, and done, which is a boolean, True or False.
@ line 8 | Loop through the tasks
Line eight loops through the tasks.
@ line 9 | A short if: "x" if done, otherwise a space
Line nine is a compact way of choosing between two values. Mark is an x if the task is done, otherwise a space. You read it just like English: x, if done, else a space. We'll learn the full if statement in the next module.
@ line 10 | Print a checklist line
Line ten prints a checklist line: the mark in square brackets, the task's name, and the minutes in round brackets.
@ predict 5 | Which tasks will be ticked?
Which tasks will have an x next to them?
@ run | A checklist from the data
Run. A neat checklist. Homework and walk the dog are ticked, and piano and reading are still to do.

## CODE | planner_v2.py
```python
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Practise piano", "minutes": 20, "done": False},
    {"name": "Walk the dog", "minutes": 30, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
total = 0
done_count = 0
left = 0
for task in tasks:
    total += task["minutes"]
    if task["done"]:
        done_count += 1
    else:
        left += task["minutes"]
print(f"{len(tasks)} tasks, {total} minutes in total")
print(f"Done: {done_count} of {len(tasks)}")
print(f"Still to do: {left} minutes")
```
@ say
Step two: the numbers. We'll add up the total time, count the finished tasks, and add up the time still needed.
@ line 1-6 | The same tasks
The same four tasks.
@ line 7-9 | Three counters, all starting at 0, BEFORE the loop
Three variables, all starting at zero, before the loop: the total minutes, the number of tasks done, and the minutes left.
@ line 10-11 | Every task adds to the total
Inside the loop, every task's minutes are added to the total, using plus equals.
@ line 12-13 | Done? Count it
If the task is done, we add one to the done count.
@ line 14-15 | Not done? Its minutes are still to do
Otherwise, its minutes are added to the time left.
@ line 16-18 | Report after the loop
After the loop, three lines report the results.
@ predict 7 | Work out the total, done count and time left
Before we run, work out all three numbers from the list. Total minutes, tasks done, and minutes still to do.
@ run | 115 minutes; 2 of 4 done; 45 minutes left
Run. Four tasks, one hundred and fifteen minutes in total. Done: two of four. Still to do: forty five minutes, that's twenty for piano and twenty five for reading. Did you get them all right?

## CODE | planner_v3.py
```python
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
name = input("New task: ")
minutes = int(input("How many minutes? "))
tasks.append({"name": name, "minutes": minutes, "done": False})
tasks[1]["done"] = True
for task in tasks:
    mark = "x" if task["done"] else " "
    print(f"[{mark}] {task['name']} ({task['minutes']} min)")
```
@ input Tidy desk | 15
@ say
Step three: adding a task from the keyboard, and ticking one off. To keep the screen tidy, this version starts with just two tasks.
@ line 1-4 | Start with two tasks
Two tasks to start with.
@ line 5 | Ask for the name
Line five asks for the new task's name.
@ line 6 | Ask for the minutes, as a number
Line six asks how many minutes it takes, converted to a whole number with int.
@ line 7 | Build a new record and append it
Line seven builds a new record, a dictionary, right inside the brackets of append. New tasks always start as not done.
@ line 8 | Tick off task 1: change a field
Line eight ticks off task one, which is Read. It changes the done field to True.
@ line 9-11 | Print the checklist again
Then the same checklist loop as before.
@ predict 6 | What will the checklist show now?
I'll add a task called tidy desk, taking fifteen minutes. What will the checklist look like?
@ run | A new task added, Read ticked off
Run. Tidy desk, fifteen. And the checklist now shows homework and read both ticked, and our new task, tidy desk, waiting to be done.

## CODE | time_left.py
```python
DAY_START = 16 * 60
BEDTIME = 21 * 60
free = BEDTIME - DAY_START
planned = 40 + 20 + 30 + 25
spare = free - planned
print(f"Free time: {free} minutes")
print(f"Planned: {planned} minutes")
print(f"Spare: {spare // 60} h {spare % 60} min")
```
@ say
One last feature: how much free time is left in the day? Let's say school finishes at four o'clock, and bedtime is nine o'clock.
@ line 1-2 | Times as minutes after midnight
We store both times as minutes after midnight. Four o'clock in the afternoon is hour sixteen, times sixty. Bedtime is hour twenty one, times sixty. Writing it as a calculation makes it easy to read and change.
@ line 3 | Free minutes between them
Line three finds the free minutes between them.
@ line 4 | The four tasks' minutes
Line four adds up our four tasks' minutes.
@ line 5 | Spare = free - planned
Line five works out the spare time.
@ line 6-8 | Hours and minutes with // and %
And three prints, the last one using floor division and modulo to turn minutes into hours and minutes, from lesson two point six.
@ predict 6 | 5 hours free, 115 minutes planned. How much spare?
Five hours is three hundred minutes. Take away one hundred and fifteen. How much spare time is that, in hours and minutes?
@ run | 185 minutes spare = 3 h 5 min
Run. Free time: three hundred minutes. Planned: one hundred and fifteen. Spare: three hours and five minutes. Plenty of time for some coding practice!

## STUDY | Ideas to extend it
@ point Sort tasks by minutes: tasks.sort(key=...) (level up)
Here are some ideas to take your planner further. Older learners could look up how to sort the list of tasks by minutes, so the quickest jobs come first.
@ point Add a "priority" field: high, medium, low
Add a priority field to every task, and print the high priority tasks first.
@ point Warn if the plan doesn't fit in the day
And once you know if statements, from the next module, print a warning when the planned time is longer than the free time.

## REVISE | Quick revise
@ point Start with a brief, then choose a data structure
We started with a brief, then chose the right data structure.
@ point A list of dictionaries: one record per task
A list of dictionaries gave us one record per task.
@ point Counters before the loop; update them inside
Counters started before the loop, and changed inside it.
@ point Build in steps, and test each step
And we built the program in steps, testing each one.

## PRACTICE | Time left
@ task Using the four tasks from step 2:\n1. Add a fifth task: "Tidy room", 15 minutes, not done\n2. Print how many tasks are NOT done and the minutes they need
Your turn. Start with the four tasks from step two. Append a fifth task: tidy room, fifteen minutes, not done. Then use a loop to print how many tasks are not done yet, and how many minutes they need altogether.
@ hint not_done = 0 and minutes_left = 0 before the loop; if not task["done"]: ...
Hint: start two counters at zero before the loop. Inside the loop, if not task done, add to both.
@ pause 15
Pause the video and give it a go.

## ANSWER | still_to_do.py
```python
tasks = [
    {"name": "Homework", "minutes": 40, "done": True},
    {"name": "Practise piano", "minutes": 20, "done": False},
    {"name": "Walk the dog", "minutes": 30, "done": True},
    {"name": "Read", "minutes": 25, "done": False},
]
tasks.append({"name": "Tidy room", "minutes": 15, "done": False})
not_done = 0
minutes_left = 0
for task in tasks:
    if not task["done"]:
        not_done += 1
        minutes_left += task["minutes"]
print(f"{not_done} tasks to go, {minutes_left} minutes")
```
@ line 1-6
The four tasks.
@ line 7
Append the new one.
@ line 8-9
Two counters before the loop.
@ line 10-13
If the task is not done, add one to the count and add its minutes.
@ line 14
And print the result.
@ run
Run. Three tasks to go, sixty minutes. Piano, reading and tidying: twenty plus twenty five plus fifteen. Fantastic work!

## OUTRO
Congratulations, you've finished Module Three! You can now organise data with lists, dictionaries, tuples and sets. Next time, Module Four begins, and our programs will start making decisions and repeating actions. We'll start with flowcharts. Like, share and subscribe, and keep coding. Happy Learning!
