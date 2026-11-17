# M4-10_Guess_the_Number - guess_final.py
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
