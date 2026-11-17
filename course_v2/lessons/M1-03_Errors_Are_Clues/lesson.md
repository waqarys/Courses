---
id: "1.3"
title: "Errors Are Clues"
module: 1
module_title: "Getting Started"
next: "Mini-Project: My Welcome Card"
minutes: 8.71
thumb_code: 'NameError: name ...'
goals: ["Why errors happen", "How to read an error message", "NameError, SyntaxError, IndentationError", "Bugs that give no error at all"]
youtube:
  title: "Python Lesson 1.3: Errors Are Clues - Reading Python Error Messages | Introduction to Python"
  description: |
    Every programmer sees errors every day. Ziggy the Python shows you how to read an error message from the
    bottom up, then we make the most common beginner mistakes on purpose and fix them live: NameError,
    SyntaxError and IndentationError. We also hunt a sneaky bug that gives no error at all.
    For beginners aged 7 to 20.
  tags: [python errors, python debugging, syntaxerror, nameerror, python for beginners, learn python, fun skill builders]
---

<!-- Booklet 1.8 smoke testing; capitals matter. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Today we're going to do something that sounds strange. We're going to make mistakes on purpose! Every programmer, even the experts, sees errors every single day. The trick is knowing how to read them, and today you'll learn exactly that.

## STUDY | Errors are normal
@ point Errors are not failures. They are clues.
When Python can't understand your code, it stops and shows an error message, often in red. That can feel scary at first. But an error is not Python being angry with you. It's Python giving you a clue about what went wrong, and usually where.
@ point Python is very fussy about details
Python is like a very strict spelling teacher. A missing bracket, a missing quote mark, or a capital letter in the wrong place, and it stops. A person would guess what you meant. Python never guesses. It needs everything exactly right.
@ point Finding and fixing mistakes is called debugging
Finding and fixing mistakes has a special name: debugging. The story goes that, long ago, engineers found a real moth stuck inside a computer and taped it into their notebook. Today, a bug just means a mistake in code, and debugging means hunting it down.
@ point Even experts spend lots of time debugging
Here's a secret. Professional programmers often spend more time debugging than writing new code. So getting good at reading errors is one of the most useful skills you can have.

## STUDY | How to read an error
@ snippet Traceback (most recent call last):\n  File "hello.py", line 1, in <module>\n    Print("Hello")\nNameError: name 'Print' is not defined
An error message has a few parts. Let's read one like a detective, starting from the bottom.
@ point Last line: the TYPE of error and what it means
The last line is the most important. It tells you the type of error, like NameError or SyntaxError, followed by a short explanation in plain words.
@ point "line 1": WHERE Python got stuck
Above that, Python shows the file name and the line number where it got stuck, and often copies that line for you. Go to that line first. Sometimes the real mistake is just before it, on the line above.
@ point Traceback = the trail Python followed
The word traceback at the top just means: here's the trail I followed before I got stuck. For our short programs, it's only one step long.
@ table Error | Usually means ; NameError | a word Python does not know ; SyntaxError | broken grammar: quote or bracket ; IndentationError | spaces at the start of a line
Here are the three errors beginners meet most. A NameError means Python found a word it doesn't know, often a spelling mistake or a wrong capital letter. A SyntaxError means the grammar of the line is broken, such as a missing quote mark or bracket. And an IndentationError means there are unexpected spaces at the start of a line.

## CODE | bug_hunt.py
```python
Print("Hello, World!")
```
@ say
Let's make our first mistake on purpose. Watch carefully.
@ line 1 | Capital P: is that a problem?
We type print, but with a capital P. It looks almost right, doesn't it?
@ predict 3 | Will it run?
Will Python let this one go? What do you think?
@ run | NameError: Python doesn't know "Print"
Let's run it. Error! Read the last line: NameError, name capital Print is not defined. Python might even suggest the word you probably meant: print with a small p. Python is case sensitive, so capital letters and small letters are completely different to it.
@ edit 1 => print("Hello, World!")
Let's fix it. We change the capital P into a small p.
@ run | Fixed! Always run again to check.
And run again. Hello, World. Fixed! Always run your program again after a fix, to check it really worked.
@ edit 1 => print("Hello, World!)
Now the second classic mistake. We delete the closing quote mark after the exclamation mark.
@ run | SyntaxError: the string never ended
Run it. This time it's a SyntaxError. Python is telling us the string was never closed. It started reading text at the first quote mark and never found the end.
@ edit 1 => print("Hello, World!")
Let's put the quote mark back.
@ run
Run again, and we're fixed once more.
@ edit 2 =>   print("Bye!")
Last one. On a new line, we add two spaces before print. Spaces at the start of a line are called indentation.
@ run | IndentationError: unexpected spaces
Run. IndentationError, unexpected indent. Python uses spaces at the start of a line to group code together, which we'll learn about later. Here they don't belong.
@ edit 2 => print("Bye!")
Remove the spaces.
@ run | Every fix = run again
And run. Both lines work. Three bugs found, three bugs fixed.

## CODE | more_bugs.py
```python
prnt("Ready")
```
@ say
Let's look at a few more bugs that you're very likely to meet.
@ line 1 | A typo in the function name
First, a typo. We've typed p r n t, and forgotten the letter i.
@ run | NameError again: a misspelled name
Run. NameError again. Python doesn't know a word called p r n t. Spelling mistakes are the number one cause of name errors.
@ edit 1 => print(Ready)
Let's fix the spelling, but this time forget the quote marks around the word Ready.
@ predict 4 | No quotes. What will Python think Ready is?
Without quote marks, what do you think Python will do with the word Ready?
@ run | Without quotes, Ready looks like a name
Run. Another NameError! Without quotes, Python thinks Ready is the name of something it should already know about. Text always needs quote marks.
@ edit 1 => print("Ready"
Let's add the quotes, but this time forget the closing bracket.
@ run | SyntaxError: a bracket was never closed
Run. SyntaxError. Python says the opening bracket was never closed. Every opening bracket needs a partner.
@ edit 1 => print("Ready")
Add the bracket.
@ run
And run. Ready! Notice that each error message pointed us in the right direction.

## CODE | sneaky_bug.py
```python
print("10 - 3 =", 10 + 3)
```
@ say
Now the sneakiest bug of all: one that doesn't cause an error.
@ line 1 | Look closely at the maths
This line is supposed to show ten minus three. Look closely before we run it.
@ run | No error... but is it right?
Run. No red message. It says ten minus three equals thirteen. Python is happy. But that answer is wrong! We typed a plus instead of a minus in the maths part.
@ edit 1 => print("10 - 3 =", 10 - 3)
Let's change the plus to a minus.
@ run | Always check the output makes sense
Run. Ten minus three equals seven. Correct. This is called a logic error. The code runs fine, but it does the wrong thing. Python can't catch these for you, which is why you should always read your output and ask: does this make sense?

## STUDY | Your debugging checklist
@ point 1. Stay calm and read the LAST line
Here's a checklist you can use every time something goes wrong. Step one: stay calm and read the last line of the error. It names the problem.
@ point 2. Go to the line number (and the line above)
Step two: go to the line number Python gives you. If that line looks fine, check the line above it, especially for a missing bracket or quote mark.
@ point 3. Check spelling, capitals, quotes and brackets
Step three: check the usual suspects. Spelling, capital letters, quote marks in pairs, and brackets in pairs.
@ point 4. Change ONE thing, then run again
Step four: change one thing, then run again. If you change five things at once and it works, you won't know which change fixed it.
@ point 5. Still stuck? Explain it out loud
And step five: if you're still stuck, explain your code out loud, line by line, to a friend, a pet, or even a toy duck. Programmers really do this. It's called rubber duck debugging, and it works surprisingly often, because explaining forces you to read every detail.

## REVISE | Quick revise
@ point An error is a clue, not a failure
An error is a clue, not a failure.
@ point Read the last line first, then find the line number
Read the last line for the type of error, then go to the line number.
@ point NameError, SyntaxError, IndentationError
NameError means an unknown word. SyntaxError means broken grammar. IndentationError means unexpected spaces.
@ point Logic errors give no message: check your output
Logic errors give no message at all, so always check your output makes sense.
@ point Fix one thing, then run again
And fix one thing at a time, then run again.

## PRACTICE | Bug hunt
@ task This program has 2 bugs. Find and fix them:\nprint("I like pizza")\nPrint("I like cake)
Here's a bug hunt. This little program has two bugs hiding in it. Can you find both and fix them?
@ hint Look closely at capital letters and quote marks.
Hint: check capital letters, and check that every quote mark has a partner.
@ pause 15
Pause the video, type it in, run it, and use the error messages to help you.

## ANSWER | bug_hunt_fixed.py
```python
print("I like pizza")
Print("I like cake)
```
@ line 1-2
Let's type the buggy version and let Python help us.
@ run
Run. Python reports a SyntaxError on line two first, because it checks the grammar of the whole program before it runs anything. The string on line two never ends.
@ edit 2 => Print("I like cake")
Add the missing quote mark.
@ run
Run again. Now line one works, and we get a NameError on line two. Capital Print again!
@ edit 2 => print("I like cake")
Change it to a small p.
@ run
And now both lines work. We fixed one error at a time and ran again each time. That's exactly how real programmers do it.

## OUTRO
Great detective work! Errors are now your friends. Next time, we'll put everything together and build a fun welcome card program with borders and patterns. Like, share and subscribe, and keep coding. Happy Learning!
