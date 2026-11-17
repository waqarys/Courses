# M2-09_Recipe_Scaler - recipe_scaler.py
# Pancake recipe scaler
RECIPE_SERVES = 4
flour_cups = 2.0
milk_cups = 1.5
eggs = 2

people = int(input("How many people are eating? "))
scale = people / RECIPE_SERVES

print(f"Pancakes for {people}:")
print(f"Flour: {flour_cups * scale} cups")
print(f"Milk:  {milk_cups * scale} cups")
print(f"Eggs:  {round(eggs * scale)}")
