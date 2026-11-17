# M3-04_For_Each_Item - score_adder.py
scores = [5, 9, 3, 8, 10]
total = 0
for score in scores:
    total = total + score
print("Total:", total)
print("Average:", total / len(scores))
