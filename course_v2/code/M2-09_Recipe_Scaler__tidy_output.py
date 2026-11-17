# M2-09_Recipe_Scaler - tidy_output.py
RECIPE_SERVES = 4
milk_cups = 1.5
people = 5
scale = people / RECIPE_SERVES
milk = milk_cups * scale
print(f"Milk: {milk} cups")
print(f"Milk: {round(milk, 1)} cups")
print(f"Scale used: {scale}")
