---
id: "4.3"
title: "if / else"
module: 4
module_title: "Making Decisions and Loops"
next: "elif: Many Choices"
minutes: 5.81
thumb_code: 'else:'
goals: ["Two paths: exactly one runs", "else has no condition", "Even or odd with %", "Choosing between if/else and two ifs"]
youtube:
  title: "Python Lesson 4.3: if and else - Two Paths in Python | Introduction to Python"
  description: |
    Give your program two paths! Ziggy the Python explains if and else, why exactly one of the two blocks always
    runs, and how else needs no condition. We build an even-or-odd checker with the remainder operator, a quiz
    question that marks your answer, and a pass/fail checker, and compare if/else with two separate ifs.
    For beginners aged 7 to 20.
  tags: [python if else, python else statement, even or odd python, python decisions, learn python, fun skill builders]
---

<!-- Booklet chapter 4: selection (if/else). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Last time, our if statements did something when the answer was yes, and nothing when it was no. But often we want something different to happen when the answer is no. Today we'll learn else, which gives a program two paths to choose between.

## STUDY | Two paths
@ flow Is the number even? > Yes: print "even" / No: print "odd" > Carry on
Picture the decision diamond again, but this time both arrows lead to an action. If the number is even, print even. Otherwise, print odd. Then both paths join up again and the program carries on.
@ point Exactly ONE of the two blocks runs, every time
With if and else, exactly one of the two blocks runs, every single time. Never both, and never neither. It's like a fork in a path through a forest: you must take one branch or the other.
@ snippet if score >= 50:\n    print("Pass")\nelse:\n    print("Try again")
In Python, the else goes at the same indentation as the if, followed by a colon. Its block is indented underneath it.
@ point else has NO condition: it means "otherwise"
Notice that else has no condition. It simply means otherwise. It catches every case where the if condition was False.
@ point else must come straight after the if block
And else must come straight after the if block. It belongs to that if, like a partner.

## CODE | even_odd.py
```python
number = int(input("Pick a whole number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
print("Thanks for playing!")
```
@ input 7
@ line 1 | Ask for a whole number
Line one asks for a whole number.
@ line 2 | Remainder 0 when divided by 2 = even
Line two uses the remainder operator from lesson two point six. If the remainder when dividing by two is zero, the number is even.
@ line 3 | Runs if True
Line three runs if the condition is True.
@ line 4 | else: same indentation as if, then a colon
Line four is else, lined up with the if, with a colon.
@ line 5 | Runs if False
Line five runs if the condition is False.
@ line 6 | Runs either way
And line six always runs.
@ predict 4 | The user types 7. Which line runs?
The user types seven. Which of the two blocks will run?
@ run | 7 % 2 = 1, so else runs
Run. Seven is odd. Seven divided by two leaves a remainder of one, so the condition was False, and the else block ran. Then thanks for playing. If you type an even number in your own editor, you'll see the if block run instead. One of the two always runs.

## CODE | quiz.py
```python
print("Quick quiz!")
answer = input("What is 6 x 7? ")
if answer == "42":
    print("Correct! Brilliant maths.")
    points = 10
else:
    print("Not quite. The answer is 42.")
    points = 0
print("Points:", points)
```
@ input 48
@ say
Let's make a quiz question that marks the answer.
@ line 1-2 | Ask a question
Line one prints a title, and line two asks a question.
@ line 3 | Compare the answer as text
Line three compares the answer with the string forty two. We don't convert to int here, because we only need to check the text matches. That also means the program won't crash if someone types a word.
@ line 4-5 | Correct: a message and 10 points
If it's correct, we print a message and set points to ten.
@ line 6-8 | Otherwise: a kind message and 0 points
Otherwise, we print a kind message with the right answer, and set points to zero.
@ line 9 | points always has a value now
Line nine prints the points. Because exactly one block runs, points is always set, whichever path we took.
@ predict 5 | The user types 48. What will happen?
This user types forty eight. What do you think will happen?
@ run | Wrong answer: else runs, 0 points
Run. Not quite, the answer is forty two. Points: zero. The else block caught the wrong answer.

## CODE | two_ifs.py
```python
temp = 30
if temp > 25:
    print("It's hot")
if temp > 15:
    print("It's warm")
```
@ say
Here's an important question: what's the difference between if and else, and two separate ifs? Let's find out.
@ line 1 | A temperature of 30
A temperature of thirty degrees.
@ line 2-3 | First if: hot?
The first if: is it more than twenty five? Then print it's hot.
@ line 4-5 | A SECOND, separate if: warm?
And a second, separate if: is it more than fifteen? Then print it's warm.
@ predict 5 | 30 degrees. One message or two?
Thirty degrees. Will we see one message, or two?
@ run | Two separate ifs: BOTH can run
Run. It's hot, and it's warm. Both conditions were true, so both blocks ran. Two separate ifs are checked separately.
@ edit 4 => else:
Now let's change the second if into an else.
@ edit 5 =>     print("It's not hot")
And change its message.
@ run | if/else: only ONE runs
Run. Only it's hot. With if and else, only one block can ever run. So use if and else when the two choices are opposites, and separate ifs when several things could all be true at once.

## STUDY | Common mistakes
@ table Mistake | What happens ; else score < 50: | SyntaxError: else has no condition ; else without a colon | SyntaxError ; else indented under the if block | SyntaxError: line it up with if ; code between the if block and else | SyntaxError: else must follow straight after
Common else mistakes. Giving else a condition, which isn't allowed, because it means otherwise. Forgetting its colon. Indenting the else instead of lining it up with its if. And putting other code between the if block and the else, which breaks the partnership.

## REVISE | Quick revise
@ point if/else: exactly one block runs
With if and else, exactly one block runs.
@ point else has no condition; it means "otherwise"
Else has no condition. It means otherwise.
@ point Line else up with its if, add a colon, indent its block
Line else up with its if, add a colon, and indent its block.
@ point Opposites: if/else. Independent checks: separate ifs
Use if and else for opposites, and separate ifs for independent checks.

## PRACTICE | Pass or fail
@ task Ask for a test score out of 100.\nIf it is 50 or more, print "Pass" and how many marks above 50.\nOtherwise print "Not this time" and how many marks were needed.
Your turn. Ask for a test score out of one hundred. If it's fifty or more, print pass, and how many marks above fifty it was. Otherwise, print not this time, and how many more marks were needed to reach fifty.
@ hint above = score - 50; needed = 50 - score
Hint: marks above fifty is score minus fifty. Marks needed is fifty minus score.
@ pause 15
Pause the video and try it.

## ANSWER | pass_fail.py
```python
score = int(input("Test score (0-100): "))
if score >= 50:
    print("Pass!", score - 50, "marks above 50")
else:
    print("Not this time.", 50 - score, "more marks needed")
```
@ input 44
@ line 1
Ask for the score, as a number.
@ line 2-3
Fifty or more: pass, and the marks above fifty.
@ line 4-5
Otherwise: not this time, and the marks needed.
@ run
Run with forty four. Not this time, six more marks needed. With a score of fifty, you'd get pass, zero marks above fifty. Great work!

## OUTRO
Excellent! Your programs can now choose between two paths. Next time, we'll handle more than two choices, using elif, so a program can pick from a whole ladder of options. Like, share and subscribe, and keep coding. Happy Learning!
