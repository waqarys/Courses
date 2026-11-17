# M4-05_Complex_Conditions - ride_rules.py
age = int(input("Age: "))
height = int(input("Height in cm: "))
with_adult = input("With an adult? (y/n) ") == "y"
old_enough = age >= 8 or with_adult
tall_enough = height >= 120
if old_enough and tall_enough:
    print("Enjoy the ride!")
else:
    print("Sorry, not this time.")
