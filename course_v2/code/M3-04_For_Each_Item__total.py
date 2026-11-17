# M3-04_For_Each_Item - total.py
scores = [12, 7, 30, 18]
total = 0
for score in scores:
    total = total + score
    print("Added", score, "-> total", total)
print("Final total:", total)
