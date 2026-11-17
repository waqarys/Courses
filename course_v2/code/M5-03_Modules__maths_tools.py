# M5-03_Modules - maths_tools.py
import math

print("Square root of 81:", math.sqrt(81))
print("Pi:", round(math.pi, 2))

radius = 5
area = math.pi * radius ** 2
print("Circle area:", round(area, 1))

people = 22
seats_per_bus = 10
print("Buses needed:", math.ceil(people / seats_per_bus))
