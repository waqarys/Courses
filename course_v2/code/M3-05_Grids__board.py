# M3-05_Grids - board.py
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
board[1][1] = "X"
board[0][2] = "O"
for row in board:
    print(" ".join(row))
