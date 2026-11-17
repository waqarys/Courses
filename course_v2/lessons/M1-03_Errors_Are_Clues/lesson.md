---
id: "1.3"
title: "Errors Are Clues"
module: 1
module_title: "Getting Started"
next: "My Welcome Card"
minutes: 5.3   # rendered video length
thumb_code: 'Print("Oops")  # NameError'
goals: ["Why errors are normal", "How to read an error message", "NameError and SyntaxError", "Fix, run, check again"]
youtube:
  title: "Python Lesson 1.3: Errors Are Clues - Reading Error Messages | Introduction to Python"
  description: |
    Every programmer sees errors every day. Pip the Python shows you how to read Python's red error messages like a detective:
    which line, what kind of error, and what to fix. We make three classic mistakes on purpose, fix each one,
    and run the program again. Finish with a bug-hunt exercise.
    For beginners aged 7 to 20.
  tags: [python errors, python for beginners, syntaxerror, nameerror, debugging for kids, learn python, fun skill builders]
---

<!-- Booklet 1.8 smoke testing; capitals matter (deliberate mistake from the earlier recording notes). -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Today we're going to do something that sounds strange. We're going to make mistakes on purpose! Because every programmer, even the experts, sees errors every single day. The trick is knowing how to read them.

## STUDY | Errors are normal
@ point Errors are not failures. They are clues.
When Python can't understand your code, it stops and shows an error message, often in red. That can feel scary at first. But an error is not Python being angry with you. It's Python giving you a clue about what went wrong.
@ point Python is very fussy about details
Python is a bit like a very strict spelling teacher. A missing bracket, a missing quote mark, or a capital letter in the wrong place, and it stops. A person would guess what you meant. Python never guesses. It needs everything exactly right.
@ point Finding and fixing mistakes is called debugging
Finding and fixing mistakes has a special name: debugging. The story goes that, long ago, engineers found a real moth stuck inside a computer and taped it into their notebook. Today, a bug just means a mistake in code.

## STUDY | How to read an error
@ snippet Traceback (most recent call last):\n  File "hello.py", line 1\nNameError: name 'Print' is not defined
An error message has a few parts. Let's read one like a detective, from the bottom up.
@ point Last line: the TYPE of error and what it means
The last line is the most important. It tells you the type of error, like NameError or SyntaxError, followed by a short explanation.
@ point "line 1": WHERE Python got stuck
Above that, Python tells you the line number where it got stuck. Go to that line first. Sometimes the real mistake is just one line above it.
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
@ run | NameError: Python doesn't know "Print"
Let's run it. Error! Read the last line: NameError, name capital Print is not defined. Python is even kind enough to ask: did you mean print with a small p? Python is case sensitive, which means capital letters and small letters are different to it.
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
Run. IndentationError, unexpected indent. Python uses spaces at the start of a line to group code, which we'll learn about later. Here they don't belong.
@ edit 2 => print("Bye!")
Remove the spaces.
@ run | Every fix = run again
And run. Both lines work. Three bugs found, three bugs fixed. You're a real debugger now!

## REVISE | Quick revise
@ point An error is a clue, not a failure
An error is a clue, not a failure.
@ point Read the last line first, then find the line number
Read the last line for the type of error, then go to the line number.
@ point NameError, SyntaxError, IndentationError
NameError means an unknown word. SyntaxError means broken grammar. IndentationError means unexpected spaces.
@ point Fix one thing, then run again
And fix one thing at a time, then run again to check.

## PRACTICE | Bug hunt
@ task This program has 2 bugs. Find and fix them:\nprint("I like pizza")\nPrint("I like cake)
Here's a bug hunt. This little program has two bugs hiding in it. Can you find both and fix them?
@ hint Look closely at capital letters and quote marks.
Hint: check capital letters, and check that every quote mark has a partner.
@ pause 12
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
And now both lines work. Notice how we fixed one error at a time and ran again each time. That's exactly how real programmers do it.

## OUTRO
Great detective work! Errors are now your friends. Next time, we'll put everything together and build a fun welcome card program with borders and patterns. Like, share and subscribe, and keep coding. Happy Learning!
