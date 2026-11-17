---
id: "4.5"
title: "Complex and Nested Conditions"
module: 4
module_title: "Making Decisions and Loops"
next: "match / case"
minutes: 8.25
thumb_code: 'if age >= 8 and height >= 120:'
goals: ["and, or, not inside if statements", "Brackets and named booleans for clear conditions", "Nested ifs: a decision inside a decision", "Choosing between nesting and and"]
youtube:
  title: "Python Lesson 4.5: Complex Conditions and Nested if Statements | Introduction to Python"
  description: |
    Real rules are rarely one simple question. Ziggy the Python shows how to combine conditions with and, or and
    not, how brackets and well-named booleans keep them readable, and how to put an if inside another if. We code
    theme-park ride rules, a two-step login, and a free-delivery rule, and fix a sneaky "or" bug.
    For beginners aged 7 to 20.
  tags: [python and or not, nested if python, complex conditions python, boolean logic, learn python, fun skill builders]
---

<!-- Booklet chapter 4: selection with compound conditions; truth tables from chapter 2. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Real life rules are rarely just one simple question. You can go to the park if your homework is done and it isn't raining. You get a discount if you're a student or over sixty five. Today we'll write conditions like these, and put decisions inside other decisions.

## STUDY | Combining conditions
@ table Operator | True when... | Example ; and | BOTH sides are True | age >= 8 and height >= 120 ; or | at least ONE side is True | day == "Sat" or day == "Sun" ; not | the condition is False | not is_raining
Remember and, or and not from lesson two point seven? Now we'll use them inside if statements. And is True only when both sides are True. Or is True when at least one side is True. And not flips True to False, and False to True.
@ point and = every rule must pass
Use and when every rule must pass, like a ride that needs you to be both old enough and tall enough.
@ point or = any one rule is enough
Use or when any one rule is enough, like a weekend that can be Saturday or Sunday.
@ point Each side must be a FULL comparison
One important detail: each side of and or or must be a complete comparison. Day equals Saturday or day equals Sunday, not day equals Saturday or Sunday. We'll see what goes wrong with the short version in a moment.

## STUDY | Keeping conditions readable
@ snippet if (age >= 8 or with_adult) and height >= 120:
When you mix and with or, use brackets to show which parts belong together, just like in maths. Python checks not first, then and, then or. But brackets make your meaning obvious to anyone reading the code.
@ snippet old_enough = age >= 8 or with_adult\ntall_enough = height >= 120\nif old_enough and tall_enough:
Even better: give each part a name. Store each piece of the rule in a well named boolean variable, then the if reads like a sentence. If old enough and tall enough.
@ point Readable conditions = fewer bugs
Readable conditions lead to fewer bugs, because you can check each part on its own.

## CODE | ride_rules.py
```python
age = int(input("Age: "))
height = int(input("Height in cm: "))
with_adult = input("With an adult? (y/n) ") == "y"
old_enough = age >= 8 or with_adult
tall_enough = height >= 120
if old_enough and tall_enough:
    print("Enjoy the ride!")
else:
    print("Sorry, not this time.")
```
@ input 7 | 130 | y
@ line 1-2 | Two numbers
Lines one and two ask for the rider's age and height, as numbers.
@ line 3 | A comparison stores True or False
Line three is clever. It asks a yes or no question, and compares the answer with the letter y. The result of that comparison, True or False, is stored straight into with adult.
@ line 4 | Rule 1: 8 or older, OR with an adult
Line four is the first rule: at least eight, or with an adult.
@ line 5 | Rule 2: at least 120 cm
Line five is the second rule: at least one hundred and twenty centimetres.
@ line 6-9 | Both rules must pass
And the if needs both rules to pass.
@ predict 6 | Age 7, 130 cm, with an adult. Can they ride?
Our rider is seven years old, one hundred and thirty centimetres tall, and is with an adult. Can they ride?
@ run | Yes: with an adult makes rule 1 True
Run. Enjoy the ride! Age seven fails the age check, but with adult is True, and or only needs one. They're also tall enough, so and is satisfied. Splitting the rule into named parts made it easy to reason about.

## CODE | weekend_bug.py
```python
day = "Monday"
if day == "Saturday" or "Sunday":
    print("It's the weekend!")
else:
    print("School day.")
```
@ say
Now here's a sneaky bug that almost every beginner writes. Watch closely.
@ line 1 | It's Monday
The day is Monday.
@ line 2 | Looks right... but is it?
Line two looks like English: if day equals Saturday or Sunday.
@ line 3-5
Then the two messages.
@ predict 5 | Monday. Weekend or school day?
It's Monday, so we should see school day. Will we?
@ run | Bug: Monday is "the weekend"!
Run. It's the weekend! On a Monday! What happened? Python read it as two separate parts: day equals Saturday, which is False, or the string Sunday on its own. And a non empty string counts as True in a condition. So the whole thing is always True.
@ edit 2 => if day == "Saturday" or day == "Sunday":
The fix: make both sides full comparisons.
@ run | Fixed: both sides compare day
Run. School day. Correct. Another neat fix is to use in with a list: if day in Saturday, Sunday. That's short, clear and impossible to get wrong in this way.

## STUDY | Nested ifs
@ point A nested if = an if INSIDE another if's block
Sometimes a second question only makes sense if the first answer was yes. You only ask for a password if the username is correct. To do that, we put an if inside the block of another if. That's called a nested if.
@ snippet if username == "ziggy":\n    if password == "hiss123":\n        print("Welcome!")
The inner if is indented once more. Each level of indentation is another layer of decision.
@ point Each level is indented four more spaces
Each level is indented four more spaces. Keep it to two or three levels at most, or the code becomes hard to follow.
@ point Nesting lets you give different messages at each step
Nesting is useful when you want different messages at each step, like: username not found, versus: wrong password.

## CODE | login.py
```python
USERNAME = "ziggy"
PASSWORD = "hiss123"
name = input("Username: ")
if name == USERNAME:
    secret = input("Password: ")
    if secret == PASSWORD:
        print("Welcome back, Ziggy!")
    else:
        print("Wrong password.")
else:
    print("Username not found.")
```
@ input ziggy | hiss12
@ line 1-2 | The correct details, as constants
The correct username and password, stored as constants. In a real app, passwords are stored much more safely, but this shows the idea.
@ line 3 | Ask for the username
Line three asks for the username.
@ line 4 | Outer if: is the username right?
The outer if checks the username.
@ line 5 | Only then ask for the password
Only if it's right do we ask for the password. This line is inside the outer block.
@ line 6-9 | Inner if/else: indented again
Then an inner if and else, indented one more level, checks the password.
@ line 10-11 | The outer else
And the outer else, lined up with the outer if, handles a wrong username.
@ predict 6 | Right username, but "hiss12". Which message?
The user types the correct username, but the password hiss twelve, missing the three. Which message will they see?
@ run | Outer True, inner False → "Wrong password."
Run. The username matched, so we were asked for the password. The password didn't match, so the inner else ran: wrong password. Follow the indentation to see which else belongs to which if.

## CODE | delivery.py
```python
total = 32
is_member = False
if total >= 50 or is_member:
    print("Free delivery!")
elif total >= 30 and not is_member:
    print("Delivery costs 2 coins.")
else:
    print("Delivery costs 5 coins.")
```
@ say
Let's finish with and, or and not together in a ladder: an online shop's delivery rules. Free delivery if you spend fifty or more, or if you're a member. Otherwise, two coins if you spend at least thirty, and five coins below that.
@ line 1-2 | A 32-coin order, not a member
The order total is thirty two, and the customer isn't a member.
@ line 3-4 | Rule 1: big order OR member
The first rule uses or.
@ line 5-6 | Rule 2: 30 or more AND not a member
The second rule uses and with not.
@ line 7-8 | Everything else
And else for everything else.
@ predict 6 | 32 coins, not a member. Which message?
Thirty two coins, and not a member. Which message will appear?
@ run | Rule 1 False, rule 2 True: 2 coins
Run. Delivery costs two coins. The first rule was False, because thirty two is less than fifty and they're not a member. The second rule was True. Strictly speaking, the not is member part isn't needed, because members already got free delivery on the first rung. But writing it makes the rule crystal clear to a reader. Clear beats clever.

## STUDY | Common mistakes
@ table Mistake | What happens ; if day == "Sat" or "Sun": | always True: repeat day == ; if 10 < age > 15 | confusing: write two clear comparisons ; mixing and/or without brackets | the order of checks may surprise you ; else lined up with the wrong if | it belongs to a different decision
The mistakes to watch out for. Leaving out the second comparison with or, which makes the condition always True. Writing confusing chains. Mixing and with or without brackets. And lining up an else with the wrong if in nested code.

## REVISE | Quick revise
@ point and: all must pass. or: one is enough. not: flip
And needs all parts to pass, or needs just one, and not flips the result.
@ point Each side must be a full comparison
Each side of and or or must be a full comparison.
@ point Use brackets and named booleans for clarity
Use brackets and named booleans to keep conditions clear.
@ point A nested if is an if inside another if's block
A nested if is an if inside another if's block, indented one more level.

## PRACTICE | Club entry
@ task A coding club is open to ages 9 to 16 who have a club card, OR anyone with a teacher's note.\nAsk for age, card (y/n) and note (y/n). Print "Welcome!" or "Sorry".
Your turn. A coding club is open to anyone aged nine to sixteen who has a club card, or to anyone at all who has a note from a teacher. Ask for the age, whether they have a card, and whether they have a note. Print welcome or sorry.
@ hint right_age = 9 <= age <= 16; has_card = input(...) == "y"
Hint: make three named booleans: right age, has card and has note. Then combine them with brackets.
@ pause 15
Pause the video and give it a go.

## ANSWER | club_entry.py
```python
age = int(input("Age: "))
has_card = input("Club card? (y/n) ") == "y"
has_note = input("Teacher's note? (y/n) ") == "y"
right_age = 9 <= age <= 16
if (right_age and has_card) or has_note:
    print("Welcome!")
else:
    print("Sorry")
```
@ input 17 | y | y
@ line 1-3
Three questions, two of them turned straight into booleans.
@ line 4
A named boolean for the age range, using a chained comparison.
@ line 5-8
Then the rule, with brackets around the first part.
@ run
Run with age seventeen, a card, and a note. Welcome! Seventeen is too old for the card rule, but the teacher's note gets them in. Great logic!

## OUTRO
Superb! You can now write complicated rules clearly, and nest decisions inside each other. Next time, we'll learn match and case, a tidy way to choose between lots of exact options. Like, share and subscribe, and keep coding. Happy Learning!
