# M4-09_Loop_Control - validate.py
while True:
    text = input("Pick a number from 1 to 10: ")
    if not text.isdigit():
        print("That's not a whole number.")
        continue
    number = int(text)
    if 1 <= number <= 10:
        break
    print("That's outside 1 to 10.")
print("Thanks! You chose", number)
