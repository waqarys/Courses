---
id: "5.6"
title: "Final Project: Big Five Wellbeing Check-In"
module: 5
module_title: "Next Steps"
next: ""
minutes: 11.7
thumb_code: 'ratings[area] = get_rating(area)'
goals: ["Turn a design brief into a plan", "Plan with stubs, then build one piece at a time", "Combine functions, loops, validation, a dictionary and if/elif", "Test the finished program"]
youtube:
  title: "Python Lesson 5.6: Final Project - Big Five Wellbeing Check-In | Introduction to Python"
  description: |
    The grand finale! Ziggy the Python builds a complete program from a design brief: a Big Five Wellbeing
    Check-In that asks for 1 to 5 ratings for sleep, food, movement, friends and feelings, rejects bad answers
    with a validation loop, stores everything in a dictionary, works out the total and average, draws a star
    chart and gives friendly feedback. We plan with stubs, build piece by piece, and test as we go.
    For beginners aged 7 to 20.
  tags: [python project, python final project, beginner python project, wellbeing check in python, learn python, fun skill builders]
---

<!-- Final project, pulling together modules 1 to 5. The feedback is friendly and general, never a diagnosis. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. This is it: the final project! We're going to build a complete program from start to finish, called the Big Five Wellbeing Check-In. It uses almost everything from this course: input, variables, lists, dictionaries, loops, if and elif, validation and functions. Just like real programmers, we'll start with a design brief, make a plan, and build it one piece at a time, testing as we go.

## STUDY | The design brief
@ point A quick check-in on 5 areas of everyday wellbeing
Here's the brief. Make a quick, friendly check-in, where someone rates five areas of their week.
@ boxes Sleep | Food | Movement | Friends | Feelings
The Big Five areas are: sleep, food, movement, friends and feelings.
@ point Each area gets a rating from 1 (not great) to 5 (great)
Each area gets a rating from one, meaning not great, to five, meaning great.
@ point Reject anything that isn't a whole number from 1 to 5
The program must reject any answer that isn't a whole number from one to five, and ask again.
@ point Show a star chart, the total, the average and friendly feedback
At the end, it shows a star chart, the total and average, a friendly message, and which area might need a little extra care.
@ point It's a reflection tool, not a test. There are no wrong answers.
And one important design choice. This is a reflection tool, not a test. There are no wrong answers, and the messages should always be kind.

## STUDY | Breaking it down
@ flow Ask for each area's rating (with validation) > Store the ratings in a dictionary > Work out the total and average > Show a star chart > Choose friendly feedback
A big program feels scary, until you break it into smaller jobs. This is called decomposition. First, ask for each rating, checking it's valid. Store the ratings in a dictionary. Work out the total and average. Show a star chart. And choose some friendly feedback.
@ table Job | Python tool ; list of the five areas | a list ; ask until the answer is valid | a while loop in a function ; area → rating | a dictionary ; total and average | sum() and len() ; feedback | if / elif / else in a function
For each job, we can pick a tool we already know. A list for the areas. A while loop inside a function for asking until the answer is valid. A dictionary to link each area to its rating. Sum and len for the total and average. And an if, elif ladder, inside another function, for the feedback.

## CODE | checkin_plan.py
```python
# Big Five Wellbeing Check-In: the plan
AREAS = ["Sleep", "Food", "Movement", "Friends", "Feelings"]

def get_rating(area):
    # TODO: ask until we get a whole number from 1 to 5
    return 3

def feedback(average):
    # TODO: choose a friendly message
    return "Feedback goes here"

print("Areas:", AREAS)
print("Sleep rating:", get_rating("Sleep"))
print(feedback(3))
```
@ say
Step one: the plan. We write the skeleton of the program first, using something called stubs.
@ line 1 | A title comment
A title comment.
@ line 2 | The five areas, as a constant list
Line two stores the five areas in a list. It's in capitals, because it's a constant that won't change.
@ line 4-6 | A stub: the right shape, a fake answer
Lines four to six are a stub. It's a function with the right name and parameter, but instead of the real work, it just returns three for now. The to do comment reminds us what it should really do.
@ line 8-10 | A second stub
Lines eight to ten are another stub, for the feedback.
@ line 12-14 | A smoke test of the plan
And lines twelve to fourteen call everything, as a quick smoke test.
@ predict 4 | It doesn't do anything real yet. Will it run?
Nothing real happens yet. Will it run without errors?
@ run | The skeleton works
Run. The areas, a rating of three, and feedback goes here. The skeleton works! Now we can replace each stub with real code, one at a time, and test each one as we go. If something breaks, we'll know exactly which piece caused it.

## CODE | get_rating.py
```python
def get_rating(area):
    while True:
        answer = input(f"{area} (1-5): ")
        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)
        print("Please type a whole number from 1 to 5.")

rating = get_rating("Sleep")
print("You chose", rating)
```
@ input 7 | three | 4
@ say
Step two: the real get rating function. This is our validation loop.
@ line 1 | One parameter: which area we're asking about
Get rating takes one parameter: the name of the area.
@ line 2 | Keep asking forever... until we return
Line two is a while True loop. It would repeat forever, but return will end it as soon as we get a good answer.
@ line 3 | Ask, showing the area's name
Line three asks the question, using the area's name in an F string.
@ line 4 | Digits only AND between 1 and 5?
Line four checks two things, joined with and. Is the answer made only of digits? And is the number between one and five? Because and checks the left side first, int is only used when the answer really is digits, so letters can't crash the program.
@ line 5 | Valid: return the number, ending the loop and the function
If both are true, line five returns the number, which ends the loop and the function at once.
@ line 6 | Otherwise, explain and loop again
Otherwise, line six explains what we need, and the loop goes round again.
@ line 8-9 | Test it
Lines eight and nine test it.
@ predict 6 | Inputs: 7, then "three", then 4. What happens?
Our test inputs are seven, then the word three, then four. What will happen?
@ run | Two rejections, then 4 is accepted
Run. Seven: please type a whole number from one to five. Three, in words: rejected too, and no crash. Four: accepted. You chose four. We tested an out-of-range number and a word, and the function coped with both.

## CODE | feedback.py
```python
def feedback(average):
    if average >= 4:
        return "You're having a great week. Keep it up!"
    elif average >= 3:
        return "A good week. Maybe give one area some extra care."
    elif average >= 2:
        return "A tricky week. Be kind to yourself."
    else:
        return "That sounds hard. Talk to someone you trust."

for test in [4.6, 4, 3.2, 2.5, 1.4]:
    print(test, "->", feedback(test))
```
@ say
Step three: replace the feedback stub with an if, elif ladder.
@ line 1-3 | 4 or more: great
Four or more gets: you're having a great week, keep it up.
@ line 4-5 | 3 or more: good
Three or more: a good week, maybe give one area some extra care.
@ line 6-7 | 2 or more: tricky
Two or more: a tricky week, be kind to yourself.
@ line 8-9 | Below 2: talk to someone you trust
And anything lower: that sounds hard, talk to someone you trust. Talking to a friend, a family member or a teacher really does help.
@ line 11-12 | Test every branch, including the boundary 4
Lines eleven and twelve test every branch, including exactly four, which is a boundary.
@ predict 6 | Which message does exactly 4 get?
Remember from the elif lesson: the first true condition wins. Which message will exactly four get?
@ run | Every branch works
Run. Four point six and exactly four both get the great message, because four is greater than or equal to four. Three point two is good, two point five is tricky, and one point four gets the gentle suggestion to talk to someone. Every branch tested.

## CODE | wellbeing_checkin.py
```python
AREAS = ["Sleep", "Food", "Movement", "Friends", "Feelings"]

def get_rating(area):
    while True:
        answer = input(f"{area} (1-5): ")
        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)
        print("Please type a whole number from 1 to 5.")

def feedback(average):
    if average >= 4:
        return "You're having a great week. Keep it up!"
    elif average >= 3:
        return "A good week. Maybe give one area some extra care."
    elif average >= 2:
        return "A tricky week. Be kind to yourself."
    else:
        return "That sounds hard. Talk to someone you trust."

print("=== Big Five Wellbeing Check-In ===")
ratings = {}
for area in AREAS:
    ratings[area] = get_rating(area)

total = sum(ratings.values())
average = total / len(ratings)

lowest = AREAS[0]
for area in AREAS:
    if ratings[area] < ratings[lowest]:
        lowest = area

for area, score in ratings.items():
    print(area, "*" * score)
print(f"Total: {total} out of 25")
print("Average:", round(average, 1))
print(feedback(average))
print("Area to give extra care:", lowest)
```
@ input 4 | 6 | 3 | 5 | 2 | 4
@ say
Step four: put it all together. The two finished functions go at the top, and the main program goes underneath.
@ line 1 | The five areas
Line one is our list of areas.
@ line 3-8 | get_rating, tested in step 2
Lines three to eight are get rating, exactly as we tested it.
@ line 10-18 | feedback, tested in step 3
Lines ten to eighteen are feedback, also already tested.
@ line 20 | A title
Now the main program. Line twenty prints a title.
@ line 21 | An empty dictionary for the ratings
Line twenty one makes an empty dictionary to hold the ratings.
@ line 22-23 | For each area: ask, and store area → rating
Lines twenty two and twenty three loop through the areas. For each one, we call get rating, and store the answer in the dictionary, with the area's name as the key.
@ line 25 | Add up all the ratings
Line twenty five adds up all the values in the dictionary.
@ line 26 | The average: total ÷ how many
Line twenty six divides the total by how many ratings there are, to get the average.
@ line 28-31 | Find the lowest-rated area
Lines twenty eight to thirty one find the area with the lowest rating. We start by guessing the first area, then check each one. If an area's rating is lower than our current lowest, it becomes the new lowest.
@ line 33-34 | A star chart: one star per point
Lines thirty three and thirty four draw a star chart. For each area and score in the dictionary, print the name, and that many stars, using string repetition.
@ line 35-36 | Total and average
Lines thirty five and thirty six show the total out of twenty five, and the average, rounded.
@ line 37 | The friendly message
Line thirty seven chooses the friendly message.
@ line 38 | And the area that could use some care
And line thirty eight names the area that could use some extra care.
@ predict 8 | Sleep 4, Food 6 then 3, Movement 5, Friends 2, Feelings 4
Let's test it. The answers will be: sleep four. For food, six, which should be rejected, then three. Movement five, friends two, and feelings four. Can you work out the total, the average and the message before we run it?
@ run | Total 18, average 3.6, extra care for Friends
Run. Each area is asked in turn, and the six is rejected with our friendly message. Then the star chart: four stars for sleep, three for food, five for movement, two for friends and four for feelings. A total of eighteen out of twenty five. An average of three point six, which gives: a good week, maybe give one area some extra care. And the area to give extra care is friends. Perhaps it's time to message a friend, or plan something fun together.

## STUDY | Testing the finished program
@ table Test | Inputs | Expected ; all great | 5 5 5 5 5 | total 25, great message ; all low | 1 1 1 1 1 | total 5, talk to someone ; boundary average | 4 4 4 4 4 | average 4.0, great message ; invalid answers | 0, 9, ten, 3.5 | each rejected, asked again
A finished program still needs a test plan. All fives should give twenty five and the great message. All ones should give five and the gentle message. All fours sits right on the boundary, and should give the great message. And invalid answers, like zero, nine, the word ten, or three point five, should each be rejected. Try all of these at home.
@ point Three point five has a dot, so .isdigit() says False and asks again
Did you notice three point five? It contains a dot, so is digit returns False, and the program asks again. Exactly what our brief asked for: whole numbers only.

## STUDY | What you've built
@ boxes input & f-strings | lists & dictionaries | for & while loops | if / elif / else | functions & return | validation & testing
Take a moment to look at what you've just built. Input and F strings, from module two. Lists and dictionaries, from module three. For and while loops, and if, elif and else, from module four. Functions, return values, validation and testing, from module five. That's a real, useful program, and you understand every single line of it.

## STUDY | Common mistakes
@ table Mistake | What happens ; forgetting return in get_rating | every rating is None, and sum() fails ; int(answer) before checking isdigit() | ValueError for letters ; dividing by 5 instead of len(ratings) | wrong average if you add an area ; feedback checks >= 2 before >= 4 | everyone gets the "tricky" message
Common project mistakes. Forgetting return in get rating, so every rating is None. Using int before checking the answer is digits, which crashes on letters. Dividing by five instead of len, which breaks when you add an area. And putting the ladder in the wrong order, so everyone gets the same message.

## REVISE | Quick revise
@ point Brief → break it down → plan with stubs → build → test
Start with a brief, break it down, plan with stubs, build one piece at a time, and test.
@ point Stubs let you test the shape before the details
Stubs let you test the shape of a program before writing the details.
@ point Test each function on its own, then the whole program
Test each function on its own, then the whole program.
@ point Big programs are just small pieces, joined together
And remember: big programs are just small pieces, joined together.

## PRACTICE | Make it your own
@ task 1. Add a sixth area, such as "Fun" or "Learning". (Update the total message: it's now out of 30.)\n2. Weekly average: given week = [3.6, 4.0, 2.8, 3.4, 4.2, 4.4, 3.9], print the average for the whole week, rounded to 1 decimal place.
Your final challenge has two parts. First, add a sixth area to the check-in, like fun or learning. Think about what else needs to change. Hint: the total is now out of thirty. Second, add a weekly average. Here's a list of seven daily averages. Write a function that returns their average, and print it, rounded to one decimal place.
@ hint Use len(AREAS) * 5 for the maximum, and sum(week) / len(week) for the weekly average
Hint: instead of typing thirty, use len of areas times five, so it's always right. And the weekly average is the sum of the list, divided by its length.
@ pause 20
Pause the video and give it a go. Take your time. This is your project now.

## ANSWER | my_checkin.py
```python
AREAS = ["Sleep", "Food", "Movement", "Friends", "Feelings", "Fun"]

def get_rating(area):
    while True:
        answer = input(f"{area} (1-5): ")
        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)
        print("Please type a whole number from 1 to 5.")

def weekly_average(days):
    return sum(days) / len(days)

ratings = {}
for area in AREAS:
    ratings[area] = get_rating(area)
total = sum(ratings.values())
print(f"Total: {total} out of {len(AREAS) * 5}")
print("Average:", round(total / len(ratings), 1))

week = [3.6, 4.0, 2.8, 3.4, 4.2, 4.4, 3.9]
print("Weekly average:", round(weekly_average(week), 1))
```
@ input 4 | 3 | 5 | 2 | 4 | 5
@ line 1
The list now has six areas, including fun. Because everything else loops over the list, the program asks about fun automatically.
@ line 3-8
Get rating is unchanged.
@ line 10-11
A new function returns the average of any list of numbers.
@ line 13-15
The ratings are collected exactly as before.
@ line 16-18
The total is now shown out of len of areas times five, which is thirty, and the average divides by len, so it's still right.
@ line 20-21
And the weekly average uses our new function.
@ run
Run. Six questions, a total of twenty three out of thirty, an average of three point eight, and a weekly average of three point eight too. You may have built it differently, and that's great, as long as it works and you can explain it.

## OUTRO
Congratulations, Happy Learners! You've finished Introduction to Python. You started with a single print line, and now you can plan, build and test complete programs. Keep practising, keep building your own projects, and keep being curious. I'm so proud of you. This has been Ziggy the Python. Like, share and subscribe, and keep coding. Happy Learning!
