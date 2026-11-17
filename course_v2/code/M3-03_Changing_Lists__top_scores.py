# M3-03_Changing_Lists - top_scores.py
scores = [40, 95, 72, 18]
scores[3] = 60
print(scores)
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)
print("Best:", scores[0])
print(100 in scores)
