# Lesson 24 — repeat while something is still true
resources = 5
while resources > 0:
    print("Working...", resources)
    resources = resources - 1
print("Done")

calculation = 0
while calculation < 10:
    calculation = calculation + 1
    if calculation == 4:
        print("Stopped early")
        break
print("After the loop", calculation)

from random import randint

player_health = 100
while player_health > 0:
    damage = randint(10, 20)
    player_health = player_health - damage
    print("Health:", player_health)
print("Game over")
