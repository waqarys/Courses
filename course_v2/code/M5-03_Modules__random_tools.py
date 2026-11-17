# M5-03_Modules - random_tools.py
import random

colours = ["red", "green", "blue", "purple"]
print("Random colour:", random.choice(colours))

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print("Shuffled:", cards)

print("Random decimal:", round(random.random(), 2))
