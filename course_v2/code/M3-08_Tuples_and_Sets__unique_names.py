# M3-08_Tuples_and_Sets - unique_names.py
sign_ups = ["Asha", "Leo", "Asha", "Mia", "Leo", "Asha"]
print(len(sign_ups), "sign-ups")
unique = set(sign_ups)
print(len(unique), "different people")
print("Mia" in unique)
unique.add("Tom")
unique.add("Mia")
print(sorted(unique))
