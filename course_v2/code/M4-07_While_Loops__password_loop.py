# M4-07_While_Loops - password_loop.py
SECRET = "mango"
guess = input("Password: ")
tries = 1
while guess != SECRET:
    print("Wrong, try again.")
    guess = input("Password: ")
    tries = tries + 1
print(f"Welcome! You got in after {tries} tries.")
