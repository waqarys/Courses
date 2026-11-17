# M4-07_While_Loops - keep_asking.py
answer = input("What is 9 x 8? ")
attempts = 1
while answer != "72":
    answer = input("Not quite. What is 9 x 8? ")
    attempts += 1
print(f"Correct in {attempts} attempts!")
