# M3-06_Dictionaries - votes.py
votes = ["mango", "apple", "mango", "kiwi", "mango", "apple"]
counts = {}
for fruit in votes:
    if fruit in counts:
        counts[fruit] = counts[fruit] + 1
    else:
        counts[fruit] = 1
print(counts)
