# M4-06_Match_Case - commands.py
command = input("Command: ").strip().lower()
match command:
    case "north" | "n":
        print("You walk north into the forest.")
    case "south" | "s":
        print("You walk south to the river.")
    case "look":
        print("Tall trees all around. A path leads north.")
    case "quit":
        print("Goodbye, adventurer!")
    case _:
        print(f"I don't understand '{command}'.")
