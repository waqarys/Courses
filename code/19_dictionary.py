# Lesson 19 — labels instead of positions
student = {
    "name": "Jimmy",
    "age": 15,
    "grade": "Year 10",
}
print(student["name"])
print(student["age"])

student["school"] = "Code High"
student["age"] = 16
del student["grade"]
print(student)

character = {"name": "Archer", "level": 5, "health": 100}
print(character["name"])
