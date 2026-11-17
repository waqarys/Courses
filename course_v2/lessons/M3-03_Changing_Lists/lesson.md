---
id: "3.3"
title: "Changing Lists"
module: 3
module_title: "Data Structures"
next: "Going Through a List with for"
minutes: 8.71
thumb_code: 'basket.append("milk")'
goals: ["Lists are mutable: they can change", "append, insert, remove and pop", "Changing an item by its index", "sort, and checking with in"]
youtube:
  title: "Python Lesson 3.3: Changing Lists - append, insert, remove, pop, sort | Introduction to Python"
  description: |
    Lists can grow, shrink and change while your program runs. Ziggy the Python builds a shopping list step by
    step with append, insert, remove and pop, swaps items by index, sorts a list, and checks for items with in.
    We predict the list after every change and meet the errors you get when an item isn't there.
    For beginners aged 7 to 20.
  tags: [python list methods, python append, python remove pop, python sort list, learn python, fun skill builders]
---

<!-- Booklet chapter 3: arrays/lists, mutability. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Real lists change all the time. You add songs to a playlist, cross things off a to do list, and move your favourite game to the top. Today we'll learn the list methods that let our programs add, remove, change and sort items, while the program is running.

## STUDY | Lists can change
@ point Lists are mutable: they can be changed
Remember that strings can't be changed? Every string method made a brand new string. Lists are different. Lists are mutable, which means they can be changed in place. The same list can grow, shrink, and have its items swapped.
@ point Methods use a dot: basket.append("milk")
We change a list using methods, with a dot, just like dot upper on a string. The list's name, a dot, the method's name, and round brackets.
@ point Most list methods change the list and give back nothing
Here's an important difference. List methods like append change the list itself. They don't give you a new list. So you don't need to store the result. You just call the method, and the list is different afterwards.
@ snippet basket[0] = "bread"
You can also change one item directly, using its index and an equals sign. This replaces whatever was at index zero.

## STUDY | The list toolbox
@ table Method | What it does ; .append(x) | add x to the END ; .insert(i, x) | put x at index i, shuffling the rest along ; .remove(x) | remove the first x found ; .pop() | remove and give back the last item ; .sort() | put the items in order
Here's the toolbox. Append adds an item to the end. Insert puts an item at a particular index, and everything after it shuffles along by one. Remove takes out the first matching item. Pop removes the last item and gives it back to you, so you can use it. And sort puts the items in order: alphabetical for strings, smallest to largest for numbers.
@ point Like a queue: append joins the back, insert pushes in
Think of a queue for the cinema. Append is someone joining the back of the queue. Insert is someone pushing in at a particular place, and everyone behind them moves back one.
@ point pop() is like taking the top plate off a stack
Pop is like taking the top plate off a stack of plates. It's gone from the stack, and now it's in your hand.

## CODE | shopping.py
```python
basket = ["eggs", "rice"]
print(basket)
basket.append("milk")
print(basket)
basket.insert(0, "bread")
print(basket)
basket.remove("rice")
print(basket)
last = basket.pop()
print("Took out:", last)
print(basket)
```
@ line 1-2 | Start with two items
Let's build a shopping list step by step. We start with eggs and rice, and print the list.
@ line 3 | append: add to the end
Line three appends milk.
@ line 4
And prints the list.
@ predict 4 | Where will milk go?
Where in the list will milk appear?
@ run | append adds to the END
Run. Eggs, rice, then milk at the end. Append always adds to the end.
@ line 5 | insert(0, ...): push in at the front
Line five inserts bread at index zero, the very front.
@ line 6
Print it.
@ line 7 | remove: take out an item by value
Line seven removes rice. Notice that we give remove the item itself, not its index.
@ line 8
Print again.
@ predict 6 | What will the list look like after insert and remove?
After inserting bread at the front and removing rice, what will the list look like?
@ run | bread, eggs, milk
Run. Bread, eggs, rice, milk after the insert. Then bread, eggs, milk after rice is removed.
@ line 9 | pop(): remove the last item AND keep it
Line nine pops the last item off the list, and stores it in a variable called last.
@ line 10-11 | Show what came out, and what's left
Lines ten and eleven show what came out, and what's left.
@ run | pop() hands the item back to you
Run. Took out: milk. And the list is now bread and eggs. Pop removed milk from the list, but because it handed milk back to us, we could still print it.

## CODE | top_scores.py
```python
scores = [40, 95, 72, 18]
scores[3] = 60
print(scores)
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)
print("Best:", scores[0])
print(100 in scores)
```
@ say
Now let's change items directly, and sort a list.
@ line 1 | Four scores
Four scores in a game.
@ line 2 | Replace the item at index 3
Line two replaces the item at index three. That's the fourth score, eighteen. It becomes sixty.
@ line 3
Print the list.
@ line 4 | sort(): smallest to largest
Line four sorts the list.
@ line 5
And prints it again.
@ predict 5 | What will the list be after the change, and after sorting?
What will the two printed lists look like?
@ run | Change by index, then sort
Run. Forty, ninety five, seventy two, sixty, with the eighteen replaced. Then sorted from smallest to largest: forty, sixty, seventy two, ninety five.
@ line 6 | reverse=True: largest first
Line six sorts again, but with reverse equals True. That puts the largest first, like a leaderboard.
@ line 7-8 | Print it, and the best score
Line seven prints it, and line eight prints the best score, which is now at index zero.
@ line 9 | in checks if a value is in the list
And line nine checks whether one hundred is in the list.
@ run | A leaderboard in two lines
Run. Ninety five, seventy two, sixty, forty. Best: ninety five. And one hundred is not in the list: False. Sorting in reverse is a really common way to make a high score table.

## CODE | playlist.py
```python
playlist = ["Roar", "Happy", "Shake", "Happy"]
print(len(playlist))
print(playlist.count("Happy"))
print(playlist.index("Shake"))
del playlist[0]
print(playlist)
playlist.extend(["Firework", "Hello"])
print(playlist)
print(len(playlist))
```
@ say
Let's look at a few more tools, using a music playlist. Watch how the length changes as we go.
@ line 1 | Four songs, one appears twice
Our playlist has four songs, and one of them, Happy, appears twice. Lists are allowed to contain duplicates.
@ line 2 | How many songs?
Line two prints the length.
@ line 3 | .count(x): how many times x appears
Line three uses dot count, which counts how many times an item appears in the list.
@ line 4 | .index(x): WHERE x is
Line four uses dot index, which tells us the position of an item.
@ predict 5 | Length? How many Happys? Where is Shake?
Predict the three answers. Remember that positions start at zero.
@ run | 4 songs, 2 Happys, Shake at index 2
Run. Four songs. Happy appears twice. And Shake is at index two: Roar is zero, Happy is one, Shake is two.
@ line 5 | del removes by INDEX
Line five uses the word del, short for delete, to remove the item at index zero. Remove works with a value, but del works with a position.
@ line 6
Print the list.
@ line 7 | .extend() adds a whole list to the end
Line seven uses dot extend, which adds every item from another list onto the end. Append would add the whole list as one single item, but extend adds them one by one.
@ line 8-9 | Print it and count again
Print the playlist, and its new length.
@ run | Roar is gone, two new songs added
Run. Roar is gone, so we have Happy, Shake and Happy. Then Firework and Hello are added on the end, and the length is now five. The same list changed three times while the program ran, and the variable name never changed.

## CODE | oops.py
```python
pets = ["cat", "dog"]
pets.remove("fish")
```
@ say
What happens when we try to remove something that isn't there?
@ line 1 | Only a cat and a dog
A list with a cat and a dog.
@ line 2 | Remove a fish?
Line two tries to remove a fish.
@ predict 4 | There's no fish. What happens?
There's no fish in the list. Will Python ignore it, or complain?
@ run | ValueError: the item isn't in the list
Run. ValueError: list remove, x not in list. Python can't remove something that isn't there.
@ edit 2 => print("fish" in pets)
A safer approach is to check first with in. Later, when we learn if statements, we'll only remove an item when it's really there.
@ run | Check first with in
Run. False. No fish, so we know not to remove it.

## STUDY | Common mistakes
@ table Mistake | What happens ; basket = basket.append("tea") | basket becomes None: append returns nothing ; basket.append("tea", "jam") | TypeError: append takes ONE item ; basket.remove(0) | removes the VALUE 0, not index 0 ; sorting a mix of numbers and text | TypeError: can't compare them
Here are the mistakes to avoid. Writing basket equals basket dot append is a classic. Append changes the list and gives back nothing, which Python calls None, so you'd lose your whole list. Append only takes one item at a time. Remove looks for a value, not an index. And you can't sort a list that mixes numbers and strings, because Python can't decide which comes first.

## REVISE | Quick revise
@ point Lists are mutable: they change in place
Lists are mutable. They change in place.
@ point append adds to the end; insert(i, x) puts x at i
Append adds to the end, and insert puts an item at an index.
@ point remove(x) takes out a value; pop() removes and returns the last
Remove takes out a value. Pop removes the last item and gives it back.
@ point list[i] = x replaces; sort() orders; in checks
Index and equals replaces an item, sort puts the list in order, and in checks for an item.

## PRACTICE | To-do list
@ task todo = ["homework", "feed cat", "tidy room"]\n1. Add "read a book" and "call Gran"\n2. Remove "tidy room" (done!)\n3. Sort the list and print it
Your turn. Start with a to do list of three jobs: homework, feed cat and tidy room. Add two more jobs: read a book, and call Gran. Then remove tidy room, because you've done it. Finally, sort the list and print it.
@ hint Two appends, one remove, one sort, one print.
Hint: you'll need two appends, one remove, one sort and one print.
@ pause 15
Pause the video and try it.

## ANSWER | todo.py
```python
todo = ["homework", "feed cat", "tidy room"]
todo.append("read a book")
todo.append("call Gran")
todo.remove("tidy room")
todo.sort()
print(todo)
```
@ line 1
The starting list.
@ line 2-3
Two appends.
@ line 4
Remove tidy room.
@ line 5-6
Sort, then print.
@ run
Run. Call Gran, feed cat, homework, read a book, in alphabetical order. Notice that sort looked at the first letter of each job: c, f, h, r. If one of your jobs started with a capital letter, it would jump to the front, because capitals come before small letters. If yours matches, well done!

## OUTRO
Superb! Your lists can now grow, shrink and get sorted. Next time, we'll learn to go through a list one item at a time with a for loop, which is one of the most powerful ideas in programming. Like, share and subscribe, and keep coding. Happy Learning!
