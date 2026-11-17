---
id: "2.2"
title: "Good Names and Constants"
module: 2
module_title: "Variables, Input and Output"
next: "Strings: Playing with Text"
minutes: 8.37
thumb_code: 'player_score = 0'
goals: ["The rules for variable names", "snake_case and other naming styles", "Choosing meaningful names", "Constants in CAPITALS"]
youtube:
  title: "Python Lesson 2.2: Naming Variables - Rules, snake_case and Constants | Introduction to Python"
  description: |
    Good names make code easy to read. Ziggy the Python covers the rules Python enforces for variable names, the
    styles programmers use (snake_case, camelCase, Hungarian notation), how to choose meaningful names, and
    constants written in capitals. We break the rules on purpose to see the errors, then fix them.
    For beginners aged 7 to 20.
  tags: [python variable names, snake case, python constants, pep 8, python for beginners, learn python, fun skill builders]
---

<!-- Booklet chapter 2: naming conventions (snake case, camel case, Hungarian notation). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Last time, we made variables. Today, we'll learn how to name them. Some names break Python's rules and cause errors. Other names are allowed, but make your code confusing. By the end of this lesson, you'll be choosing names like a professional.

## STUDY | The rules Python enforces
@ point Letters, numbers and underscores only
Python has a few strict rules for names. A name can only contain letters, numbers and the underscore character, which is the low line you get by holding shift and pressing the minus key.
@ point Can't START with a number
A name can't start with a number. Player two is fine, but two player is not allowed.
@ point No spaces, no hyphens
No spaces and no hyphens. A space would split the name into two words, and Python reads a hyphen as a minus sign. So player dash score looks like player minus score.
@ point Capitals matter: Score and score are different
Names are case sensitive. Score with a capital S and score with a small s are two completely different boxes.
@ point Can't use Python's own keywords
And you can't use Python's special keywords as names, words like if, for, while, class and True. Python has already given those words a job.

## STUDY | Python's keywords
@ table Some Python keywords | Their job ; if, elif, else | making decisions ; for, while, break | loops ; def, return | making functions ; True, False, None | special values ; import | using extra tools
Here are some of Python's keywords. You'll learn what all of these do during this course. For now, just remember that you can't use them as variable names. There are about thirty five of them in total. The good news is that most editors colour keywords differently, so if a variable name suddenly changes colour as you type it, that's a clue that you've accidentally used a keyword.

## STUDY | Naming styles
@ table Style | Example | Where you see it ; snake_case | player_score | Python variables ; camelCase | playerScore | JavaScript, Java ; PascalCase | PlayerScore | class names ; Hungarian | strName, intAge | older code
When a name has more than one word, we need a way to join the words. Python programmers use snake case: all small letters, with underscores between the words. It's called snake case because it's long and low to the ground, like me. Other languages often use camel case, where each new word starts with a capital, like the humps on a camel. And some older code uses Hungarian notation, where the name starts with a hint about its type, like s t r for a string.
@ point Python's style guide (PEP 8) says: snake_case
Python has an official style guide called PEP eight. It says: use snake case for variable names. So that's what we'll use in this course.
@ point Pick one style and stick to it
The most important thing is to be consistent. Mixing styles in one program makes it harder to read.

## STUDY | Meaningful names
@ table Unclear name | Better name ; x | age ; n | number_of_pets ; thing | favourite_colour ; s | high_score
Python doesn't care whether you call a variable x or high score. But people do! Code is read many more times than it's written, often by you, weeks later. A good name tells you what's inside the box without needing a comment.
@ point Long enough to be clear, short enough to type
A good name is long enough to be clear, and short enough to type easily. Number of pets is great. The number of pets that I currently have at home is too long.

## CODE | names.py
```python
player-score = 5
print(player-score)
```
@ say
Let's break some rules on purpose and read the errors.
@ line 1 | A hyphen in the name
Line one tries to make a variable called player dash score, with a hyphen.
@ line 2
And line two prints it.
@ predict 4 | Allowed or not?
Will Python accept this name? Think about how Python reads a hyphen.
@ run | SyntaxError: Python sees "player minus score"
Run. SyntaxError. Python read the hyphen as a minus sign. So it thought we were trying to store five into player minus score, which makes no sense.
@ edit 1 => player_score = 5
Let's fix line one by changing the hyphen to an underscore.
@ edit 2 => print(player_score)
And fix line two the same way.
@ run | Underscore: perfectly legal
Run. Five. Underscores are perfectly legal.
@ edit 3 => 2nd_place = "Leo"
Now let's add a line that starts with a number: two n d place.
@ run | SyntaxError: names can't start with a digit
Run. Another SyntaxError. Names can't start with a digit. Python thinks it's reading a number, and then gets confused by the letters.
@ edit 3 => second_place = "Leo"
Let's write the number as a word instead: second place.
@ edit 4 => print(Second_place)
And print it, but with a capital S.
@ run | NameError: capitals matter
Run. NameError! There's no box called Second place with a capital S. We made second place with a small s. Capitals matter.
@ edit 4 => print(second_place)
Fix the capital letter.
@ run | Every name follows the rules now
And run. Five, and Leo. Every name follows the rules now.

## CODE | mystery.py
```python
a = 4
b = 3
c = a * b
print(c)
```
@ say
Let's see why meaningful names matter. Here's a tiny program with terrible names.
@ line 1-3 | What do a, b and c mean?
A equals four. B equals three. C equals a times b.
@ predict 4 | What is this program FOR?
Python can run this easily. But can you tell what it's for? Is it about money? Pizza? Pets? Have a think.
@ run | It works, but what does 12 mean?
Run. Twelve. It works, but we have no idea what twelve means.
@ edit 1 => boxes = 4
Let's rename the variables. A becomes boxes.
@ edit 2 => cakes_per_box = 3
B becomes cakes per box.
@ edit 3 => total_cakes = boxes * cakes_per_box
C becomes total cakes, made from boxes times cakes per box.
@ edit 4 => print("Total cakes:", total_cakes)
And we print it with a label.
@ run | Same maths, but now it explains itself
Run. Total cakes, twelve. Exactly the same maths, exactly the same answer, but now anyone can understand the program at a glance. That's the power of a good name.

## STUDY | Constants
@ snippet SECONDS_PER_MINUTE = 60\nMAX_LIVES = 3
Sometimes a value should never change while the program runs. The number of seconds in a minute is always sixty. We call a value like that a constant.
@ point CONSTANTS are written in CAPITALS
In Python, we show that something is a constant by writing its name in capital letters, with underscores between the words.
@ point It's a promise: "please don't change this"
Python doesn't actually stop you from changing a constant. The capitals are a promise to anyone reading the code: this value is meant to stay the same.
@ point Constants avoid "magic numbers"
Constants also avoid what programmers call magic numbers. If you see the number sixty in a program, it could mean anything. If you see seconds per minute, you know exactly what it is.

## CODE | constants.py
```python
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
hours_of_sleep = 9
minutes = hours_of_sleep * MINUTES_PER_HOUR
seconds = minutes * SECONDS_PER_MINUTE
print("Hours of sleep:", hours_of_sleep)
print("Minutes:", minutes)
print("Seconds:", seconds)
```
@ line 1-2 | Constants in capitals at the top
Let's use constants in a real calculation. We put the constants at the top of the program, in capitals: sixty seconds per minute, and sixty minutes per hour.
@ line 3 | A normal variable in snake_case
Line three is a normal variable in snake case: nine hours of sleep.
@ line 4 | The names explain the maths
Line four works out the minutes: hours of sleep times minutes per hour. You can read the maths like a sentence.
@ line 5
Line five turns the minutes into seconds.
@ predict 5 | How many seconds are in 9 hours?
Any guesses? How many seconds of sleep is nine hours?
@ line 6-8 | Print the results with labels
Lines six to eight print the results with labels.
@ run | 540 minutes, 32,400 seconds
Run. Nine hours. Five hundred and forty minutes. And thirty two thousand four hundred seconds. That's a lot of seconds! And because every name is meaningful, anyone could read this code and understand it straight away.

## REVISE | Quick revise
@ point Letters, digits, _ only; never start with a digit
Names use letters, digits and underscores, and never start with a digit.
@ point No spaces or hyphens; capitals matter; no keywords
No spaces or hyphens, capitals matter, and keywords are not allowed.
@ point Python uses snake_case for variables
Python uses snake case for variable names.
@ point CONSTANTS in capitals; choose meaningful names
Constants are written in capitals, and every name should be meaningful.

## PRACTICE | Fix the names
@ task Fix these names so the program runs and reads well:\nmy score = 10\n1st_level = "Forest"\nX = 3   # lives\nprint(my score, 1st_level, X)
Your turn. This little program has three badly named variables. Two of them break Python's rules, and one is legal but unclear. Rename all three so the program runs and is easy to read.
@ hint Use snake_case, write numbers as words, and say what X is for.
Hint: use snake case, write the number as a word, and give X a name that says what it stores.
@ pause 15
Pause the video and fix them.

## ANSWER | fixed_names.py
```python
my_score = 10
first_level = "Forest"
lives = 3
print(my_score, first_level, lives)
```
@ line 1 | A space becomes an underscore
My space score becomes my underscore score.
@ line 2 | No digit at the start
One s t level becomes first level.
@ line 3 | A clear name means no comment is needed
And X becomes lives. Now we don't even need the comment.
@ line 4
Print all three.
@ run
Run. Ten, Forest, three. Your names might be a little different, and that's fine, as long as they follow the rules and say what's in the box.

## OUTRO
Well done! Your variable names are now legal and easy to read. Next time, we'll have fun with strings: joining text, counting letters, and shouting in capitals. Like, share and subscribe, and keep coding. Happy Learning!
