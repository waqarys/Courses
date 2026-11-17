# M3-07_Records - top_student.py
students = [
    {"name": "Asha", "score": 88},
    {"name": "Leo", "score": 72},
    {"name": "Mia", "score": 95},
]
best = students[0]
total = 0
for s in students:
    total = total + s["score"]
    if s["score"] > best["score"]:
        best = s
print("Top student:", best["name"], best["score"])
print("Class average:", round(total / len(students), 1))
