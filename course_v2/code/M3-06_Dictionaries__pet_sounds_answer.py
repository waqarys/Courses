# M3-06_Dictionaries - pet_sounds.py
sounds = {"cat": "meow", "dog": "woof",
          "duck": "quack", "sheep": "baa"}
print(sounds["duck"])
sounds["owl"] = "hoot"
for animal, sound in sounds.items():
    print(f"The {animal} says {sound}")
