# M5-03_Modules - compliments.py
import random

adjectives = ["awesome", "brilliant", "super", "fantastic"]
nouns = ["coder", "thinker", "builder", "explorer"]

for i in range(2):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    print(f"You are a {adj} {noun}!")
