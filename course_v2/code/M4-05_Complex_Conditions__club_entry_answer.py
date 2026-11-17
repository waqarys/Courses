# M4-05_Complex_Conditions - club_entry.py
age = int(input("Age: "))
has_card = input("Club card? (y/n) ") == "y"
has_note = input("Teacher's note? (y/n) ") == "y"
right_age = 9 <= age <= 16
if (right_age and has_card) or has_note:
    print("Welcome!")
else:
    print("Sorry")
