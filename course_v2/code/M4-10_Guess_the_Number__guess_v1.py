# M4-10_Guess_the_Number - guess_v1.py
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
