# Lesson 17 — change a list, then visit every item
inventory = ["sword", "shield", "armor", "bow"]
inventory.append("health potion")
inventory.insert(1, "golden sword")
inventory.remove("shield")
dropped_item = inventory.pop()
print(inventory)
print("Dropped:", dropped_item)
print("Count:", len(inventory))

for item in inventory:
    print("You have a", item)
