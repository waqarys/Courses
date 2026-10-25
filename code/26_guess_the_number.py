# Lesson 26 — capstone. Run this and type guesses.
import random

ATTEMPT_LIMIT = 7
answer = random.randint(1, 100)
attempt = 0
won = False

print("Welcome to Guess the Number")

while attempt < ATTEMPT_LIMIT and not won:
    print("Attempt", attempt + 1, "of", ATTEMPT_LIMIT)
    text = input("Your guess (1-100): ")

    if not text.isnumeric():
        print("Type a whole number.")
        continue

    guess = int(text)
    if guess < 1 or guess > 100:
        print("Stay between 1 and 100.")
        continue

    attempt = attempt + 1

    if guess == answer:
        won = True
        print("You got it in", attempt, "tries.")
    elif guess < answer:
        print("Too low")
    else:
        print("Too high")

if not won:
    print("Out of tries. It was", answer)
