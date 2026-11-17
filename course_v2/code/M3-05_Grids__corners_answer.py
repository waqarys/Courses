# M3-05_Grids - corners.py
board = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]
board[1][1] = "X"
board[0][0] = "O"
board[0][2] = "O"
board[2][0] = "O"
board[2][2] = "O"
for row in board:
    print(" ".join(row))
