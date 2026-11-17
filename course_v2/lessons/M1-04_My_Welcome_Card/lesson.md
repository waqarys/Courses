---
id: "1.4"
title: "Mini-Project: My Welcome Card"
module: 1
module_title: "Getting Started"
next: "Variables: Labelled Boxes"
minutes: 4.5   # rendered video length
thumb_code: 'print("*" * 30)'
goals: ["Plan before you code", "Repeat text with a star", "Lay out output neatly", "Build a complete program"]
youtube:
  title: "Python Lesson 1.4: Mini-Project - Make a Welcome Card | Introduction to Python"
  description: |
    Our first mini-project! Pip the Python shows you how to plan a program on paper first, repeat text with the star
    trick to draw borders, and lay out your output neatly. We build a welcome card line by line, run it,
    and then you design a birthday card of your own.
    For beginners aged 7 to 20.
  tags: [python project for beginners, python for kids, print in python, string repetition, learn python, fun skill builders]
---

<!-- Booklet 1.9 mini-project 1 ("Hello World" + intro to the wellbeing project idea). Original design. -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Time for our first mini-project. We'll use everything we've learned so far to build a welcome card that shows up in the output, with a border, your details, and a friendly message. Let's get creative!

## STUDY | Plan first, code second
@ point Real programmers plan before they type
Before builders build a house, they draw a plan. Programmers do the same thing. If you know what the finished output should look like, writing the code becomes much easier.
@ snippet ******************************\n*     WELCOME TO MY PAGE     *\n******************************
Here's our plan. A border of stars at the top, a title in the middle, another border, then some details about me, and a thank-you message at the end. Every line of this picture will be one print.
@ point One print = one line of the picture
So our plan turns straight into code. One print for each line, from top to bottom, in the same order as the picture. That's sequence again, working for us.

## STUDY | The star trick
@ snippet print("*" * 30)
Typing thirty stars by hand is boring, and it's easy to miscount. Python has a trick for this.
@ point Text * number = the text repeated
When you multiply a piece of text by a number, Python repeats the text that many times. So a star in quote marks, times thirty, gives a line of thirty stars. Change the thirty to ten, and the line gets shorter.
@ point Level up: * means different things for different values
Here's something interesting. For numbers, the star means multiply: seven times six is forty two. For text, the star means repeat. The same symbol does different jobs depending on what kind of value it's working with. We'll explore these kinds of values, called data types, in the next module.
@ point Spaces inside quotes are kept exactly
One more tip. Spaces inside quote marks are shown exactly as you type them. We can use them to push words to the middle or line things up neatly, like columns in a table.

## CODE | welcome_card.py
```python
# My welcome card
print("*" * 30)
print("*     WELCOME TO MY PAGE     *")
print("*" * 30)
print()
print("Name:    Asha")
print("Age:     11")
print("Hobbies: drawing and cricket")
print()
print("~" * 30)
print("Thanks for visiting!")
```
@ say
Let's build it, line by line. Type along with me.
@ line 1
We start with a comment that says what the program is.
@ line 2 | "*" * 30 = thirty stars
Line two uses the star trick: a star in quotes, times thirty, for the top border.
@ line 3 | Count: 30 characters wide
Line three is the title. Five spaces, the words, five more spaces, with a star at each end. Together that's exactly thirty characters, the same width as the border.
@ line 4 | Same border again
Line four repeats the border underneath.
@ line 5 | Empty line for spacing
An empty print gives us some breathing space.
@ line 6-8 | Spaces line up the details
Lines six to eight are the details. Look at the spaces after each label. They make the answers line up in a neat column. Use your own name, age and hobbies here.
@ line 9-10 | A wavy border with ~
Another empty line, and then a wavy border, using the tilde symbol, times thirty.
@ line 11
And finally, a friendly message.
@ run | Your plan, now real output
Let's run our card. There it is! A starry border, a title right in the middle, neat details, and a thank-you at the bottom. It looks exactly like the plan we drew. That's the power of planning first.

## REVISE | Quick revise
@ point Plan the output first, then write one print per line
Plan the output first, then write one print for each line.
@ point "text" * number repeats the text
A piece of text times a number repeats the text.
@ point Spaces inside quotes are kept
Spaces inside quote marks are kept, so you can line things up.
@ point print() makes an empty line
And an empty print makes an empty line.

## PRACTICE | Design a birthday card
@ task Make a birthday card for a friend: a border of 25 # symbols at the top and bottom, a "HAPPY BIRTHDAY" line, the friend's name, and a short wish.
Your turn to design. Make a birthday card for a friend. It needs a border of twenty five hash symbols at the top and at the bottom, a happy birthday line, your friend's name, and a short wish.
@ hint "#" * 25 makes the border. Plan it on paper first!
Hint: a hash symbol in quote marks, times twenty five, makes the border. Draw your card on paper first.
@ pause 15
Pause the video and build your card.

## ANSWER | birthday_card.py
```python
print("#" * 25)
print("    HAPPY BIRTHDAY!")
print("    Dear Kabir,")
print("  Have an amazing day!")
print("#" * 25)
```
@ line 1
Here's my version. The top border: twenty five hash symbols.
@ line 2-4
Then three lines with a few spaces in front, so they sit near the middle.
@ line 5
And the bottom border.
@ run
Run it, and our card is ready. Your card can look completely different, with other symbols or more lines. If it runs and looks the way you planned, you've done it!

## OUTRO
Congratulations, you finished Module One! You can write, run and debug programs and design your own output. Next time, we start Module Two with variables: labelled boxes that let your programs remember things. Like, share and subscribe, and keep coding. Happy Learning!
