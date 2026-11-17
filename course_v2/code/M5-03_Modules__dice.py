# M5-03_Modules - dice.py
import random

print("Rolling five dice...")
for i in range(5):
    roll = random.randint(1, 6)
    print(f"Dice {i + 1}: {roll}")
