# M4-07_While_Loops - savings.py
savings = 0
goal = 50
weekly = 8
weeks = 0
while savings < goal:
    savings = savings + weekly
    weeks = weeks + 1
    print(f"Week {weeks}: {savings} coins")
print(f"Goal reached in {weeks} weeks!")
