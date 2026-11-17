# M3-07_Records - student.py
student = {"name": "Asha", "year": 7,
           "score": 88, "club": "chess"}
print(student["name"])
print(f"{student['name']} is in year {student['year']}.")
student["score"] = student["score"] + 5
student["age"] = 12
print(student)
