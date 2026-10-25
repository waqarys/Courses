# Lesson 20 — a record, a tuple, a set, and a task list
from dataclasses import dataclass


@dataclass
class Character:
    name: str
    level: int
    health: int


player1 = Character("Archer", 5, 100)
print(player1)
print(player1.name)
player1.health = 80
print(player1.health)

position = (10, 20)
x, y = position
print(x, y)

found = {"key", "coin", "key"}
print(found)
found.add("map")
print("coin" in found)

tasks = [["wake up", 10], ["breakfast", 15], ["code", 45]]
total = 0
for task in tasks:
    print(task[0], task[1], "min")
    total = total + task[1]
print("Total:", total)
