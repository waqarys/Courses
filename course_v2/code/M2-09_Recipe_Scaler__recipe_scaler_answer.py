# M2-09_Recipe_Scaler - recipe_scaler.py
RECIPE_SERVES = 4
sugar_spoons = 3
people = int(input("How many people are eating? "))
scale = people / RECIPE_SERVES
print(f"Sugar: {round(sugar_spoons * scale)} spoons")
