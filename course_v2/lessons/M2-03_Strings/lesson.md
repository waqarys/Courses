---
id: "2.3"
title: "Strings: Playing with Text"
module: 2
module_title: "Variables, Input and Output"
next: "Asking Questions with input()"
minutes: 9.09
thumb_code: 'f"Hello, {name}!"'
goals: ["What a string is", "Joining strings with +", "len(), .upper() and .lower()", "Building sentences with f-strings"]
youtube:
  title: "Python Lesson 2.3: Strings - Joining, len(), upper() and f-strings | Introduction to Python"
  description: |
    Text in Python is called a string. Ziggy the Python shows how to join strings with plus, measure them with len,
    change them with upper and lower, and build sentences the easy way with f-strings. We make name badges and
    a shouting machine line by line, predict the outputs, and meet the mistakes everyone makes with strings.
    For beginners aged 7 to 20.
  tags: [python strings, python f-strings, string methods python, python len, python for beginners, learn python, fun skill builders]
---

<!-- Booklet chapter 2: data types (string). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Today we're playing with text. You'll learn how to join words together, count letters, shout in capitals, and build sentences with a trick that professional programmers use every single day. Text is everywhere in programs, from usernames to game messages, so let's master it.

## STUDY | What is a string?
@ point A string = text inside quote marks
A string is a piece of text inside quote marks. It can be a single letter, a word, a whole sentence, or even an empty pair of quotes with nothing inside, which we call an empty string.
@ point Like beads on a string: characters in a row
Why the name string? Imagine beads threaded on a string, one after another. Each bead is a character: a letter, a digit, a space or a symbol. A string keeps them in order.
@ point "7" is text. 7 is a number.
Here's something important. Seven in quote marks is a string. It's just the symbol for seven, like a picture of the number. Seven without quotes is a real number that you can do maths with.
@ point Store strings in variables
And of course, we can store strings in variables, so we can use them again and again.

## STUDY | Things you can do with strings
@ snippet "Ziggy" + " " + "Python"
You can join strings with a plus sign. This is called concatenation. It glues the strings end to end. If you want a space between the words, you have to add it yourself, as its own little string.
@ point len("Ziggy") counts the characters → 5
The len function, short for length, counts the characters in a string. Len of Ziggy is five. Spaces and symbols count too.
@ point .upper() SHOUTS, .lower() whispers
Strings also have methods. A method is a function that belongs to a value, and you use it with a dot. Dot upper gives you the string in capital letters. Dot lower gives you small letters.
@ snippet f"Hello, {name}!"
And now the superstar: F strings. Put the letter f just before the opening quote mark. Then, anywhere inside the string, put a variable name in curly brackets. Python swaps it for the variable's value. It's like a fill in the blanks sentence.

## CODE | strings.py
```python
first = "Ziggy"
last = "Python"
full = first + " " + last
print(full)
print(len(full))
print(full.upper())
print(f"Hello, {first}! Nice to meet you.")
```
@ line 1-2 | Two strings in two variables
Let's try all of these. Two variables: first stores Ziggy, and last stores Python.
@ line 3 | Join with + (don't forget the space)
Line three joins them with a space in the middle, and stores the result in full.
@ line 4
Line four prints it.
@ line 5 | len() counts every character
Line five prints the length of full.
@ predict 5 | How many characters? Count carefully!
How many characters do you think it will say? Count carefully, and decide whether the space counts.
@ line 6 | .upper() returns a CAPITAL version
Line six prints full in capital letters, using dot upper.
@ line 7 | An f-string fills in the blank
And line seven is an F string, with first in curly brackets.
@ run | Ziggy Python = 12 characters
Let's run it. Ziggy Python, joined with a space. Twelve, because five letters, plus one space, plus six letters, makes twelve. Then the name in capitals. And finally, our F string has swapped in the name: Hello, Ziggy! Nice to meet you.

## CODE | badge.py
```python
name = "Mia"
year = 7
club = "robotics"
print("=" * 20)
print(f"Name: {name}")
print(f"Year: {year}")
print(f"Club: {club.upper()}")
print("=" * 20)
print(f"{name} is in year {year + 1} next year.")
```
@ say
Let's make a name badge. This shows why F strings are so popular.
@ line 1-3 | Three variables, one is a number
Three variables: a name, a school year, which is a number, and a club.
@ line 4 | A border, using string repetition
A border of twenty equals signs, using the repeating trick from Module One.
@ line 5-6 | f-strings work with numbers too
Two F strings. The second one puts a number into the sentence, and F strings handle numbers with no extra work.
@ line 7 | You can call a method inside the braces
Line seven goes further. Inside the curly brackets, we call dot upper on club. You can put small bits of code inside the brackets, not just names.
@ line 8 | Bottom border
The bottom border.
@ line 9 | Even maths inside the braces
And line nine does maths inside the curly brackets: year plus one.
@ predict 5 | What will the last line say?
What will the last line say? Make a prediction.
@ run | Everything inside { } is worked out
Run. A neat badge: Name Mia, Year seven, Club in capitals, ROBOTICS. And the last line: Mia is in year eight next year. Python worked out year plus one, then put the answer into the sentence.

## CODE | shout.py
```python
word = "hello"
print(word.upper())
print(word.lower())
print(word + "!" * 3)
print(word * 2)
print(word)
```
@ say
One more quick example: a shouting machine. Watch carefully, because there's a surprise at the end.
@ line 1
We store the word hello, in small letters.
@ line 2-3 | Shout, then whisper
Line two shouts it with dot upper. Line three whispers it with dot lower.
@ line 4 | Join with three exclamation marks
Line four joins the word with three exclamation marks.
@ line 5 | Repeat the whole word
Line five repeats the whole word twice.
@ line 6 | Has word changed?
And line six prints word itself. We've shouted it and added things to it.
@ predict 5 | Will word still be "hello"?
So, has the word changed? Will it print HELLO with exclamation marks? Or just hello?
@ run | Strings never change: methods make NEW strings
Run. HELLO, hello, hello with three exclamation marks, hellohello. And the last line, just hello, exactly as we stored it. Strings in Python never change. Dot upper and the plus sign make brand new strings, and leave the original alone. Programmers say strings are immutable. If you want to keep a changed version, store it: word equals word dot upper.

## CODE | methods.py
```python
title = "the jungle book"
print(title.title())
print(title.replace("jungle", "python"))
print(title.count("o"))
print("book" in title)
print(len(title))
```
@ say
Here's a level up: four more string tools that are really useful, especially when you start working with lots of text.
@ line 1 | A film title, all in small letters
We store the title of a story, the jungle book, all in small letters.
@ line 2 | .title() capitalises each word
Line two uses dot title. It makes the first letter of every word a capital, like the title of a book.
@ line 3 | .replace(old, new) swaps words
Line three uses dot replace. Inside the brackets, we give it two strings: the old word, and the new word to put in its place.
@ line 4 | .count() counts how many times something appears
Line four uses dot count, to count how many times the letter o appears.
@ line 5 | in asks: is this inside the string?
Line five asks a question using the word in: is the word book inside the title? The answer will be either True or False.
@ line 6
And line six prints the length.
@ predict 6 | How many o's? And how long is it?
Before we run, count the letter o in the jungle book, and count all the characters, including the spaces. Take your time.
@ run | Title case, a swap, a count, True and 15
Run. The Jungle Book, with capital letters. The python book, with jungle swapped out. Two, because there are two o's, both in the word book. Counting by hand is easy to get wrong, which is exactly why we let Python count for us. Then True, because book really is inside the title. And fifteen characters: thirteen letters, plus two spaces. Remember, none of these methods changed title itself. Each one made a new string or a new answer.

## STUDY | Strings in real programs
@ point Usernames, passwords, messages, file names
Strings are everywhere in real programs: usernames, passwords, chat messages, song titles, web addresses and file names. Every time you type into a box on a website, a program receives a string.
@ point Programs clean and check text all the time
Programs spend a lot of time cleaning and checking text. A website might use dot lower to compare email addresses, so that capitals don't matter. A game might use len to make sure a username isn't too long. You now know the tools they use.

## STUDY | Common mistakes
@ table Code | What goes wrong ; "Age: " + 11 | TypeError: can't join text and a number ; print("Hi {name}") | forgot the f: prints {name} ; name.upper | forgot the ( ): nothing happens ; first + last | no space: ZiggyPython
Strings have a few classic traps. Joining a string and a number with plus gives a TypeError, because Python won't guess whether you want maths or text. An F string is the easy fix. If you forget the letter f, the curly brackets are printed exactly as typed. If you forget the round brackets after upper, the method isn't actually run. And when you join two words with plus, don't forget the space.

## REVISE | Quick revise
@ point A string is text in quotes; "7" is not 7
A string is text in quotes, and the string seven is not the number seven.
@ point + joins, * repeats, len() counts
Plus joins strings, star repeats them, and len counts the characters.
@ point .upper() and .lower() make new strings
Dot upper and dot lower make new strings. The original never changes.
@ point f"...{name}..." fills in the blanks
And F strings fill in the blanks with values, numbers, and even small calculations.

## PRACTICE | Name badge
@ task Store your first name and your favourite hobby. Print:\n1. your name in CAPITALS\n2. how many letters your name has\n3. an f-string like: Asha loves drawing!
Your turn. Store your first name and your favourite hobby in two variables. Print your name in capital letters. Then print how many letters your name has. Then use an F string to print a sentence like: Asha loves drawing!
@ hint Use .upper(), len(), and f"{name} loves {hobby}!"
Hint: you'll need dot upper, the len function, and one F string with two sets of curly brackets.
@ pause 15
Pause the video and give it a try.

## ANSWER | my_badge.py
```python
name = "Asha"
hobby = "drawing"
print(name.upper())
print(len(name))
print(f"{name} loves {hobby}!")
```
@ line 1-2
Two variables: name and hobby.
@ line 3-4
Print the name in capitals, and its length.
@ line 5
And an F string with both variables.
@ run
Run. ASHA. Four. Asha loves drawing! Try it with your own name. Does the number of letters match what you expected?

## OUTRO
Fantastic! You're now a string expert. Next time, our programs will start a conversation, asking questions and listening to the answers with the input function. Like, share and subscribe, and keep coding. Happy Learning!
