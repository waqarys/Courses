---
id: "1.2"
title: "Hello, World!"
module: 1
module_title: "Getting Started"
next: "Errors Are Clues"
minutes: 9.04
thumb_code: 'print("Hello, World!")'
goals: ["What a program is made of", "How print shows text", "Strings and comments", "Python reads top to bottom"]
youtube:
  title: "Python Lesson 1.2: Hello, World! Your First Program | Introduction to Python"
  description: |
    Write the most famous program in the world with Ziggy the Python. We look closely at print, brackets, quote
    marks and strings, add comments, discover that Python runs lines from top to bottom, print blank lines and
    patterns, and smoke test our code. Then you write a three-line "about me" program.
    For beginners aged 7 to 20.
  tags: [hello world python, python print, first python program, python for kids, learn python, fun skill builders]
---

<!-- Booklet chapter 1: Hello World, smoke testing. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python, and today is a big day. We're writing Hello, World! It's the first program that millions of programmers have written, in almost every language on Earth. Today, it's your turn to join them.

## STUDY | Why "Hello, World!"?
@ point A tradition since the 1970s
Why Hello, World? Back in the nineteen seventies, a famous programming book used a tiny program that printed the words hello, world. Ever since, it's been the traditional first program.
@ point It proves everything works
It's not just a tradition. It's a test. If Hello, World appears, you know your editor works, Python is installed, and you can run code. Everything else is built on top of that.
@ point Small steps, then build up
Programmers always start small, check that it works, and then add more. We'll do exactly the same thing in this course.

## STUDY | Meet print
@ snippet print("Hello, World!")
Here's the whole program. One line. Let's look at every part of it.
@ point print means: show this on the screen
The word print is a function. A function is a command with a name that does a job. print's job is to show something in the output.
@ point Round brackets hold what you want to show
After print come round brackets. Whatever is inside the brackets is what gets shown. Programmers say we pass it to print.
@ point "Quote marks" make text a string
Inside the brackets, the words are wrapped in quote marks. Text inside quote marks is called a string, because it's a string of letters, one after another, like beads on a string.
@ point 'Single' or "double" quotes both work
You can use double quotes or single quotes. Both make a string. Just use the same kind at the start and the end.

## STUDY | Notes and order
@ point # starts a comment: a note for humans
Programs can also contain notes for humans. A note starts with a hash symbol. It's called a comment, and Python skips it completely.
@ point Python reads from top to bottom
Python reads your program from the top line to the bottom line, one at a time. The order you write the lines is the order they happen.
@ point Each print starts a new line in the output
And every print starts on a new line in the output, so three prints give you three lines.

## CODE | hello.py
```python
# My first program
print("Hello, World!")
print("I am learning Python.")
print('Single quotes work too!')
```
@ say
Let's build it in the editor, one line at a time.
@ line 1 | A comment: Python skips it
Line one starts with a hash, so it's a comment. It tells anyone reading the file what this program is. Comments show in grey.
@ line 2 | The famous line
Line two: print, round brackets, quote marks, and the words Hello, World! with a capital H, a comma and an exclamation mark.
@ predict 3 | What will we see? Will the comment show?
Before we run it, a question. Will the comment show up in the output? Think about it.
@ run | Only the print appears
Run. Hello, World! appears. And the comment? Not there. Python skipped it, because comments are only for humans.
@ line 3 | Each print starts a new line
Line three is another print with a different sentence.
@ line 4 | Single quotes make a string too
And line four uses single quotes instead of double quotes.
@ run | Three prints, three lines, in order
Run it again. Three lines, in exactly the order we wrote them. And the single quotes worked just as well as the double ones. The quote marks themselves never appear in the output. They only mark where the string starts and ends.

## CODE | order_matters.py
```python
print("3...")
print("2...")
print("1...")
print("Lift off!")
print()
print("*****")
print("* Hi *")
print("*****")
```
@ say
Let's prove that order really matters, with a rocket launch.
@ line 1-3 | A countdown, top to bottom
Three lines for the countdown: three, two, one.
@ line 4
Then lift off!
@ run | Runs in the order we wrote it
Run. Three, two, one, lift off. Perfect. If we had written lift off first, the rocket would leave before the countdown. Computers don't fix our order for us.
@ line 5 | print() with nothing inside = a blank line
Line five is print with empty brackets. What does that do?
@ predict 3 | An error? Or something else?
Will that be an error, or will something happen? Guess before I run it.
@ line 6-8 | Strings can draw pictures
Now three more lines that draw a little box out of stars. Strings can contain any symbols you like.
@ run | A blank line, then a picture made of text
Run it. After lift off there's an empty line. That's what an empty print does: it prints nothing, then moves to a new line. It's great for spacing out your output. And then our box. Lots of early computer games drew all their pictures like this, using only letters and symbols.

## CODE | quotes_and_commas.py
```python
print("It's my first program!")
print('Ziggy said "Hello!"')
print("I am", 11, "years old.")
print("Next year I will be", 11 + 1)
```
@ say
Here's a puzzle that catches lots of beginners. What if the text itself contains a quote mark, like the word it's?
@ line 1 | An apostrophe inside double quotes is fine
Line one prints: it's my first program. The word it's has an apostrophe, which is the same key as a single quote. So we wrap the whole string in double quotes. Python only ends the string when it sees another double quote.
@ line 2 | Double quotes inside single quotes
Line two does the opposite. The string contains double quote marks, because Ziggy is speaking. So we wrap the whole thing in single quotes.
@ predict 4 | Will the inner quote marks appear?
What do you think? Will the inner quote marks show up in the output this time?
@ run | The inner quotes are part of the text
Run. Yes! It's my first program, with the apostrophe. And Ziggy said hello, with the speech marks. The outside quotes mark the start and the end. The inside ones are just part of the text.
@ line 3 | Commas join several things, with spaces
Line three shows another trick. You can give print several things, separated by commas: some text, a number, and more text. print puts a space between each one.
@ line 4 | Text plus a calculation
Line four mixes text with a calculation: eleven plus one, with no quotes, so Python works it out.
@ run | print adds the spaces for you
Run it. I am eleven years old. Next year I will be twelve. Notice we didn't type any spaces next to the commas, and print still added one between each item. It's a neat way to put text and numbers together.

## CODE | level_up.py
```python
print("Ziggy", "the", "Python")
print("Ziggy", "the", "Python", sep="-")
print("Loading", end="")
print("...", end="")
print("done!")
```
@ say
Here's a level up for anyone who wants more. print has a couple of hidden settings that change how it behaves.
@ line 1 | Commas: print puts a space between items
Line one gives print three strings, separated by commas. We know print will put a space between them.
@ line 2 | sep= changes the separator
Line two is the same, but at the end we add sep equals, and a dash in quotes. S E P is short for separator: the thing print puts between the items.
@ predict 4 | What will sep="-" do?
What do you think the second line will look like?
@ run | Spaces, then dashes
Run. Ziggy the Python with spaces. Then Ziggy dash the dash Python. We swapped the spaces for dashes.
@ line 3 | end="" means: don't start a new line
Now line three. print Loading, with end equals an empty string. Normally, print finishes by moving to a new line. end lets us change that. An empty string means: stay on the same line.
@ line 4-5 | Keep adding to the same line
Line four adds three dots, also staying on the line. And line five prints done, normally.
@ run | Three prints, one line
Run. Loading, dot dot dot, done, all on one line, even though it came from three prints. You don't need these settings yet, but they're handy for neat output later on.

## STUDY | Smoke testing
@ point Smoke test = run it often, check it quickly
The booklet talks about something called a smoke test. When engineers built a new machine, they switched it on and checked that no smoke came out. For us, a smoke test means: run the program after every small change, and check the output looks right.
@ point Write a little, run, check, repeat
That's why we keep pressing Run. Write a line or two, run, check, repeat. If something breaks, you know it was the line you just wrote.
@ table Common mistake | Fix ; Print("Hi") | print must be all lower case ; print("Hi) | close the quote: "Hi" ; print "Hi" | add the round brackets ; print('Hi") | use matching quote marks
Here are the most common slips with print. A capital P. A missing closing quote. Forgetting the brackets. And mixing a single quote with a double quote. Each one gives an error, and each one is easy to fix once you know what to look for.

## REVISE | Quick revise
@ point print("...") shows text in the output
print shows text in the output.
@ point Text in quotes is called a string
Text inside quote marks is called a string.
@ point # comments are notes that Python skips
Comments start with a hash. They're notes for humans, and Python skips them.
@ point Python runs top to bottom; print() alone = blank line
Python runs from top to bottom, and an empty print makes a blank line.

## PRACTICE | Your turn
@ task Write an "about me" program:\n1. A comment with your name\n2. Three prints: your name, your age, your favourite food\n3. Bonus: a blank line and a row of stars at the end
Your turn. Write an about me program. Start with a comment. Then three prints: your name, your age, and your favourite food. For a bonus, add a blank line and a row of stars at the end.
@ hint One print per line. Every string needs a quote mark at both ends.
Hint: one print per line, and remember the quote marks on both sides of each string.
@ pause 15
Pause the video and give it a try.

## ANSWER | about_me.py
```python
# About me, by Asha
print("My name is Asha.")
print("I am 11 years old.")
print("I love mango ice cream.")
print()
print("**********")
```
@ line 1
Here's one way. A comment at the top.
@ line 2-4
Three print lines, each with a full sentence in quote marks.
@ line 5-6
And the bonus: an empty print for a blank line, then a row of stars.
@ run
Run it. My name is Asha. I am eleven years old. I love mango ice cream. A blank line, and the stars. Your sentences will be different, and that's the whole point. It's your program!

## OUTRO
Amazing! You've written Hello, World! and joined millions of programmers around the world. Next time, we'll make some mistakes on purpose, and learn how to read Python's error messages like a detective. Like, share and subscribe, and keep coding. Happy Learning!
