# M5-06_Wellbeing_Check_In - my_checkin.py
AREAS = ["Sleep", "Food", "Movement", "Friends", "Feelings", "Fun"]

def get_rating(area):
    while True:
        answer = input(f"{area} (1-5): ")
        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)
        print("Please type a whole number from 1 to 5.")

def weekly_average(days):
    return sum(days) / len(days)

ratings = {}
for area in AREAS:
    ratings[area] = get_rating(area)
total = sum(ratings.values())
print(f"Total: {total} out of {len(AREAS) * 5}")
print("Average:", round(total / len(ratings), 1))

week = [3.6, 4.0, 2.8, 3.4, 4.2, 4.4, 3.9]
print("Weekly average:", round(weekly_average(week), 1))
