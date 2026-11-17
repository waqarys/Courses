# M4-06_Match_Case - day_name.py
day = int(input("Day number (1-7): "))
match day:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case 4:
        name = "Thursday"
    case 5:
        name = "Friday"
    case 6 | 7:
        name = "the weekend!"
    case _:
        name = "not a real day"
print(f"Day {day} is {name}")
