---
id: "2.3"
title: "Strings: Playing with Text"
module: 2
module_title: "Variables, Input and Output"
next: "Asking Questions with input()"
minutes: 5.6   # rendered video length
thumb_code: 'print(f"Hi {name}!")'
goals: ["What strings are", "Joining text with +", "len() and .upper()", "f-strings"]
youtube:
  title: "Python Lesson 2.3: Strings and f-strings - Playing with Text | Introduction to Python"
  description: |
    Text in Python is called a string. Pip the Python shows how to join strings with plus, measure them with len,
    change them with upper and lower, and build sentences the easy way with f-strings.
    Type each line with us, see the output, then try the name badge exercise.
    For beginners aged 7 to 20.
  tags: [python strings, f-strings, python for beginners, string methods, learn python, python for kids, fun skill builders]
---

<!-- Booklet 2.2.1 Text (Strings). -->

## INTRO
Hello, Happy Learners! It's Pip the Python here. Today we're playing with text. You'll learn how to join words together, count letters, shout in capitals, and build sentences with a trick that professional programmers use every day.

## STUDY | What is a string?
@ point A string is text inside quote marks
A string is a piece of text inside quote marks. It can be a letter, a word, a whole sentence, or even an empty pair of quotes with nothing inside.
@ point Each character is a bead on a string
Why is it called a string? Picture a necklace of beads. Each bead is one character: a letter, a digit, a space or a symbol. They're threaded together in order, and that's a string.
@ snippet 'single quotes'  or  "double quotes"
Python lets you use single quote marks or double quote marks. Both work the same. Just make sure the start and end match. Double quotes are handy when your text contains an apostrophe, like in the word don't.
@ point "7" is text. 7 is a number.
Here's an important detail. Seven in quote marks is text, just a picture of the digit. Seven without quotes is a real number that you can do maths with. Python treats them very differently.

## STUDY | Tools for text
@ snippet "Pip" + " " + "Python"
You can join strings with a plus sign. This is called concatenation. It glues the strings end to end, so if you want a space between words, you have to add it yourself.
@ point len(text) counts the characters
The len function, short for length, counts how many characters are in a string. Spaces count too!
@ point text.upper() and text.lower() change the case
Strings also come with built-in tools called methods. You use them with a dot after the string. Dot upper makes every letter a capital. Dot lower makes every letter small.
@ snippet f"Hello, {first}!"
And now the superstar: F strings. Put the letter f just before the opening quote mark. Then, anywhere inside the string, put a variable name in curly brackets. Python swaps it for the variable's value. It's like a fill in the blanks sentence.
@ point Level up: strings are immutable
For the curious: strings in Python are immutable, which means they can't be changed once they're made. Dot upper doesn't change the original string. It makes a brand new one, in capitals.

## CODE | strings.py
```python
first = "Pip"
last = "Python"
full = first + " " + last
print(full)
print(len(full))
print(full.upper())
print(f"Hello, {first}! Nice to meet you.")
```
@ say
Let's code it. Type each line with me.
@ line 1-2 | Two string variables
Lines one and two make two string variables: first and last.
@ line 3 | + glues strings together
Line three joins them: first, plus a space in quotes, plus last. The result is stored in a new variable called full.
@ line 4
Line four prints full.
@ line 5 | len() counts characters, spaces too
Line five prints the length of full. Before we run it, count the letters. Don't forget the space!
@ line 6 | .upper() = all capitals
Line six prints full in capital letters, using the dot upper method.
@ line 7 | f"...{variable}..." fills in the value
And line seven uses an F string. The f goes before the quote, and first goes inside curly brackets.
@ run | Pip Python = 10 characters
Let's run it. Pip Python, joined with a space. Ten, because three letters, plus one space, plus six letters, makes ten. Then the name in capitals. And finally, our F string has swapped in the name: Hello, Pip! Nice to meet you.

## CODE | shout.py
```python
word = "python"
print(word * 3)
print(word.capitalize())
print(word.replace("p", "j"))
print(f"{word} has {len(word)} letters")
```
@ say
Let's try a few more string tools, because strings can do a lot.
@ line 1
We start with one word, all in small letters.
@ line 2 | text * number repeats it
Line two repeats it three times, using the star trick from our welcome card.
@ line 3 | .capitalize() = first letter big
Line three uses dot capitalize, which makes just the first letter a capital.
@ line 4 | .replace(old, new) swaps letters
Line four uses dot replace. It swaps every small p for a j. Can you guess the new word?
@ line 5 | len() inside an f-string
And line five uses len inside an F string.
@ run | The original word never changed
Run it. Python three times in a row, Python with a capital P, jython, and python has six letters. And notice: the last line still says python. None of the methods changed the original word. They each made a new string. That's what immutable means.

## REVISE | Quick revise
@ point A string is text in quotes; "7" is not the number 7
A string is text in quote marks, and a digit in quotes is text, not a number.
@ point + joins strings (add your own spaces)
Plus joins strings together, so remember to add your own spaces.
@ point len() counts, .upper() and .lower() change case
len counts characters, while dot upper and dot lower change the case.
@ point f"{name}" puts a variable's value inside text
And F strings put a variable's value right inside your text.

## PRACTICE | Name badge
@ task Make variables for your first name and your hobby. Use an f-string to print:\nHELLO, MY NAME IS ASHA\nI love drawing and my name has 4 letters.
Your turn: make a name badge. Create variables for your first name and your hobby. On the first line, print hello my name is, followed by your name, all in capital letters. On the second line, use an F string to say what you love and how many letters are in your name.
@ hint .upper() for capitals. len(name) inside the curly brackets counts letters.
Hint: use dot upper for the capitals. And yes, you can put len of name directly inside the curly brackets of an F string.
@ pause 15
Pause the video and make your badge.

## ANSWER | name_badge.py
```python
name = "Asha"
hobby = "drawing"
print("HELLO, MY NAME IS " + name.upper())
print(f"I love {hobby} and my name has {len(name)} letters.")
```
@ line 1-2
Two string variables: name and hobby.
@ line 3
Line three joins the text with name dot upper, so the name is in capitals too.
@ line 4
Line four is an F string with two blanks: hobby, and len of name.
@ run
Run it. HELLO, MY NAME IS ASHA. I love drawing and my name has four letters. Try it with your own name. The letter count updates by itself!

## OUTRO
Fantastic! You're now a string expert. Next time, our programs will start a conversation, asking questions and listening to the answers with the input function. Like, share and subscribe, and keep coding. Happy Learning!
