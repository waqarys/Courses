# M3-04_For_Each_Item - numbered.py
snacks = ["apple", "banana", "mango", "grapes"]
number = 1
for snack in snacks:
    print(f"{number}. {snack}")
    number = number + 1
print(f"That's {number - 1} snacks.")
