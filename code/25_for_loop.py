# Lesson 25 — a known number of laps
for i in range(5):
    print("Lap", i)
print("Done")

items = ["map", "rope", "torch"]
for item in items:
    print("Pack", item)

for i, item in enumerate(items, start=1):
    print(i, item)

challenges = ["goblin", "trap", "prisoner", "dragon"]
for challenge in challenges:
    if challenge == "trap":
        print("Skip the trap")
        continue
    if challenge == "prisoner":
        print("Rescued")
        break
    print("Battled a", challenge)

for n in range(10, 0, -1):
    print(n)
print("Go")
