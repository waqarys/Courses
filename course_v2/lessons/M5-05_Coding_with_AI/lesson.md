---
id: "5.5"
title: "Coding with AI, Wisely"
module: 5
module_title: "Next Steps"
next: "Final Project: Big Five Wellbeing Check-In"
minutes: 7.87
thumb_code: '# AI suggested this. Is it right?'
goals: ["What AI coding helpers can and can't do", "Ask, read, test, understand: checking suggestions", "Finding a bug in AI-written code", "Honesty and privacy when using AI"]
youtube:
  title: "Python Lesson 5.5: Coding with AI Helpers, Wisely | Introduction to Python"
  description: |
    AI helpers can suggest code in seconds, but they can be confidently wrong. Ziggy the Python explains what
    AI coding helpers do, a simple ask, read, test, understand routine, and how to catch the bugs hiding in
    suggested code with good test data. Plus honesty and privacy: what to share and what to keep to yourself.
    For beginners aged 7 to 20.
  tags: [ai coding helper, ai and python, check ai code, coding with ai for beginners, learn python, fun skill builders]
---

<!-- Booklet 1.6: AI helpers. The "AI-written" programs here are written for the lesson to show typical mistakes. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. You've probably heard of AI helpers that can write code when you ask them. They can be really useful. But they also make mistakes, and they sound just as confident when they're wrong as when they're right. Today, you'll learn how to use them wisely, as a helper, not a replacement for your own brain.

## STUDY | What AI helpers do
@ point An AI helper predicts likely text, learned from huge amounts of examples
An AI coding helper is a program that has learned patterns from enormous amounts of text and code. When you ask a question, it predicts what a good answer probably looks like.
@ point Good at: explaining, examples, ideas, spotting typos
That makes it good at explaining an error message in simple words, giving examples, suggesting ideas, and spotting a missing bracket.
@ point But: it doesn't run your code, and it can be confidently wrong
But it doesn't truly understand your program, and it usually doesn't run the code it gives you. So it can produce code that looks perfect, but has a bug. It can even invent functions that don't exist.
@ point You are the programmer. The AI is the assistant.
So here's the golden rule. You are the programmer. The AI is an assistant. If code goes into your program, you are responsible for it, so you must understand it.

## STUDY | Ask, read, test, understand
@ flow Ask a clear question > Read every line of the answer > Test it with normal, boundary and invalid data > Understand it well enough to explain it
Here's a routine to use every time. Ask a clear, specific question. Read every line of the answer, slowly. Test it, using the normal, boundary and invalid data we learned about last time. And make sure you understand it well enough to explain each line to a friend. If you can't explain it, don't use it yet.
@ point Better question: "Why does my loop print 5 times instead of 4?"
A clear question gets a better answer. Help with Python is vague. Why does my loop print five times instead of four, here's my code, is much better.
@ point Ask it to EXPLAIN, not just to do it for you
And when you're learning, ask it to explain, or to give you a hint, rather than to write the whole thing. Your brain only gets stronger when it does the thinking.

## CODE | ai_biggest.py
```python
# Suggested by an AI helper:
def biggest(scores):
    best = 0
    for s in scores:
        if s > best:
            best = s
    return best

print(biggest([4, 9, 2]))
print(biggest([15, 3, 12]))
```
@ say
Let's practise. Imagine we asked an AI helper for a function that finds the biggest number in a list. It gave us this. Let's read it, line by line.
@ line 1 | A comment so we remember where it came from
Line one is a comment, so we remember this came from an AI helper.
@ line 2-3 | Start with best = 0
The function starts by setting best to zero.
@ line 4-6 | Bigger than best? It becomes the new best
Then it looks at each score. If a score is bigger than best, it becomes the new best.
@ line 7 | Return the winner
And it returns best.
@ line 9-10 | Two quick tests
Lines nine and ten test it with two lists.
@ predict 4 | Does it work?
It looks sensible. Will it give the right answers?
@ run | 9 and 15: looks right...
Run. Nine and fifteen. Both correct. So it works! Or does it? We only tried normal data. Let's be a proper tester.
@ edit 11 => print(biggest([-5, -2, -8]))
Let's try a list where every number is negative, like temperatures on a freezing winter week.
@ predict 5 | The biggest of -5, -2 and -8 is -2. What will it say?
The biggest of minus five, minus two and minus eight is minus two. What will the function say?
@ run | 0?! Zero isn't even in the list!
Run. Zero! Zero isn't even in the list. Because best started at zero, no negative number was ever bigger than it. The code looked perfect, passed two tests, and was still wrong.
@ edit 3 =>     best = scores[0]
The fix: start with the first item in the list, instead of zero.
@ run | Fixed: -2
Run again. Nine, fifteen, and minus two. All correct. This is exactly why we test suggested code ourselves, with tricky data, before trusting it.

## STUDY | Check for made-up things
@ snippet scores.biggest()
Sometimes an AI helper invents things that don't exist. Lists don't have a method called biggest. Python's real tool for this is the built in function max.
@ snippet max([-5, -2, -8])
If you run code with an invented method, Python gives an AttributeError. So, if a suggestion uses something you've never seen, look it up in Python's official documentation, or try it in a tiny test program first.

## STUDY | Honesty and privacy
@ point Follow your school's or club's rules about AI
Now, two important habits that have nothing to do with code. First, honesty. Follow the rules of your school or club about when AI help is allowed. If you used it, say so. Handing in AI work as your own isn't fair, and it also means you miss out on the learning.
@ point Never share personal details, passwords or private information
Second, privacy. Whatever you type into an AI helper may be stored and seen by others. Never share your full name, address, school, passwords, photos, or other people's private information. Make your examples up instead.
@ point Not sure? Ask a trusted adult first
And if you're not sure whether something is OK to share, ask a trusted adult first.

## CODE | ai_average.py
```python
# Suggested by an AI helper:
def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

print(average([2, 4, 6]))
print(average([7]))
print(average([]))
```
@ say
One more suggestion. This time it's a function that works out an average.
@ line 1 | Where it came from
Again, a comment to remind us where it came from.
@ line 2-4 | Add them up, divide by how many
It adds the numbers with sum, and divides the total by how many there are, using len.
@ line 6 | Normal data
Line six tests normal data.
@ line 7 | Boundary: just one number
Line seven tests a boundary: a list with only one number.
@ line 8 | Invalid: an empty list
And line eight tests an empty list.
@ predict 6 | What's the average of nothing at all?
What is the average of an empty list? Think about what len gives.
@ run | ZeroDivisionError!
Run. Four point zero, seven point zero, and then an error! A traceback with ZeroDivisionError. The length of an empty list is zero, and you can't divide by zero.
@ edit 4 =>     return total / max(len(numbers), 1)
Here's a neat fix in one line. Max picks the bigger of two numbers. So we divide by the length, or by one if the list is empty. We never divide by zero, and an empty list gives zero divided by one, which is zero.
@ run | Safe for every kind of data
Run. Four point zero, seven point zero, and zero point zero, with no crash. Only testing invalid data revealed this bug.

## STUDY | Common mistakes
@ table Mistake | Better habit ; pasting code you don't understand | read and explain every line first ; testing only normal data | add boundary and invalid tests ; trusting a function that doesn't exist | look it up or test it ; sharing private details | make examples up
Common mistakes with AI helpers. Pasting in code you don't understand. Only testing it with normal data. Trusting functions that might not exist. And sharing private details. Each one has a better habit next to it.

## REVISE | Quick revise
@ point AI helpers are useful, but can be confidently wrong
AI helpers are useful, but can be confidently wrong.
@ point Ask, read, test, understand
Ask, read, test and understand, every time.
@ point You're responsible for every line in your program
You're responsible for every line in your program.
@ point Be honest about AI use; keep private things private
Be honest about using AI, and keep private things private.

## PRACTICE | Fix the suggestion
@ task An AI helper suggested this:\n\ndef count_vowels(word):\n    count = 0\n    for letter in word:\n        if letter in "aeiou":\n            count += 1\n    return count\n\nprint(count_vowels("Ziggy"))\nprint(count_vowels("APPLE"))\n\nTest it, find the bug, fix it, and explain why it happened.
Your turn to be the checker. An AI helper suggested this function, which counts the vowels in a word. Type it in, test it with Ziggy and with APPLE in capitals, find the bug, fix it, and explain in one sentence why it happened.
@ hint What happens to capital letters? Remember .lower()
Hint: think about capital letters. Which string method from lesson two point three could help?
@ pause 15
Pause the video and try it.

## ANSWER | count_vowels.py
```python
def count_vowels(word):
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count += 1
    return count

print(count_vowels("Ziggy"))
print(count_vowels("APPLE"))
```
@ line 1-2
The function starts counting at zero.
@ line 3
The fix is on line three. We loop over word dot lower, so capital letters become small letters first.
@ line 4-6
Then each vowel adds one to the count, and the count is returned.
@ line 8-9
And our two tests.
@ run
Run. One vowel in Ziggy, and two in APPLE. Before the fix, APPLE gave zero, because capital A and capital E aren't in the string of small vowels. Explaining why a bug happened shows you really understand the code.

## OUTRO
Excellent! You now know how to use AI helpers like a thoughtful programmer. Next time, it's the grand finale: our final project, the Big Five Wellbeing Check-In, where we'll use everything from the whole course. Like, share and subscribe, and keep coding. Happy Learning!
