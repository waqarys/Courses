---
id: "5.2"
title: "Parameters and return"
module: 5
module_title: "Next Steps"
next: "Python's Toolbox: Modules"
minutes: 8.47
thumb_code: 'def area(width, height):'
goals: ["Parameters: information going in", "Parameters vs arguments", "return: an answer coming out", "return vs print"]
youtube:
  title: "Python Lesson 5.2: Function Parameters and return Values | Introduction to Python"
  description: |
    Make functions that take information in and give answers back. Ziggy the Python explains parameters and
    arguments with ingredients and a dish, return values, and the big difference between return and print. We
    build greeting, area and temperature-converter functions, use default values, and fix the mistakes everyone makes.
    For beginners aged 7 to 20.
  tags: [python parameters, python return, function arguments python, return vs print, learn python, fun skill builders]
---

<!-- Beyond the booklet: functions with parameters and return values. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. Last time, our functions did exactly the same thing every time. Today we'll make them flexible. We'll pass information into a function, so it can work with different values, and we'll get answers back out of it. This is where functions become truly powerful.

## STUDY | Ingredients in, dish out
@ flow Ingredients go in (parameters) > The function does its job > A dish comes out (return value)
Think of a function as a kitchen. Ingredients go in. The kitchen does its work. And a finished dish comes out. In Python, the ingredients are called parameters, and the dish is called the return value.
@ snippet def greet(name):\n    print(f"Hello, {name}!")
A parameter is a variable listed inside the round brackets when you define a function. Here, name is a parameter. Inside the function, it works just like a normal variable.
@ snippet greet("Asha")\ngreet("Leo")
When you call the function, you put a value in the brackets. That value is called an argument. Python puts the argument into the parameter, and then runs the body.
@ point Parameter = the empty box. Argument = what you put in it
Here's an easy way to remember the difference. The parameter is the empty labelled box in the definition. The argument is the actual value you put into the box when you call it.
@ point Several parameters are separated by commas, in order
A function can have several parameters, separated by commas. The arguments are matched to the parameters in the same order.

## CODE | greet.py
```python
def greet(name, times):
    for i in range(times):
        print(f"Hello, {name}!")

greet("Asha", 2)
greet("Leo", 1)
greet("Ziggy", 3)
```
@ line 1 | Two parameters: name and times
Line one defines greet with two parameters: name and times.
@ line 2-3 | Use the parameters like variables
Inside, a loop uses times to decide how often to repeat, and name in the greeting.
@ line 5 | Arguments: "Asha" → name, 2 → times
Line five calls it with two arguments. Asha goes into name, and two goes into times.
@ line 6-7 | Different arguments, different results
Two more calls, with different arguments.
@ predict 5 | How many hellos for each person?
How many hellos will each person get?
@ run | One function, three different results
Run. Hello Asha twice. Hello Leo once. Hello Ziggy three times. One function, and three different results, because each call gave it different ingredients.

## STUDY | return: getting an answer back
@ snippet def area(width, height):\n    return width * height
Sometimes we don't want a function to print something. We want it to work out an answer and hand it back to us, so we can use it. That's what return does.
@ point return sends a value back to where the function was called
Return sends a value back to the line that called the function. The call is replaced by that value, just like len of a word is replaced by a number.
@ snippet room = area(4, 3)
So we can store the result in a variable, use it in a calculation, or pass it to another function.
@ point return also ENDS the function immediately
Return also ends the function straight away. Any lines after it inside the function are skipped.
@ point print shows a value. return hands it back.
Here's the big difference. Print shows a value on the screen for a human to read, but the program can't use it afterwards. Return hands the value back to the program, so it can keep working with it.

## CODE | area.py
```python
def area(width, height):
    return width * height

room = area(4, 3)
print("Room:", room, "square metres")
garden = area(10, 6)
print("Garden:", garden)
print("Total:", room + garden)
print("A 5 by 5 square:", area(5, 5))
```
@ line 1-2 | Work out the answer, hand it back
The area function multiplies width by height, and returns the answer.
@ line 4 | The call becomes the answer: room = 12
Line four calls area with four and three. The call is replaced by the returned value, which is stored in room.
@ line 5 | Use the stored answer
Line five prints it.
@ line 6-7 | Another call, another answer
Lines six and seven work out the garden's area.
@ line 8 | Returned values can be used in maths
Line eight adds the two answers together. That's only possible because the function returned them.
@ line 9 | A call inside print
And line nine puts a call right inside print.
@ predict 6 | Room, garden, total and the square?
Work out all four numbers before we run it.
@ run | 12, 60, 72, 25
Run. Room: twelve square metres. Garden: sixty. Total: seventy two. And a five by five square is twenty five. The function did the maths, and the main program decided what to do with each answer.

## CODE | print_vs_return.py
```python
def double_print(n):
    print(n * 2)

def double_return(n):
    return n * 2

a = double_print(5)
b = double_return(5)
print("a is", a)
print("b is", b)
```
@ say
Let's see the difference between print and return with our own eyes. This catches out almost everyone at first.
@ line 1-2 | Version 1 PRINTS the answer
The first version prints double the number.
@ line 4-5 | Version 2 RETURNS the answer
The second version returns double the number.
@ line 7-8 | Store the result of each
Lines seven and eight call both, and store the results in a and b.
@ line 9-10 | What did we actually get back?
Then we print what's in a and b.
@ predict 6 | What will a and b be?
Here's the puzzle. What will a and b hold?
@ run | a is None: print gives nothing back
Run. First, ten appears, printed by double print when it was called. Then: a is None! b is ten. Double print showed ten on the screen, but it didn't hand anything back, so a got None, which means nothing. Double return handed ten back, so b got it. If you need to use the answer later, return it.

## CODE | converter.py
```python
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def describe(celsius):
    f = c_to_f(celsius)
    if celsius >= 30:
        feel = "hot"
    elif celsius >= 15:
        feel = "mild"
    else:
        feel = "cold"
    return f"{celsius}°C is {f}°F and feels {feel}"

for temp in [0, 20, 35]:
    print(describe(temp))
```
@ say
Let's build something useful: a temperature converter, with one function using another.
@ line 1-2 | The formula: × 9 ÷ 5 + 32
The first function converts Celsius to Fahrenheit, using the formula: times nine, divide by five, add thirty two.
@ line 4-5 | describe() calls c_to_f()
The second function, describe, starts by calling the first one, and stores the result in f.
@ line 6-11 | Decide how it feels
Then it decides how the temperature feels, using a ladder.
@ line 12 | Return a whole sentence
And it returns a complete sentence, as an F string.
@ line 14-15 | Describe three temperatures
The main program loops over three temperatures, and prints each description.
@ predict 6 | 0°C, 20°C, 35°C in Fahrenheit?
Do you know what zero degrees Celsius is in Fahrenheit? It's the freezing point of water.
@ run | 32°F, 68°F, 95°F
Run. Zero degrees is thirty two point zero Fahrenheit, and cold. Twenty is sixty eight, and mild. Thirty five is ninety five, and hot. Small functions, each doing one clear job, combined to make something bigger.

## STUDY | Default values
@ snippet def greet(name, greeting="Hello"):\n    print(f"{greeting}, {name}!")
A parameter can have a default value, written with an equals sign in the definition. If the caller doesn't give that argument, the default is used.
@ point greet("Asha") → Hello, Asha!   greet("Leo", "Hi") → Hi, Leo!
So greet Asha uses the default, hello. And greet Leo, Hi, uses Hi instead. Many of Python's own functions work like this. Round has a default of zero decimal places, and print has a default end of a new line, which we changed with end equals, way back in lesson one point two.
@ point Variables made inside a function stay inside it
One more thing to know: variables created inside a function only exist inside that function. When the function finishes, they disappear. That keeps functions tidy and independent. If the main program needs a value, the function should return it.

## STUDY | Common mistakes
@ table Mistake | What happens ; area(4) when it needs 2 arguments | TypeError: missing an argument ; printing instead of returning | the caller gets None ; code after return | never runs ; using a function's variable outside it | NameError
Common mistakes. Calling a function with the wrong number of arguments gives a TypeError. Printing instead of returning means the caller gets None. Code after a return inside the function never runs. And variables made inside a function can't be used outside it.

## REVISE | Quick revise
@ point Parameters are the inputs listed in def name(a, b):
Parameters are the inputs listed in the function definition.
@ point Arguments are the values you pass when calling
Arguments are the values you pass in when you call it.
@ point return hands a value back and ends the function
Return hands a value back, and ends the function.
@ point print shows; return gives back for later use
Print shows a value. Return gives it back for the program to use.

## PRACTICE | Converter
@ task Write a function f_to_c(fahrenheit) that RETURNS the temperature in Celsius: (F - 32) × 5 ÷ 9.\nUse it to print 212°F and 98.6°F in Celsius, rounded to 1 decimal place.
Your turn. Write a function called f to c, which takes a temperature in Fahrenheit and returns it in Celsius. The formula is: subtract thirty two, then multiply by five, then divide by nine. Use it to convert two hundred and twelve, and ninety eight point six, and print the answers rounded to one decimal place.
@ hint return (fahrenheit - 32) * 5 / 9 — the brackets matter!
Hint: put brackets around fahrenheit minus thirty two, so the subtraction happens first.
@ pause 15
Pause the video and try it.

## ANSWER | f_to_c.py
```python
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(round(f_to_c(212), 1))
print(round(f_to_c(98.6), 1))
```
@ line 1-2
The function returns the converted temperature. The brackets make the subtraction happen first.
@ line 4-5
Then two calls, each rounded to one decimal place.
@ run
Run. One hundred point zero, the boiling point of water. And thirty seven point zero, a normal body temperature. Because the function returns its answer, we could round it afterwards. Excellent!

## OUTRO
Superb! Your functions can now take inputs and give back answers, just like Python's own. Next time, we'll open Python's toolbox of modules, with random numbers, maths functions and dates. Like, share and subscribe, and keep coding. Happy Learning!
