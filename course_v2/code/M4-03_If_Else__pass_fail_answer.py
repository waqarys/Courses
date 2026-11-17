# M4-03_If_Else - pass_fail.py
score = int(input("Test score (0-100): "))
if score >= 50:
    print("Pass!", score - 50, "marks above 50")
else:
    print("Not this time.", 50 - score, "more marks needed")
