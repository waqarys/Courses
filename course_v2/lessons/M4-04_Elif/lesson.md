---
id: "4.4"
title: "elif: Many Choices"
module: 4
module_title: "Making Decisions and Loops"
next: "Complex and Nested Conditions"
minutes: 6.53
thumb_code: 'elif score >= 70:'
goals: ["More than two choices with elif", "The first True condition wins", "Why the order of conditions matters", "Using else as a catch-all"]
youtube:
  title: "Python Lesson 4.4: elif - Choosing Between Many Options | Introduction to Python"
  description: |
    When two paths aren't enough, use elif! Ziggy the Python explains the if / elif / else ladder, why only the
    first True condition runs, and why the order of your conditions matters so much. We build a grade calculator,
    break it by putting the conditions in the wrong order, fix it, and make a weather-to-clothes adviser.
    For beginners aged 7 to 20.
  tags: [python elif, if elif else python, grade calculator python, python decisions, learn python, fun skill builders]
---

<!-- Booklet chapter 4: selection (if/elif/else). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Life is full of choices with more than two options. Is the traffic light red, amber or green? Is your grade an A, B, C or D? Today we'll learn elif, which lets a program choose between as many options as it needs.

## STUDY | A ladder of questions
@ snippet if score >= 90:\n    grade = "A"\nelif score >= 70:\n    grade = "B"\nelse:\n    grade = "C"
Elif is short for else if. You put it between an if and an else, and you can have as many elifs as you like. Each one has its own condition and its own block.
@ point Python checks from the TOP, one rung at a time
Think of it as a ladder of questions. Python starts at the top rung and asks the first question. If the answer is no, it climbs down to the next rung and asks that question, and so on.
@ point The FIRST True condition wins, and the rest are skipped
As soon as one condition is True, Python runs that block, and skips all the rest of the ladder. Even if later conditions would also be True, they're never checked.
@ point else at the bottom catches everything else
The else at the bottom is optional. It's the catch all: it runs only if every condition above it was False.
@ point Exactly one block runs (if there's an else)
So with an else at the bottom, exactly one block of the whole ladder runs. Without an else, it's possible that none of them run.

## STUDY | Order matters
@ point Put the most specific conditions FIRST
Because the first True condition wins, the order of the rungs really matters. Usually, you should put the most specific or highest condition first.
@ table Score | Grade ; 90 or more | A ; 70 to 89 | B ; 50 to 69 | C ; below 50 | D
Here are the grade boundaries we'll use. Ninety or more is an A. Seventy to eighty nine is a B. Fifty to sixty nine is a C. Below fifty is a D.
@ point Checking >= 90 first means elif >= 70 only sees scores below 90
If we check ninety or more first, then by the time Python reaches the B question, it already knows the score is below ninety. So we only need to ask: is it at least seventy? The ladder does part of the work for us.

## CODE | grades.py
```python
score = int(input("Score out of 100: "))
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "D"
print(f"A score of {score} is a grade {grade}")
```
@ input 76
@ line 1 | Ask for a score
Line one asks for a score.
@ line 2-3 | Top rung: 90 or more?
The top rung: ninety or more is an A.
@ line 4-5 | elif: 70 or more?
Then elif: seventy or more is a B.
@ line 6-7 | elif: 50 or more?
Another elif: fifty or more is a C.
@ line 8-9 | else: everything else
And else catches everything else: a D.
@ line 10 | After the ladder
After the ladder, we print the result.
@ predict 5 | 76 is more than 50 AND more than 70. Which grade?
The score is seventy six. That's more than seventy and more than fifty, so two conditions are True. Which grade will we get?
@ run | First True wins: B
Run. Grade B. Python checked ninety or more: False. Then seventy or more: True! So it set grade to B, and skipped the rest. The fifty or more condition was never even checked.

## CODE | wrong_order.py
```python
score = 95
if score >= 50:
    grade = "C"
elif score >= 70:
    grade = "B"
elif score >= 90:
    grade = "A"
print(score, "->", grade)
```
@ say
Now let's see what happens when the rungs are in the wrong order.
@ line 1 | An excellent score: 95
An excellent score: ninety five.
@ line 2-3 | Lowest boundary first...
This time, the first question is: fifty or more?
@ line 4-7 | ...then 70, then 90
Then seventy, then ninety.
@ line 8
And print the grade.
@ predict 5 | 95 should be an A. Is it?
Ninety five should definitely be an A. Will it be?
@ run | Bug: 95 gets a C!
Run. Ninety five gets a C! The first question was fifty or more, which is True, so Python gave a C and never looked at the other rungs. No error message, just a wrong answer. That's a logic error caused by the order.
@ edit 2 => if score >= 90:
Let's fix it by putting the highest boundary first.
@ edit 3 =>     grade = "A"
That gives an A.
@ edit 6 => elif score >= 50:
And the fifty check moves to the bottom.
@ edit 7 =>     grade = "C"
That gives a C.
@ run | Fixed: highest boundary first
Run. Ninety five gets an A. When you write a ladder, always ask: could a later condition ever be reached? If an earlier one would always catch it first, the order is wrong.

## CODE | weather.py
```python
temp = int(input("Temperature in °C: "))
if temp >= 30:
    advice = "shorts, a hat and water"
elif temp >= 20:
    advice = "a T-shirt"
elif temp >= 10:
    advice = "a jumper"
elif temp >= 0:
    advice = "a coat and scarf"
else:
    advice = "everything! It's freezing"
print(f"At {temp}°C, wear {advice}.")
```
@ input 14
@ say
Here's another ladder: a clothes adviser that uses the temperature.
@ line 1 | Ask for the temperature
Line one asks for the temperature in degrees Celsius.
@ line 2-9 | Four rungs, hottest first
Then four rungs, from hottest to coldest: thirty or more, twenty or more, ten or more, and zero or more. Each one stores some advice.
@ line 10-11 | Below zero: the catch-all
Anything below zero falls through to the else.
@ line 12 | One print at the end
And one print at the end uses whichever advice was chosen. Storing the result in a variable and printing it once is neater than putting a print in every block.
@ predict 5 | 14 degrees. What should we wear?
It's fourteen degrees. What will the advice be?
@ run | 14 → a jumper
Run. At fourteen degrees, wear a jumper. Fourteen is not thirty or more, not twenty or more, but it is ten or more. Try a negative number in your own editor, like minus three, and you'll see the else in action.

## STUDY | Common mistakes
@ table Mistake | What happens ; else if score > 70: | SyntaxError: write elif ; elif after else | SyntaxError: else must be last ; conditions in the wrong order | later rungs are never reached ; a new if instead of elif | both blocks may run
Here are the classic elif mistakes. Writing else if as two words, which Python doesn't accept. Putting an elif after the else, when else must always be last. Putting conditions in the wrong order, so later rungs can never be reached. And starting a new if when you meant elif, which breaks the ladder into separate questions.

## REVISE | Quick revise
@ point if / elif / elif / else: a ladder of questions
If, elif and else make a ladder of questions.
@ point Python checks from the top; the first True wins
Python checks from the top, and the first True condition wins.
@ point Order matters: most specific (or highest) first
Order matters, so put the most specific or highest condition first.
@ point else is the optional catch-all at the bottom
And else is the optional catch all at the bottom.

## PRACTICE | Traffic light
@ task Ask for a traffic light colour (red, amber or green).\nred → "Stop"   amber → "Get ready"   green → "Go"\nanything else → "That's not a traffic light colour!"\nBonus: make it work for RED and Red too.
Your turn. Ask the user for a traffic light colour. If it's red, print stop. If it's amber, print get ready. If it's green, print go. And for anything else, print that's not a traffic light colour. For a bonus, make it work even if the user types capital letters.
@ hint colour = input(...).lower(); if colour == "red": ... elif ... else
Hint: use dot lower on the input, then an if, two elifs and an else.
@ pause 15
Pause the video and give it a go.

## ANSWER | traffic_light.py
```python
colour = input("Light colour? ").lower()
if colour == "red":
    print("Stop")
elif colour == "amber":
    print("Get ready")
elif colour == "green":
    print("Go")
else:
    print("That's not a traffic light colour!")
```
@ input Amber
@ line 1
Ask for the colour, and make it lower case straight away, for the bonus.
@ line 2-7
An if and two elifs, one for each colour.
@ line 8-9
And else for anything else.
@ run
Run with Amber, with a capital A. Get ready. The dot lower turned it into amber first, so the comparison matched. Well done!

## OUTRO
Fantastic! You can now build ladders of decisions with elif. Next time, we'll combine conditions with and, or and not, and put decisions inside other decisions. Like, share and subscribe, and keep coding. Happy Learning!
