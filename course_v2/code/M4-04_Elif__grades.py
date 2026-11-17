# M4-04_Elif - grades.py
score = int(input("Score out of 100: "))
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "D"
print(f"A score of {score} is a grade {grade}")
