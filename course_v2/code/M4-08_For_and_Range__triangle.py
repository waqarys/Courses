# M4-08_For_and_Range - triangle.py
rows = 5
for row in range(1, rows + 1):
    line = ""
    for star in range(row):
        line = line + "*"
    print(line)
