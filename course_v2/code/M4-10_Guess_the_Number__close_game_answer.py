# M4-10_Guess_the_Number - close_game.py
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
