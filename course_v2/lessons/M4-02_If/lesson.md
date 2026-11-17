---
id: "4.2"
title: "if: Making a Choice"
module: 4
module_title: "Making Decisions and Loops"
next: "if / else"
minutes: 7.55
thumb_code: 'if height >= 120:'
goals: ["Selection: choosing what runs", "if condition: then an indented block", "The colon and indentation", "Conditions with input and variables"]
youtube:
  title: "Python Lesson 4.2: The if Statement - Making Decisions in Python | Introduction to Python"
  description: |
    Programs that make decisions! Ziggy the Python explains selection with a fork in the road, how an if statement
    runs its indented block only when the condition is True, why the colon and indentation matter, and how to
    use if with input. We build a ticket checker and a bonus-points game step by step and fix the classic errors.
    For beginners aged 7 to 20.
  tags: [python if statement, python conditions, selection in programming, python indentation, learn python, fun skill builders]
---

<!-- Booklet chapter 4: selection (if). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Until now, our programs have done the same thing every time they run. Today, that changes. With the if statement, a program can look at a situation and decide what to do. This is where programs start to feel smart.

## STUDY | A fork in the road
@ point Selection: the program chooses which steps to run
Remember the decision diamond in a flowchart? It asks a yes or no question, and the program goes one way or the other. In programming, this is called selection, because the program selects which steps to run.
@ point "IF it's raining, take an umbrella"
We make decisions like this all the time. If it's raining, take an umbrella. If you're hungry, have a snack. If the light is red, stop. Each one has a condition, the part that's true or false, and an action that only happens when the condition is true.
@ point The condition is a True/False question
The condition is a question with a True or False answer. That's exactly what we learned in lesson two point seven, with comparisons like greater than and double equals.
@ flow Is it raining? > Yes: take an umbrella > Then: go outside
Picture it as a flowchart. Is it raining? If yes, take an umbrella. Either way, we then go outside. The umbrella step only happens sometimes. Going outside always happens.

## STUDY | Writing an if statement
@ snippet if height >= 120:\n    print("You can ride!")
Here's an if statement in Python. The word if, then the condition, then a colon. On the next line, indented by four spaces, the code that runs only when the condition is True.
@ point if CONDITION :  ← never forget the colon
The colon at the end is essential. It means: here comes the block of code that belongs to this if.
@ point The indented block runs only when the condition is True
The indented lines are called the block, or body. If the condition is True, Python runs the block. If it's False, Python skips the whole block and carries on after it.
@ point Indentation decides what's inside the if
Just like with for loops, indentation decides what's inside the if. Four spaces is the standard. Most editors add them automatically when you press Enter after a colon.
@ point The first unindented line runs either way
And the first line after the block that isn't indented always runs, whatever the answer was.

## CODE | ride.py
```python
height = 125
if height >= 120:
    print("You can ride the roller coaster!")
    print("Hold on tight!")
print("Thanks for visiting the park.")
```
@ line 1 | The rider's height
Line one stores a height of one hundred and twenty five centimetres.
@ line 2 | The condition, then a colon
Line two is the if statement. Is height greater than or equal to one hundred and twenty? Then a colon.
@ line 3-4 | Indented: only runs if True
Lines three and four are indented, so they belong to the if. They only run when the condition is true.
@ line 5 | Not indented: always runs
Line five isn't indented, so it always runs.
@ predict 4 | 125 cm. What will be printed?
With a height of one hundred and twenty five, what will we see?
@ run | True: the block runs
Run. One hundred and twenty five is at least one hundred and twenty, so the condition is True. Both lines of the block run, and then the thank you message.
@ edit 1 => height = 110
Now let's change the height to one hundred and ten.
@ predict 4 | 110 cm. What now?
What will happen this time?
@ run | False: the block is skipped
Run. Only the thank you message. The condition was False, so Python skipped the whole indented block. Same program, different data, different result. That's selection.
@ edit 1 => height = 120
One more test: exactly one hundred and twenty.
@ run | Exactly 120: >= includes the boundary
Run. You can ride! Greater than or equal to includes one hundred and twenty itself. Testing the exact boundary value like this is really important, because that's where bugs love to hide. If we'd used just greater than, a rider of exactly one hundred and twenty would be turned away.

## CODE | bonus.py
```python
score = int(input("Your score: "))
if score >= 100:
    print("Bonus level unlocked!")
    score = score + 50
if score == 0:
    print("Keep practising!")
print("Final score:", score)
```
@ input 120
@ say
Now let's use input, so the user decides what happens.
@ line 1 | Ask for a score, as a number
Line one asks for a score, and converts it to a number with int. Remember, we can only compare numbers properly once they're numbers.
@ line 2 | First decision
Line two is our first decision: is the score at least one hundred?
@ line 3-4 | Two lines in the block
If so, two things happen: a message, and fifty bonus points.
@ line 5-6 | A second, separate decision
Lines five and six are a second, separate if: is the score exactly zero? Two equals signs, because we're comparing.
@ line 7 | Always runs
And line seven always prints the final score.
@ predict 5 | Score 120: which messages appear? What's the final score?
I'll type one hundred and twenty. Which messages will appear, and what will the final score be?
@ run | Bonus: 120 + 50 = 170
Run. Bonus level unlocked! And the final score is one hundred and seventy. The second if was checked too, but one hundred and seventy isn't zero, so it was skipped. Each if is checked on its own, one after the other.

## CODE | password_check.py
```python
password = input("Choose a password: ")
if len(password) < 8:
    print("Too short! Use at least 8 characters.")
if password.lower() == "password":
    print("That's far too easy to guess!")
if " " in password:
    print("Please don't use spaces.")
print("Checked:", len(password), "characters")
```
@ input password
@ say
Conditions can use anything that gives True or False: len, string methods and in. Let's write a password checker.
@ line 1 | Ask for a password
Line one asks the user to choose a password.
@ line 2-3 | Check the length
The first check: is it shorter than eight characters?
@ line 4-5 | Check for the most guessable password of all
The second check uses dot lower, so that capitals don't matter. Is it the word password? Sadly, that's one of the most common passwords in the world.
@ line 6-7 | Check for spaces with in
The third check uses in, to see if there's a space anywhere in it.
@ line 8 | Always runs
And the last line always runs.
@ predict 6 | The user types: password. Which warnings appear?
The user types the word password, all in small letters. It has eight characters. Which warnings will appear?
@ run | One warning: too easy to guess
Run. Only one warning: that's far too easy to guess. It's exactly eight characters, so it isn't too short, and it has no spaces. Three separate checks, and each one only speaks up when its condition is True.

## STUDY | Common mistakes
@ table Mistake | What happens ; if score > 100 (no colon) | SyntaxError: expected ':' ; block not indented | IndentationError: expected an indented block ; if score = 100: | SyntaxError: use == to compare ; if age > "10": | TypeError: compare numbers with numbers
Here are the mistakes everyone makes with if. Forgetting the colon. Forgetting to indent the block. Using one equals sign instead of two. And comparing a number with text, which usually happens when you forget to convert an input with int.

## REVISE | Quick revise
@ point Selection lets a program choose what to run
Selection lets a program choose what to run.
@ point if condition: then an indented block
Write if, a condition and a colon, then an indented block.
@ point True: the block runs. False: it's skipped
When the condition is True, the block runs. When it's False, it's skipped.
@ point Test the boundary: >= vs >
And always test the boundary value, like exactly one hundred and twenty.

## PRACTICE | Ride check
@ task Ask the user for their height in cm.\nIf it is 120 or more, print "Ride allowed".\nAlways print "Have a great day!" at the end.\nTest with 150, 119 and 120.
Your turn. Ask the user for their height in centimetres. If it's one hundred and twenty or more, print ride allowed. Whatever happens, print have a great day at the end. Then test it with one hundred and fifty, one hundred and nineteen, and exactly one hundred and twenty.
@ hint height = int(input(...)); if height >= 120:
Hint: convert the input with int, and use greater than or equal to.
@ pause 15
Pause the video and give it a go.

## ANSWER | ride_check.py
```python
height = int(input("Your height in cm: "))
if height >= 120:
    print("Ride allowed")
print("Have a great day!")
```
@ input 119
@ line 1
Ask for the height, as a number.
@ line 2-3
If it's at least one hundred and twenty, ride allowed.
@ line 4
And the goodbye message, not indented.
@ run
Let's test the trickiest one: one hundred and nineteen. Just the goodbye message, because one hundred and nineteen is less than one hundred and twenty. Try one hundred and twenty and one hundred and fifty in your own editor, and you should see ride allowed for both.

## OUTRO
Amazing! Your programs can now make decisions. Next time, we'll give them two paths with if and else, so that something always happens, whether the answer is yes or no. Like, share and subscribe, and keep coding. Happy Learning!
