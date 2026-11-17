# M5-06_Wellbeing_Check_In - wellbeing_checkin.py
AREAS = ["Sleep", "Food", "Movement", "Friends", "Feelings"]

def get_rating(area):
    while True:
        answer = input(f"{area} (1-5): ")
        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)
        print("Please type a whole number from 1 to 5.")

def feedback(average):
    if average >= 4:
        return "You're having a great week. Keep it up!"
    elif average >= 3:
        return "A good week. Maybe give one area some extra care."
    elif average >= 2:
        return "A tricky week. Be kind to yourself."
    else:
        return "That sounds hard. Talk to someone you trust."

print("=== Big Five Wellbeing Check-In ===")
ratings = {}
for area in AREAS:
    ratings[area] = get_rating(area)

total = sum(ratings.values())
average = total / len(ratings)

lowest = AREAS[0]
for area in AREAS:
    if ratings[area] < ratings[lowest]:
        lowest = area

for area, score in ratings.items():
    print(area, "*" * score)
print(f"Total: {total} out of 25")
print("Average:", round(average, 1))
print(feedback(average))
print("Area to give extra care:", lowest)
