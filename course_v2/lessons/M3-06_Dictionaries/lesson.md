---
id: "3.6"
title: "Dictionaries"
module: 3
module_title: "Data Structures"
next: "Records and Fields"
minutes: 8.71
thumb_code: 'capitals["France"]'
goals: ["Keys and values", "Looking up, adding and changing entries", "Checking for a key with in", "Looping through a dictionary"]
youtube:
  title: "Python Lesson 3.6: Dictionaries - Keys and Values | Introduction to Python"
  description: |
    Dictionaries store information with labels instead of position numbers. Ziggy the Python explains keys and
    values with a real dictionary, then we look up capital cities, add and change entries, avoid a KeyError with
    in and get(), loop through a dictionary, and count votes for favourite fruits.
    For beginners aged 7 to 20.
  tags: [python dictionary, python dict for beginners, keys and values python, keyerror python, learn python, fun skill builders]
---

<!-- Booklet chapter 3: dictionaries (associative arrays). -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Lists are great, but finding something by its position isn't always handy. Do you remember which index your best friend's phone number is at? Of course not! You look it up by their name. Today we'll learn dictionaries, which store information with labels, so you can look things up by name.

## STUDY | A real dictionary
@ point A dictionary: look up a WORD, get its MEANING
Think about a real dictionary book. You don't look up the word python by its page number. You look up the word, and it gives you the meaning. The word is the thing you search for, and the meaning is the thing you get back.
@ point Python dictionary: look up a KEY, get its VALUE
A Python dictionary works the same way. Each entry has a key, which is the label you look up, and a value, which is the information stored with it. Key and value, always in pairs.
@ table Key | Value ; "France" | "Paris" ; "Japan" | "Tokyo" ; "Kenya" | "Nairobi"
Here's a dictionary of countries and their capital cities. Look up the key France, and you get the value Paris. Look up Japan, and you get Tokyo.
@ point Keys are unique: each key appears only once
Each key can only appear once in a dictionary, just like each word appears once in a real dictionary. But different keys can have the same value.
@ point Other names: map, hash table, associative array
Other languages call this a map, a hash table, or an associative array, as the booklet does. They all mean the same idea: keys linked to values.

## STUDY | Writing a dictionary
@ snippet capitals = {"France": "Paris",\n            "Japan": "Tokyo"}
In Python, a dictionary uses curly brackets. Inside, each entry is a key, a colon, and a value. Entries are separated by commas.
@ point Look up: capitals["France"]
To look something up, use square brackets with the key inside, instead of an index number.
@ point Add or change: capitals["Peru"] = "Lima"
To add a new entry, or change an existing one, use the key in square brackets and an equals sign. If the key is new, it's added. If it already exists, its value is replaced.
@ point Keys are usually strings or numbers
Keys are usually strings or numbers. Values can be anything at all: strings, numbers, booleans, lists, or even other dictionaries.
@ point {} is an empty dictionary
And a pair of curly brackets with nothing inside makes an empty dictionary, ready to fill.

## CODE | capitals.py
```python
capitals = {"France": "Paris",
            "Japan": "Tokyo",
            "Kenya": "Nairobi"}
print(capitals["Japan"])
capitals["Peru"] = "Lima"
capitals["Japan"] = "TOKYO"
print(capitals)
print(len(capitals))
print(capitals["Spain"])
```
@ line 1-3 | Keys and values in curly brackets
Lines one to three make a dictionary of three countries and their capitals. The key comes first, then a colon, then the value.
@ line 4 | Look up by key
Line four looks up Japan.
@ run | Look up a key, get its value
Run. Tokyo. We found it by its name, not by its position.
@ line 5 | A new key: added
Line five adds a new entry: Peru, with Lima.
@ line 6 | An existing key: replaced
Line six uses a key that already exists, Japan, and gives it a new value in capitals.
@ line 7-8 | Print it all, and count the entries
Lines seven and eight print the whole dictionary, and its length.
@ predict 6 | How many entries now? What will Japan be?
How many entries does the dictionary have now? And what is Japan's value?
@ run | 4 entries; Japan was replaced, not added
Run. The dictionary now has Peru on the end, and Japan's value is TOKYO in capitals. The length is four, not five, because setting Japan again replaced the old value. Keys are unique.
@ line 9 | Look up a key that isn't there
Finally, line nine looks up Spain, which isn't in the dictionary.
@ predict 4 | Spain isn't a key. What happens?
What do you think will happen?
@ run | KeyError: that key doesn't exist
Run. KeyError: Spain. A KeyError means you asked for a key that doesn't exist. It's the dictionary version of an IndexError.

## CODE | safe_lookup.py
```python
sounds = {"cat": "meow", "dog": "woof", "cow": "moo"}
print("dog" in sounds)
print("fish" in sounds)
print(sounds.get("cow"))
print(sounds.get("fish"))
print(sounds.get("fish", "...silence"))
```
@ say
So how do we avoid a KeyError? There are two good ways.
@ line 1 | Animals and their sounds
A dictionary of animals and the sounds they make.
@ line 2-3 | in checks the KEYS
Lines two and three use in to check whether a key exists. With a dictionary, in looks at the keys, not the values.
@ line 4 | .get(key): no crash if it's missing
Line four uses dot get to look up cow. Get does the same job as square brackets, but it doesn't crash when the key is missing.
@ line 5 | .get() of a missing key
Line five uses get with fish, which is missing.
@ line 6 | .get(key, default): your own fallback
And line six gives get a second value: a default, to use if the key is missing.
@ predict 6 | What does .get() give for a missing key?
What do you think get gives back when the key is missing?
@ run | None, or your default
Run. Dog is a key: True. Fish isn't: False. Cow says moo. Then, for fish, get gives None. None is Python's special value meaning nothing at all. And with a default, we get dot dot dot silence. No crashes anywhere.

## CODE | loop_dict.py
```python
ages = {"Asha": 11, "Leo": 14, "Mia": 9}
for name in ages:
    print(name, "is", ages[name])
for name, age in ages.items():
    print(f"{name} will be {age + 1} next year")
print(list(ages.keys()))
print(list(ages.values()))
```
@ say
Loops work with dictionaries too.
@ line 1 | Names and ages
A dictionary of names and ages.
@ line 2-3 | Looping over a dictionary gives its KEYS
Looping over a dictionary gives you each key in turn. So name is each name, and we look up the age with square brackets.
@ run | Each key, with its value
Run. Asha is eleven, Leo is fourteen, Mia is nine. Dictionaries remember the order the entries were added.
@ line 4 | .items() gives key AND value together
Line four uses dot items, which gives the key and the value together. We use two loop variables, name and age, separated by a comma.
@ line 5 | Use both in an f-string
Line five uses both in an F string.
@ line 6-7 | .keys() and .values()
And lines six and seven get just the keys, and just the values, turned into lists.
@ run | items(), keys(), values()
Run. Next year's ages for everyone. Then a list of the names, and a list of the ages. These three methods, items, keys and values, are your main tools for working through a dictionary.

## CODE | votes.py
```python
votes = ["mango", "apple", "mango", "kiwi", "mango", "apple"]
counts = {}
for fruit in votes:
    if fruit in counts:
        counts[fruit] = counts[fruit] + 1
    else:
        counts[fruit] = 1
print(counts)
```
@ say
Here's a classic use for a dictionary: counting votes. This one uses a sneak peek of if and else, which we'll learn properly in Module Four.
@ line 1 | Six votes for favourite fruit
A list of six votes for favourite fruit.
@ line 2 | An empty dictionary to count with
An empty dictionary to hold the counts.
@ line 3 | Look at each vote
We loop through every vote.
@ line 4-5 | Seen it before? Add 1
If this fruit is already a key, we add one to its count.
@ line 6-7 | First time? Start at 1
Otherwise, it's the first vote for this fruit, so we set its count to one.
@ line 8
And we print the counts.
@ predict 6 | Count the votes: who wins?
Count the votes yourself. Which fruit wins, and by how much?
@ run | Mango wins with 3 votes
Run. Mango three, apple two, kiwi one. Mango wins! This exact pattern is used to count words in books, likes on posts and votes in elections.

## STUDY | List or dictionary?
@ table Use a list when... | Use a dictionary when... ; order matters: a queue, a playlist | you look things up by name ; items are all the same kind | each value has a label ; you go through items one by one | you need a quick answer to "what is X?"
How do you choose between a list and a dictionary? Use a list when the order matters, like a queue or a playlist, and when you mostly go through the items one by one. Use a dictionary when each value has a label, and you want to look things up by that label, like a phone book, a game's settings, or the prices in a shop.
@ point Dictionaries find keys very fast, even with millions of entries
And here's a bonus fact. Dictionaries are incredibly fast at finding a key. Even with millions of entries, looking up one key takes almost no time at all. That's why they're used inside search engines, databases and games.

## STUDY | Common mistakes
@ table Mistake | What happens ; capitals[0] | KeyError: dictionaries use keys, not positions ; {"a": 1, "a": 2} | only one "a" is kept: the last one ; capitals["france"] | KeyError: keys are case-sensitive ; ["France": "Paris"] | SyntaxError: use curly brackets
Common dictionary mistakes. Dictionaries don't have positions, so index zero gives a KeyError, unless zero is actually a key. Repeating a key keeps only the last value. Keys are case sensitive, so france with a small f isn't the same as France. And dictionaries need curly brackets, not square ones.

## REVISE | Quick revise
@ point A dictionary links keys to values: {key: value}
A dictionary links keys to values, inside curly brackets.
@ point d[key] looks up; d[key] = value adds or changes
Square brackets look up a value. Square brackets and equals add or change one.
@ point Missing key → KeyError; use in or .get()
A missing key gives a KeyError. Check with in, or use get.
@ point Loop with for key in d, or for k, v in d.items()
Loop through the keys, or use items for keys and values together.

## PRACTICE | Pet sounds
@ task Make a dictionary of 4 animals and their sounds.\n1. Print the sound for one animal\n2. Add a new animal\n3. Loop and print: The cat says meow
Your turn. Make a dictionary of four animals and the sounds they make. Print the sound for one animal. Add a fifth animal. Then use a loop with items to print a sentence for each one, like: the cat says meow.
@ hint for animal, sound in sounds.items():
Hint: use for animal comma sound in sounds dot items.
@ pause 15
Pause the video and try it.

## ANSWER | pet_sounds.py
```python
sounds = {"cat": "meow", "dog": "woof",
          "duck": "quack", "sheep": "baa"}
print(sounds["duck"])
sounds["owl"] = "hoot"
for animal, sound in sounds.items():
    print(f"The {animal} says {sound}")
```
@ line 1-2
Four animals and their sounds.
@ line 3
Look up the duck.
@ line 4
Add an owl.
@ line 5-6
And loop with items.
@ run
Run. Quack. Then the cat says meow, the dog says woof, the duck says quack, the sheep says baa, and the owl says hoot. Brilliant!

## OUTRO
Wonderful! Dictionaries are one of Python's most powerful tools, and you've just learned them. Next time, we'll use dictionaries to build records: all the details about one person or thing, stored together. Like, share and subscribe, and keep coding. Happy Learning!
