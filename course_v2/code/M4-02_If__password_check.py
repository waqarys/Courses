# M4-02_If - password_check.py
password = input("Choose a password: ")
if len(password) < 8:
    print("Too short! Use at least 8 characters.")
if password.lower() == "password":
    print("That's far too easy to guess!")
if " " in password:
    print("Please don't use spaces.")
print("Checked:", len(password), "characters")
