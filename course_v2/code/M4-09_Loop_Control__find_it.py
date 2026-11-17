# M4-09_Loop_Control - find_it.py
lockers = ["books", "shoes", "keys", "lunch", "ball"]
for i in range(len(lockers)):
    print("Checking locker", i)
    if lockers[i] == "keys":
        print("Found the keys in locker", i)
        break
print("Search over.")
