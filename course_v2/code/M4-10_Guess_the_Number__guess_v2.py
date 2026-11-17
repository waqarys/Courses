# M4-10_Guess_the_Number - guess_v2.py
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
