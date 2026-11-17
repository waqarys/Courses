# M2-07_True_or_False - ride_check.py
age = 7
height = 125
with_adult = True
tall_enough = height >= 120
old_enough = age >= 8 or with_adult
print("Tall enough:", tall_enough)
print("Old enough:", old_enough)
print("Can ride:", tall_enough and old_enough)
