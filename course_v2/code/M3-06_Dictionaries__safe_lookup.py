# M3-06_Dictionaries - safe_lookup.py
sounds = {"cat": "meow", "dog": "woof", "cow": "moo"}
print("dog" in sounds)
print("fish" in sounds)
print(sounds.get("cow"))
print(sounds.get("fish"))
print(sounds.get("fish", "...silence"))
