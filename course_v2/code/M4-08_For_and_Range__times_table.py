# M4-08_For_and_Range - times_table.py
number = int(input("Which times table? "))
for i in range(1, 11):
    answer = number * i
    print(f"{i:>2} x {number} = {answer}")
print("Done!")
