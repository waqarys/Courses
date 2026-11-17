# M4-09_Loop_Control - skip_it.py
scores = [8, -1, 6, 10, -1, 7]
total = 0
for score in scores:
    if score < 0:
        print("Skipping a missing score")
        continue
    total += score
print("Total of real scores:", total)
