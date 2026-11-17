# M5-06_Wellbeing_Check_In - feedback.py
def feedback(average):
    if average >= 4:
        return "You're having a great week. Keep it up!"
    elif average >= 3:
        return "A good week. Maybe give one area some extra care."
    elif average >= 2:
        return "A tricky week. Be kind to yourself."
    else:
        return "That sounds hard. Talk to someone you trust."

for test in [4.6, 4, 3.2, 2.5, 1.4]:
    print(test, "->", feedback(test))
