---
id: "4.10"
title: "Mini-Project: Guess the Number"
module: 4
module_title: "Making Decisions and Loops"
next: "Functions: Your Own Commands"
minutes: 8.58
thumb_code: 'secret = random.randint(1, 100)'
goals: ["Random numbers with the random module", "A game loop with if / elif / else", "Counting guesses and setting a limit", "Validating every guess"]
youtube:
  title: "Python Lesson 4.10: Mini-Project - Guess the Number Game | Introduction to Python"
  description: |
    Module 4 project! Ziggy the Python builds the classic Guess the Number game step by step: a random secret
    number, too high / too low hints with if, elif and else, a while loop that counts guesses, input validation,
    and a guess limit. We play it on screen and test the edge cases like real game developers.
    For beginners aged 7 to 20.
  tags: [guess the number python, python game for beginners, python random, python project, learn python, fun skill builders]
---

<!-- Booklet chapter 4 case study: Guess the Number. Random numbers are seeded (@ seed) so the video is repeatable. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. It's game time! Today's project is a classic that programmers have been building for over fifty years: Guess the Number. The computer picks a secret number, and you try to guess it, with hints after each guess. It uses random numbers, decisions, loops, counters and validation. Everything from Module Four, in one game.

## STUDY | How the game works
@ flow Pick a secret number > Ask for a guess > Too high, too low, or correct? > Repeat until correct
Here's the plan. The computer picks a secret number from one to a hundred. The player guesses. The computer says too high, too low, or correct. If it's not correct, the player guesses again. When they get it, the game says how many guesses it took.
@ point Which building blocks?
Let's match the plan to our building blocks. Repeat until correct is iteration: a while loop. Too high, too low or correct is selection: if, elif and else. And the whole thing runs in sequence: set up, play, finish.
@ point Build it in stages, testing each one
As always, we'll build it in stages. Stage one: pick a number and check one guess. Stage two: keep guessing in a loop. Stage three: validation and a guess limit.

## STUDY | Random numbers
@ snippet import random\nsecret = random.randint(1, 100)
To pick a secret number, we need randomness. Python has a module called random, which is a toolbox of extra functions. Import random, at the top of the program, opens the toolbox. We'll learn much more about modules in lesson five point three.
@ point random.randint(1, 100): a whole number from 1 to 100
Random dot randint gives a random whole number between two values. And unlike range, both ends are included, so one hundred can be picked.
@ point Every run picks a different number
Every time the program runs, it picks a different number. That's what makes the game replayable.
@ point In this video, the random numbers are fixed so you can follow along
In this video, we've fixed the random numbers behind the scenes, so the game plays the same way every time we run it. On your computer, the secret number will be different every time.

## CODE | guess_v1.py
```python
import random
secret = random.randint(1, 100)
guess = int(input("Guess a number from 1 to 100: "))
if guess < secret:
    print("Too low!")
elif guess > secret:
    print("Too high!")
else:
    print("Correct!")
print("The secret number was", secret)
```
@ seed 12
@ input 50
@ line 1 | Open the random toolbox
Stage one. Line one imports the random module.
@ line 2 | Pick the secret number
Line two picks the secret number from one to a hundred.
@ line 3 | One guess, as a number
Line three asks for one guess, converted to a number.
@ line 4-5 | Lower than the secret?
If the guess is lower than the secret, too low.
@ line 6-7 | Higher?
If it's higher, too high.
@ line 8-9 | Otherwise it must be equal
Otherwise, it must be equal, so it's correct. We don't need to check that with double equals, because there's no other possibility left.
@ line 10 | For testing: reveal the secret
And for testing, line ten reveals the secret. We'll remove this from the finished game!
@ predict 4 | Guess 50. What hint will we get?
I'll guess fifty, the middle. What will happen?
@ run | 50 is too low (the secret was 61)
Run. Too low! The secret number was sixty one. The checking works. But one guess isn't much of a game.

## CODE | guess_v2.py
```python
import random
secret = random.randint(1, 100)
guesses = 0
guess = 0
while guess != secret:
    guess = int(input("Your guess: "))
    guesses += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print(f"Correct! You got it in {guesses} guesses.")
```
@ seed 12
@ input 50 | 75 | 60 | 65 | 62 | 61
@ say
Stage two: a loop, so the player can keep guessing, and a counter for the guesses.
@ line 1-2 | The same secret
The same import and secret number.
@ line 3 | Count the guesses
Line three starts a guess counter at zero.
@ line 4 | A starting guess that can't be right
Line four gives guess a starting value of zero. The secret is never zero, so the loop is sure to run at least once.
@ line 5 | Keep going until the guess is right
The loop keeps going while the guess is not the secret.
@ line 6-7 | Ask, and count
Inside, ask for a guess, and count it.
@ line 8-11 | Hints: too low or too high
Then the hints. We don't need an else here, because when the guess is correct, the loop will end.
@ line 12 | After the loop: success!
After the loop, the player must have got it, so we celebrate.
@ predict 6 | Halving strategy: 50, 75, 60, 65, 62... How many guesses?
I'll play using a smart strategy: always guess between the hints. Watch how quickly it closes in.
@ run | Found 61 in 6 guesses
Run. Fifty, too low. Seventy five, too high. Sixty, too low. Sixty five, too high. Sixty two, too high. Sixty one: correct, in six guesses! Each hint cut the possible numbers roughly in half. That's the halving trick from lesson four point seven, and it means a good player never needs more than seven guesses.

## CODE | guess_final.py
```python
import random
MAX_GUESSES = 7
secret = random.randint(1, 100)
guesses = 0
print(f"I'm thinking of a number from 1 to 100. You have {MAX_GUESSES} guesses.")
while guesses < MAX_GUESSES:
    text = input("Your guess: ")
    if not text.isdigit():
        print("Please type a whole number.")
        continue
    guess = int(text)
    guesses += 1
    if guess == secret:
        print(f"Correct! You won in {guesses} guesses.")
        break
    elif guess < secret:
        print("Too low!", MAX_GUESSES - guesses, "left")
    else:
        print("Too high!", MAX_GUESSES - guesses, "left")
if guess != secret:
    print("Out of guesses! It was", secret)
```
@ seed 12
@ input 50 | sixty | 70 | 60 | 61
@ say
Stage three: the finished game. We'll add a limit of seven guesses, and validation, so typing a word doesn't crash it.
@ line 1-2 | A constant for the guess limit
Import random, and a constant for the guess limit, seven.
@ line 3-4 | The secret and the counter
The secret number, and the guess counter.
@ line 5 | Explain the rules
Line five explains the rules to the player.
@ line 6 | Loop while there are guesses left
This time the loop runs while the player still has guesses left.
@ line 7 | Get the guess as text
Line seven gets the guess as text.
@ line 8-10 | Validate: not digits? Ask again, without counting it
If it isn't a whole number, we ask again with continue. Notice that this happens before the counter, so a typo doesn't use up a guess. That's being fair to the player.
@ line 11-12 | Convert and count
Now it's safe to convert, and we count the guess.
@ line 13-15 | Correct: celebrate and break
If it's correct, celebrate, and break out of the loop.
@ line 16-19 | Hints, plus guesses left
Otherwise, too low or too high, with the number of guesses left.
@ line 20-21 | After the loop: did they run out?
After the loop, if the last guess wasn't the secret, the player ran out of guesses, so we reveal the number.
@ predict 6 | 50, "sixty", 70, 60, 61: win or lose?
I'll guess fifty, then accidentally type sixty as a word, then seventy, sixty, and sixty one. Will I win, and in how many guesses?
@ run | The word was rejected without using a guess; won in 4
Run. Fifty: too low, six left. Sixty as a word: please type a whole number, and it didn't use up a guess. Seventy: too high, five left. Sixty: too low, four left. Sixty one: correct! You won in four guesses. The validation, the limit and the hints all worked together.

## STUDY | Testing the game
@ table Test | Why ; guess the secret first time | the break and the message ; use all 7 guesses wrongly | the "out of guesses" ending ; type a word, a negative, a blank | validation ; guess 1 and 100 | the edges of the range
Game developers test every path through their code. Let's list the tests for our game. Guess correctly on the first try, to check the winning message. Use all seven guesses wrongly, to check the losing message. Type a word, a negative number and nothing at all, to check the validation. And guess one and a hundred, the edges of the range. Testing every path like this is how bugs get caught before players find them.
@ point Remove the "reveal the secret" line before sharing!
And remember, remove any testing lines that reveal the secret before you share your game!

## STUDY | Make it your own
@ point Difficulty levels: 1-10, 1-100 or 1-1000
Here are some ideas to extend your game. Add difficulty levels: easy is one to ten, medium is one to a hundred, and hard is one to a thousand. Use match and case to set the range.
@ point "Getting warmer": within 5 of the secret
Add a getting warmer message when the guess is within five of the secret.
@ point Play again? Wrap the game in while True
And wrap the whole game in another while True loop, asking play again, yes or no, at the end.

## REVISE | Quick revise
@ point import random; random.randint(a, b) includes both ends
Import random, and randint picks a whole number, including both ends.
@ point while loop + if/elif/else = a game loop
A while loop with if, elif and else makes a game loop.
@ point Count guesses; break on a win; a constant for the limit
Count the guesses, break when the player wins, and use a constant for the limit.
@ point Validate before converting; test every path
Validate before converting, and test every path through the game.

## PRACTICE | Your version
@ task Change the game so that:\n1. The number is from 1 to 20 and the player gets 5 guesses\n2. It says "Very close!" when the guess is within 2 of the secret\n3. Bonus: ask "Play again? (y/n)" at the end
Your turn. Change the game so the secret number is from one to twenty, and the player gets five guesses. Add a very close message when a guess is within two of the secret. And for a bonus, ask play again at the end, and start a new game if they type y.
@ hint abs(guess - secret) <= 2 checks "within 2" (abs removes the minus sign)
Hint: the abs function gives the distance between two numbers without a minus sign. If abs of guess minus secret is two or less, it's very close.
@ pause 20
Pause the video and make the game your own.

## ANSWER | close_game.py
```python
import random
secret = random.randint(1, 20)
for turn in range(5):
    guess = int(input("Guess 1-20: "))
    if guess == secret:
        print("Correct!")
        break
    if abs(guess - secret) <= 2:
        print("Very close!")
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
print("The number was", secret)
```
@ seed 12
@ input 10 | 14 | 18 | 16
@ line 1-2
A secret from one to twenty.
@ line 3-4
This time, a for loop gives exactly five turns.
@ line 5-7
A correct guess breaks out.
@ line 8-9
Within two of the secret: very close.
@ line 10-13
Otherwise, too low or too high.
@ line 14
And reveal the number at the end.
@ run
Run. Ten: too low. Fourteen: very close! Eighteen: very close again, so it must be in between. Sixteen: correct! The number was sixteen. Your version might look different, especially if you added play again. If it works and it's fun, it's a great answer.

## OUTRO
Congratulations, you've finished Module Four and built a real game! Your programs can now make decisions and repeat things. Next time, Module Five begins with functions: your very own commands. Like, share and subscribe, and keep coding. Happy Learning!
