# M5-03_Modules - birthday.py
from datetime import date

today = date(2026, 11, 17)
print("Today is", today)
print("The year is", today.year)
print("It's a", today.strftime("%A"))

birthday = date(2027, 3, 8)
days_left = (birthday - today).days
print(f"Only {days_left} days until my birthday!")
