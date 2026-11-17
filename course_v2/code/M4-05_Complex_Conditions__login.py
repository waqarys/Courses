# M4-05_Complex_Conditions - login.py
USERNAME = "ziggy"
PASSWORD = "hiss123"
name = input("Username: ")
if name == USERNAME:
    secret = input("Password: ")
    if secret == PASSWORD:
        print("Welcome back, Ziggy!")
    else:
        print("Wrong password.")
else:
    print("Username not found.")
