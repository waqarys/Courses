# M4-09_Loop_Control - adder.py
total = 0
while True:
    text = input("Number (q to quit): ")
    if text == "q":
        break
    if not text.isdigit():
        print("Skipping", text)
        continue
    total += int(text)
print("Total:", total)
