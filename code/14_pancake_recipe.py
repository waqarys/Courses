# Lesson 14 — scale a 4-serve pancake recipe
STANDARD_SERVINGS = 4

flour_cups = 2.5
sugar_tablespoons = 3
eggs_count = 2
milk_liters = 0.5
is_vegetarian = True
topping = "banana"

desired_servings = 6
# desired_servings = int(input("How many servings? "))
scaling_factor = desired_servings / STANDARD_SERVINGS

print("New recipe amounts")
print("Flour:", flour_cups * scaling_factor, "cups")
print("Sugar:", sugar_tablespoons * scaling_factor, "tablespoons")
print("Eggs:", eggs_count * scaling_factor)
print("Milk:", milk_liters * scaling_factor, "liters")
print("Vegetarian:", is_vegetarian)
print("Topping:", topping)
