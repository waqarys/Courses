# Lesson 23 — a question inside a question, then match
has_key = True
has_weapon = True
has_enemy = True

if has_key:
    if has_weapon:
        if has_enemy:
            print("Fight to enter")
        else:
            print("Safe to enter")
    else:
        print("Need a weapon first")
else:
    print("Find the key")

player_action = "JUMP"
match player_action:
    case "JUMP":
        print("Player jumped")
    case "RUN":
        print("Player is running")
    case "ATTACK":
        print("Player attacked")
    case _:
        print("Unknown action")
