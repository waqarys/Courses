# M2-07_True_or_False - password.py
secret = "mango42"
guess = input("Password? ")
print(guess == secret)
print(len(guess) >= 6)
print(guess == secret and len(guess) >= 6)
