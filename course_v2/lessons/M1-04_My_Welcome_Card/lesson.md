---
id: "1.4"
title: "Mini-Project: My Welcome Card"
module: 1
module_title: "Getting Started"
next: "Variables: Labelled Boxes"
minutes: 8.49
thumb_code: 'print("*" * 30)'
goals: ["Plan a program before coding", "Repeat a string with *", "Line things up with spaces", "Build a project step by step"]
youtube:
  title: "Python Lesson 1.4: Mini-Project - Make a Welcome Card with print() | Introduction to Python"
  description: |
    Module 1 project! Ziggy the Python shows how real programmers plan first, then build a welcome card one step
    at a time: borders made by repeating a string, centred titles using spaces, and a little ASCII-art picture.
    Then you design and code a birthday card of your own.
    For beginners aged 7 to 20.
  tags: [python project for beginners, python print patterns, ascii art python, python for kids, learn python, fun skill builders]
---

<!-- Module 1 mini-project: planning, string repetition, layout. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Welcome to our first mini project! We'll use everything from this module to build a welcome card in Python, with borders, a title and even a little picture. And we'll do it the way real programmers do: plan first, then build one small step at a time.

## STUDY | Plan before you code
@ point Programmers plan first
Before builders build a house, they draw a plan. Programmers do the same. A few minutes of planning saves a lot of confusion later, because you know exactly what you're trying to make.
@ point Sketch what the output should look like
For a program that prints things, the easiest plan is a sketch of the output. Grab some paper and draw what you want to see in the output panel, line by line.
@ snippet ******************************\n*     WELCOME TO MY CARD     *\n******************************
Here's our sketch. A border of stars on top. A title in the middle with a star at each end. And another border at the bottom.
@ point Then turn each line of the sketch into a print
Once you have the sketch, the code almost writes itself. Each line of the drawing becomes one print. Then we build it a piece at a time and run it after each step: our smoke test from lesson two.

## STUDY | A new trick: repeating strings
@ snippet print("*" * 30)
Typing thirty stars by hand is boring, and it's easy to miscount. Python has a shortcut.
@ point string * number = the string repeated
If you multiply a string by a number, Python repeats the string that many times. Star times thirty gives thirty stars in a row.
@ point Works with any string: "ha" * 3 → hahaha
It works with any string at all. The string h a, times three, gives ha ha ha. And a dash times twenty gives a neat line of twenty dashes.
@ point Spaces are characters too
One more thing to remember: a space is a character too. It takes up room, just like a letter. We'll use spaces to push our title into the middle of the card.

## CODE | repeat_tricks.py
```python
print("*" * 10)
print("ha" * 3)
print("-=" * 8)
print("*" + " " * 8 + "*")
```
@ say
Let's try the repeating trick before we use it in the project.
@ line 1 | Ten stars, no counting
Line one prints a star repeated ten times.
@ line 2 | Repeat a whole word
Line two repeats the string h a three times.
@ predict 4 | What will "ha" * 3 look like?
What will that look like? Will there be spaces between them?
@ run | hahaha: no spaces are added
Run. Ten stars, and hahaha, all squashed together. Python repeats exactly what's in the string, and it doesn't add spaces for you.
@ line 3 | Repeat a pattern of two characters
Line three repeats a two character pattern, a dash and an equals sign, eight times.
@ line 4 | + joins strings: star, 8 spaces, star
Line four joins three strings with plus signs: a star, eight spaces, and another star. A plus sign glues strings together.
@ run | Patterns, and a box side with a gap
Run. A zig zag pattern, sixteen characters long. And a star, a gap of eight spaces, and another star. That's the side of a box! These two tricks are all we need for our card.

## CODE | welcome_card.py
```python
# My welcome card
print("*" * 30)
print("*     WELCOME TO MY CARD     *")
print("*" + " " * 28 + "*")
print("*    Made by Ziggy, 2026     *")
print("*" * 30)
print()
print("   /\\_/\\")
print("  ( o.o )   Have a great day!")
print("   > ^ <")
```
@ say
Now the project. Step one: the top border.
@ line 1 | A comment says what the program is
A comment first, saying what this program is.
@ line 2 | Top border: 30 stars
Then the top border: a star times thirty.
@ run | Smoke test: is the border right?
A quick smoke test. Run it. Thirty stars. Good start.
@ line 3 | The title line, padded with spaces
Step two: the title. A star, five spaces, the words welcome to my card, five more spaces and a star. I counted the characters so that this line is thirty wide, the same as the border.
@ line 4 | An empty row: 28 spaces between stars
Line four is an empty row inside the card. A star, twenty eight spaces, a star. Twenty eight plus two stars makes thirty.
@ line 5 | A signature line
Line five is a signature, again padded with spaces to be thirty wide.
@ line 6 | Bottom border
Then the bottom border, the same as the top.
@ predict 4 | Will the edges line up?
Here's the big question. Did I count correctly? Will the right hand edge of the card line up?
@ run | Everything lines up at 30 characters
Run. Yes! Every line is exactly thirty characters wide, so the stars on the right line up perfectly. Our editor uses a font where every character has the same width, which makes lining things up possible.
@ line 7 | A blank line
Step three: a little picture. First a blank line for spacing.
@ line 8-10 | A cat made of symbols
Then three lines that draw a cat's face with symbols. Look carefully at line eight. The cat's ears use backslashes, and we have to type each one twice. A backslash has a special job inside a string, so two backslashes are needed to print one.
@ run | Plan, build, test: finished!
Run the whole thing. Our card with its border, title and signature, then a blank line, and a cat wishing us a great day. Each backslash pair printed as a single backslash. Plan, build a step, test it, repeat. That's how every big program gets made.

## CODE | tree.py
```python
print(" " * 4 + "*")
print(" " * 3 + "*" * 3)
print(" " * 2 + "*" * 5)
print(" " * 1 + "*" * 7)
print("*" * 9)
print(" " * 4 + "|")
```
@ say
Let's add a decoration to our card, and this time we'll let Python count the spaces for us. We're going to draw a tree.
@ line 1 | 4 spaces, then 1 star
Line one: a space times four, joined to a single star. That's four spaces, then the tip of the tree.
@ line 2 | 3 spaces, then 3 stars
Line two: three spaces, then three stars. One less space, two more stars.
@ predict 5 | Spot the pattern: what comes next?
Can you spot the pattern? What do you think line three will be? Pause and guess.
@ line 3-4 | The pattern continues
Line three: two spaces and five stars. Line four: one space and seven stars. Each line, the spaces go down by one and the stars go up by two.
@ line 5 | No spaces, 9 stars
Line five has no spaces at all, just nine stars, the widest part of the tree.
@ line 6 | The trunk sits in the middle
And line six is the trunk: four spaces and a straight line, which is called a pipe symbol. Four spaces puts it right in the middle, under the tip.
@ run | A tree, built from a pattern
Run. A tree! Every row is centred, and we never typed a long row of spaces by hand. Spotting a pattern like this is a real programming skill. Later in the course, we'll learn loops, which let Python repeat a pattern like this for us, so a tree with a hundred rows would take just a few lines of code.

## STUDY | Make it yours
@ point Swap the characters: # = ~ + o
Before we finish, here are some ways to make the card your own. Swap the stars for other characters. The hash, equals, wavy line, plus and the letter o all make great borders.
@ point Try two-character patterns: "<>" * 15
Try a pattern of two characters, like a less than and greater than sign repeated fifteen times. Fifteen times two is still thirty characters wide.
@ point Draw your own picture with symbols
And draw your own picture. A fish, a house, a face, a rocket. Draw it on squared paper first, one character per square, then copy it into print lines.
@ point Remember: \\ prints one backslash
If your picture uses backslashes, remember to double them. Two backslashes print one.

## STUDY | Common mistakes
@ table Problem | Likely cause ; right edge is wobbly | a line has too many or too few spaces ; SyntaxError on a picture line | a single backslash just before a quote mark ; stars squashed together | forgot that * repeats with no spaces
If the right edge of your card is wobbly, one line has too many or too few spaces. Count the characters, or use the repeating trick for the spaces too. If you get a strange SyntaxError on a picture line, look for a single backslash right before a quote mark. Doubling it fixes the problem.

## REVISE | Quick revise
@ point Plan first: sketch the output
Plan first by sketching your output.
@ point "*" * 30 repeats a string
A string times a number repeats the string.
@ point + joins strings; spaces are characters
A plus sign joins strings, and spaces count as characters.
@ point Build a bit, run, check, repeat
And build a little, run, check, and repeat.

## PRACTICE | Your turn
@ task Make a birthday card:\n- a border made of # (use repetition)\n- a "HAPPY BIRTHDAY" line that lines up with the border\n- the person's name and a short message\n- bonus: a small picture made of symbols
Your turn. Design a birthday card for someone you know. Use the hash symbol for the border, with the repeating trick. Add a happy birthday line that lines up with the border, the person's name, and a short message. For a bonus, add a small picture made of symbols.
@ hint Sketch it first. Make every line the same width: count the characters.
Hint: sketch it first, then make every line the same width as the border.
@ pause 15
Pause the video and build your card.

## ANSWER | birthday_card.py
```python
print("#" * 24)
print("#   HAPPY BIRTHDAY!    #")
print("#     Dear Grandma     #")
print("#  Love from Sam  :)   #")
print("#" * 24)
```
@ line 1
Here's one version. A border of twenty four hash symbols.
@ line 2-4
Three lines, each starting and ending with a hash and padded with spaces to be twenty four characters wide.
@ line 5
And the bottom border.
@ run
Run it. A neat birthday card with straight edges. Yours can be bigger, smaller, or full of pictures. If the edge wobbles, count your spaces again, and remember, that's just debugging.

## OUTRO
Congratulations! You've finished Module One and built your first project. Next module, we'll learn about variables: labelled boxes that let a program remember things. Like, share and subscribe, and keep coding. Happy Learning!
