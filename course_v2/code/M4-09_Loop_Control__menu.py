# M4-09_Loop_Control - menu.py
while True:
    print("1) Say hello  2) Tell a joke  q) Quit")
    choice = input("Choose: ").lower()
    if choice == "q":
        print("Bye!")
        break
    elif choice == "1":
        print("Hello there!")
    elif choice == "2":
        print("Why did the snake learn Python? To get ahead!")
    else:
        print("Please choose 1, 2 or q.")
