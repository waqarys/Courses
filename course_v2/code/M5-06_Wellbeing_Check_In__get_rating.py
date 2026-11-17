# M5-06_Wellbeing_Check_In - get_rating.py
def get_rating(area):
    while True:
        answer = input(f"{area} (1-5): ")
        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)
        print("Please type a whole number from 1 to 5.")

rating = get_rating("Sleep")
print("You chose", rating)
