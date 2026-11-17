# M3-07_Records - class_list.py
students = [
    {"name": "Asha", "year": 7, "score": 88},
    {"name": "Leo", "year": 8, "score": 72},
    {"name": "Mia", "year": 7, "score": 95},
]
print(len(students), "records")
print(students[1]["name"])
for s in students:
    print(f"{s['name']:<6} year {s['year']}  {s['score']}")
