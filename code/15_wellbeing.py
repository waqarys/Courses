# Lesson 15 — a habit check-in, not a medical test
# Replace the sample scores with int(input(...)) when you record.
print("Daily check-in. Rate each one from 1 to 5.")

name = "Asha"
age = "12"
feel_positive = 4
did_exercise = 3
ate_well = 5
drank_water = 4
slept_well = 3

score = (feel_positive + did_exercise + ate_well + drank_water + slept_well) / 5

print()
print(name + "'s check-in (age " + age + ")")
print("Score:", round(score, 1), "/ 5")
print("Feel positive:", "*" * feel_positive)

if score >= 4:
    print("Strong day")
else:
    print("Be kind to yourself today")
