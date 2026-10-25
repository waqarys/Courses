# Lesson 22 — if, else, elif
player_health = 100
if player_health > 0:
    print("Player is alive")

player_stamina = 0
if player_stamina > 0:
    print("You can sprint")
else:
    print("Too tired to run")

power_level = 75
if power_level >= 80:
    print("Super powerful")
elif power_level >= 50:
    print("Doing well")
elif power_level >= 20:
    print("Need more power")
else:
    print("Power depleted")

has_key = True
knows_code = False
locked_by_magic = False
inventory_space = 5
required_space = 3
can_unlock = (
    (has_key or knows_code)
    and not locked_by_magic
    and inventory_space >= required_space
)
if can_unlock:
    print("You unlocked the chest")
else:
    print("The chest stays shut")

homework_done = True
if homework_done:
    print("Movie time")
else:
    print("Finish homework first")
