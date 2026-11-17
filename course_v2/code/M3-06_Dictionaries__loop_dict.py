# M3-06_Dictionaries - loop_dict.py
ages = {"Asha": 11, "Leo": 14, "Mia": 9}
for name in ages:
    print(name, "is", ages[name])
for name, age in ages.items():
    print(f"{name} will be {age + 1} next year")
print(list(ages.keys()))
print(list(ages.values()))
