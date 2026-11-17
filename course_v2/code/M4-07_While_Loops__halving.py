# M4-07_While_Loops - halving.py
number = 100
steps = 0
while number > 1:
    number = number // 2
    steps = steps + 1
    print(number)
print("Steps:", steps)
