---
id: "5.4"
title: "Testing Your Code"
module: 5
module_title: "Next Steps"
next: "Coding with AI, wisely"
minutes: 7.67
thumb_code: 'assert is_even(4) == True'
goals: ["Smoke tests and test plans", "Normal, boundary and invalid test data", "assert: tests that check themselves", "Using a failing test to find and fix a bug"]
youtube:
  title: "Python Lesson 5.4: Testing Your Code - Test Data and assert | Introduction to Python"
  description: |
    How do you know your program really works? Ziggy the Python explains smoke tests, test plans, and the three
    kinds of test data: normal, boundary and invalid. Then we write assert tests that check themselves, catch a
    sneaky boundary bug with a failing test, fix it, and test a rating validator.
    For beginners aged 7 to 20.
  tags: [python testing, python assert, test data, boundary testing, learn python, fun skill builders]
---

<!-- Booklet 1.8: smoke test. Test data types and assert extend it. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. A program that runs isn't always a program that works. It might give the right answer for one number, and the wrong answer for another. Today we'll learn how real programmers test their code, so they can be confident it does what it should, every time.

## STUDY | Why test?
@ point Running once with one value proves very little
If you run a program once and it looks right, that proves very little. Bugs love to hide in places you didn't try: the biggest value, the smallest value, or something strange that a user types.
@ point Smoke test: does it start and run without crashing?
The simplest test is a smoke test. You run the program quickly, to check that it starts and runs without crashing. The name comes from electronics: switch the new gadget on and check that no smoke comes out!
@ point Test plan: decide inputs AND expected results BEFORE running
A proper test needs a plan. Before running anything, you decide which inputs to try, and what the correct result should be for each. Then you run it, and compare what actually happened with what you expected.
@ point Expected ≠ actual? You've found a bug. That's good news!
If the actual result doesn't match the expected result, you've found a bug. And that's good news, because now you can fix it before anyone else finds it.

## STUDY | Three kinds of test data
@ table Kind | What it means | For a 1 to 5 rating ; normal | sensible, typical values | 2, 3, 4 ; boundary | right at the edges of what's allowed | 1 and 5 (and 0 and 6) ; invalid | values that should be rejected | 9, -1, "abc"
Good testers use three kinds of test data. Normal data is sensible and typical. Boundary data sits right at the edges, where the rules change. And invalid data is stuff that should be rejected. For a rating from one to five, normal is two, three or four. Boundary is one and five, and just outside them, zero and six. Invalid is nine, minus one, or someone typing letters.
@ point Most bugs live at the boundaries
Why bother with boundaries? Because that's where most bugs live. Remember the difference between less than, and less than or equal to? One wrong symbol, and the edge value gives the wrong answer.

## STUDY | assert: tests that check themselves
@ snippet assert is_even(4) == True
Python has a keyword for testing called assert. You write assert, then something that should be true.
@ point True → nothing happens. False → AssertionError, and the program stops
If it is true, nothing happens, and Python carries on quietly. If it's false, Python stops with an AssertionError, showing you which line failed.
@ point Tests run in a second, and you can run them after every change
The best thing about assert tests is that they check themselves. You don't have to read the output and decide if it's right. And you can run them again every time you change your code, to make sure you haven't broken anything.

## CODE | test_is_even.py
```python
def is_even(n):
    return n % 2 == 0

assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True
assert is_even(-2) == True
print("All tests passed!")
```
@ line 1-2 | The function we're testing
Lines one and two are the function we want to test. A number is even if dividing by two leaves no remainder.
@ line 4-5 | Normal data: 4 and 7
Lines four and five test normal data. Four should be even, and seven should not.
@ line 6 | Boundary: zero
Line six tests zero, a tricky edge. Zero is even!
@ line 7 | A negative number
Line seven tests a negative number.
@ line 8 | We only get here if every assert passed
And line eight only runs if every assert passed.
@ predict 4 | Will all four tests pass?
Will all four tests pass?
@ run | Silence means success
Run. All tests passed! The asserts stayed silent, because every one was true. Four tests, checked in a fraction of a second.

## CODE | test_can_ride.py
```python
def can_ride(height):
    return height > 120

assert can_ride(150) == True
assert can_ride(100) == False
assert can_ride(120) == True
print("All tests passed!")
```
@ say
Now a function with a hidden bug. The rule is: you can ride if you are one hundred and twenty centimetres tall, or taller.
@ line 1-2 | Taller than 120?
The function says the height must be greater than one hundred and twenty.
@ line 4 | Normal: 150 should be allowed
Line four: one fifty should be allowed.
@ line 5 | Normal: 100 should not
Line five: one hundred should not.
@ line 6 | Boundary: exactly 120 should be allowed
Line six is the boundary test. Exactly one hundred and twenty should be allowed.
@ line 7 | Only reached if all three pass
And line seven celebrates, but only if every test passes.
@ predict 5 | Which test will fail?
Look closely at line two. Will every test pass?
@ run | AssertionError on line 6!
Run. An error! The traceback points at line six, with an AssertionError. The normal tests passed, but the boundary test failed. Someone exactly one hundred and twenty centimetres tall was turned away, even though the rule says they can ride.
@ edit 2 =>     return height >= 120
The fix is one symbol. Greater than or equal to.
@ run | Fixed and proven
Run again. All tests passed! Without that boundary test, this bug could have hidden for a long time. And notice we didn't just fix the code. The test proves it's fixed, and will catch it if the bug ever comes back.

## CODE | valid_rating.py
```python
def is_valid_rating(text):
    if not text.isdigit():
        return False
    number = int(text)
    return 1 <= number <= 5

tests = ["3", "1", "5", "0", "6", "9", "abc", ""]
for t in tests:
    print(f"{t!r:6} -> {is_valid_rating(t)}")
```
@ say
Invalid data matters too. Let's test a function that checks whether someone typed a valid rating from one to five. We'll need this in our final project.
@ line 1-3 | Not all digits? Reject it
First, if the text isn't made only of digits, we reject it straight away. The string method is digit checks that. This stops letters from crashing int.
@ line 4-5 | Is it between 1 and 5?
Then we convert it, and check it's from one to five, using a chained comparison.
@ line 7 | Normal, boundary and invalid data
Line seven is our test plan: normal, boundary, and invalid values, including an empty answer.
@ line 8-9 | Show each test and its result
The loop prints each test value and its result. The exclamation mark r shows the quotes around each value, so we can see the empty one.
@ predict 6 | Which ones are True?
Before we run it: which of these should be valid?
@ run | Only 3, 1 and 5 are valid
Run. Three, one and five are True. Zero and six, just outside the edges, are False. Nine is False. Letters and an empty answer are False, and nothing crashed. Every kind of test data gave the result we expected.

## STUDY | A tester's habits
@ point Test as you go, not only at the end
Test as you go. Write a few lines, then test them. It's much easier to find a bug in five new lines than in five hundred.
@ point Ask someone else to try to break it
Ask a friend to try to break your program. Other people type things you'd never think of.
@ point Keep your tests and run them after every change
Keep your tests, and run them again after every change.

## STUDY | Common mistakes
@ table Mistake | What happens ; only testing normal data | boundary bugs slip through ; no expected result written down | you can't tell if the output is right ; assert x = 5 | SyntaxError: use == ; deleting a failing test | the bug is still there!
Common testing mistakes. Only testing normal data, so boundary bugs slip through. Not writing down the expected result first. Writing a single equals in an assert, instead of double equals. And deleting a failing test, instead of fixing the bug it found.

## REVISE | Quick revise
@ point Smoke test: does it run at all?
A smoke test checks the program runs at all.
@ point Test plan: inputs + expected results, decided first
A test plan lists inputs and expected results, decided before you run.
@ point Normal, boundary and invalid data
Use normal, boundary and invalid data.
@ point assert stays silent when True, stops with AssertionError when False
Assert stays silent when true, and stops with an AssertionError when false.

## PRACTICE | Test area()
@ task def area(width, height):\n    return width * height\n\nWrite 3 asserts for area(): a normal case, a case with 0, and a case with 1.\nThen print "area() passed!"
Your turn. Copy this area function, and write three assert tests for it: one normal case, one where a side is zero, and one where a side is one. Work out each expected answer first. Then print area passed.
@ hint assert area(4, 3) == 12
Hint: the first one could be: assert area of four and three equals twelve.
@ pause 15
Pause the video and try it.

## ANSWER | test_area.py
```python
def area(width, height):
    return width * height

assert area(4, 3) == 12
assert area(0, 7) == 0
assert area(1, 9) == 9
print("area() passed!")
```
@ line 1-2
The function.
@ line 4-6
A normal case, a zero case, and a one case.
@ line 7
And a message that only appears if all three pass.
@ run
Run. Area passed! Your numbers can be different, as long as your expected answers are correct. If one of your tests failed, check your maths before blaming the function!

## OUTRO
Brilliant work! You now test like a professional programmer. Next time, we'll talk about AI coding helpers: how they can help you learn, and why you must always check their work. Like, share and subscribe, and keep coding. Happy Learning!
