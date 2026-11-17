# M4-06_Match_Case - snack_menu.py
print("1 Apple  2 Juice  3 Sandwich")
choice = int(input("Your choice: "))
match choice:
    case 1:
        print("Apple: 2 coins")
    case 2:
        print("Juice: 3 coins")
    case 3:
        print("Sandwich: 5 coins")
    case _:
        print("Please choose 1, 2 or 3")
