# M2-06_Maths - pizza_party.py
PEOPLE = 13
SLICES_EACH = 3
SLICES_PER_PIZZA = 8
slices = PEOPLE * SLICES_EACH
print("Slices needed:", slices)
print("Full pizzas:", slices // SLICES_PER_PIZZA)
print("Extra slices:", slices % SLICES_PER_PIZZA)
pizzas = (slices + SLICES_PER_PIZZA - 1) // SLICES_PER_PIZZA
print("Pizzas to order:", pizzas)
