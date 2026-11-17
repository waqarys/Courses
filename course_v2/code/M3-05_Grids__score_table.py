# M3-05_Grids - score_table.py
scores = [[7, 9, 8],
          [5, 6, 10],
          [9, 9, 9]]
players = ["Asha", "Leo", "Mia"]
row_number = 0
for row in scores:
    name = players[row_number]
    print(name, row, "total", sum(row))
    row_number = row_number + 1
