# M4-02_If - bonus.py
score = int(input("Your score: "))
if score >= 100:
    print("Bonus level unlocked!")
    score = score + 50
if score == 0:
    print("Keep practising!")
print("Final score:", score)
