---
id: "3.5"
title: "Grids: Lists Inside Lists"
module: 3
module_title: "Data Structures"
next: "Dictionaries"
minutes: 8.42
thumb_code: 'board[1][1] = "X"'
goals: ["A list can hold other lists", "grid[row][col]: two indexes", "Changing one square", "Printing a grid with a loop"]
youtube:
  title: "Python Lesson 3.5: 2D Lists - Grids, Game Boards and grid[row][col] | Introduction to Python"
  description: |
    Put lists inside lists to make grids! Ziggy the Python explains two-dimensional lists with a seating chart and
    a noughts and crosses board, how grid[row][col] finds one square, how to change a square, and how to print
    a grid neatly with a loop. We also total a table of scores row by row.
    For beginners aged 7 to 20.
  tags: [python 2d list, python nested list, python grid, tic tac toe python, learn python, fun skill builders]
---

<!-- Booklet chapter 3: two-dimensional arrays. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. So far, our lists have been like a single line of carriages. But lots of things in the real world are grids: a chessboard, a cinema's seats, a spreadsheet, the pixels on your screen. Today we'll make grids in Python, by putting lists inside lists.

## STUDY | Rows and columns
@ table  | col 0 | col 1 | col 2 ; row 0 | Asha | Leo | Mia ; row 1 | Sam | Zara | Tom
Think about a seating chart in a classroom. There are rows going across, and columns going down. To find someone, you need two numbers: which row, and which column. Asha is in row zero, column zero. Zara is in row one, column one.
@ point A grid is a list of rows
In Python, we make a grid as a list of rows, where each row is itself a list. It's a list inside a list. Programmers call this a two dimensional list, or a 2D list, because it has two directions: across and down.
@ point Rows and columns both start at 0
Just like normal lists, both the rows and the columns are numbered from zero.
@ point Like map coordinates or a spreadsheet
If you've played a board game with lettered columns and numbered rows, or used a spreadsheet with cells like B three, you already know this idea. Every square has two coordinates.

## STUDY | grid[row][col]
@ snippet seats = [["Asha", "Leo", "Mia"],\n         ["Sam", "Zara", "Tom"]]
Here's the seating chart in Python. An outer pair of square brackets for the whole grid. Inside, two rows, and each row is a list of three names.
@ point seats[1] gives a whole ROW
If we use one index, like seats one, we get a whole row: the list Sam, Zara, Tom.
@ point seats[1][2] gives one SEAT: row 1, column 2
If we use two indexes, we get one seat. Seats one, two, means: go to row one, then go to column two inside it. That's Tom.
@ point Read it as: first the row, then the column
Always the row first, then the column. A memory trick: you walk along the corridor to the right row, then step sideways to the seat.
@ point len(grid) = rows, len(grid[0]) = columns
And to measure a grid, the length of the grid tells you the number of rows, and the length of the first row tells you the number of columns.

## CODE | seats.py
```python
seats = [["Asha", "Leo", "Mia"],
         ["Sam", "Zara", "Tom"]]
print(seats[0])
print(seats[1][1])
print(seats[0][2])
print(len(seats), "rows")
print(len(seats[0]), "columns")
```
@ line 1-2 | A list of two rows
Lines one and two make the seating chart: a list containing two rows.
@ line 3 | One index = a whole row
Line three uses one index, zero, so it gets a whole row.
@ line 4 | Row 1, column 1
Line four uses two indexes: row one, column one.
@ line 5 | Row 0, column 2
Line five: row zero, column two.
@ predict 6 | Which names will lines 4 and 5 print?
Using the table we drew earlier, which names will lines four and five print?
@ run | A row, then single seats
Run. The whole first row as a list. Then Zara, at row one column one. Then Mia, at row zero column two.
@ line 6-7 | Measure the grid
Lines six and seven measure the grid.
@ run | 2 rows, 3 columns
Run. Two rows, and three columns.

## CODE | board.py
```python
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
board[1][1] = "X"
board[0][2] = "O"
for row in board:
    print(" ".join(row))
```
@ say
Now let's make a noughts and crosses board, also called tic tac toe.
@ line 1-3 | Three rows of three empty squares
Lines one to three make the board: three rows, each with three dashes for empty squares. Laying it out over three lines makes it look like the real board.
@ line 4 | Place an X in the centre
Line four places an X in the centre square: row one, column one.
@ line 5 | Place an O in the top right
Line five places an O in the top right: row zero, column two.
@ line 6 | Loop through the rows
Line six loops through the board, one row at a time. Each row is a list of three squares.
@ line 7 | " ".join(row) glues the squares with spaces
Line seven uses a new trick: a string with a space, dot join, and the row. Join glues all the items of a list into one string, with a space between each one. It turns a list into a neat line of text.
@ predict 6 | Where will the X and the O appear?
Picture the board. Where will the X and the O appear?
@ run | X in the centre, O top right
Run. A proper board! The O is in the top right corner, and the X is in the middle. Without join, each row would print with square brackets and quote marks, which looks messy.
@ edit 8 => board[2][0] = "X"
Let's make another move, after the loop: an X in the bottom left, row two, column zero.
@ edit 9 => print(board[2])
And print the bottom row.
@ run | The grid changed after it was printed
Run. The board is printed as before, because the loop ran before the move. Then the bottom row shows the new X at the start. Changing a grid is exactly like changing a list: use the indexes and an equals sign.

## CODE | score_table.py
```python
scores = [[7, 9, 8],
          [5, 6, 10],
          [9, 9, 9]]
players = ["Asha", "Leo", "Mia"]
row_number = 0
for row in scores:
    name = players[row_number]
    print(name, row, "total", sum(row))
    row_number = row_number + 1
```
@ say
Grids aren't just for games. Here's a table of scores: three players, each with three rounds.
@ line 1-3 | Each row = one player's three rounds
Each row holds one player's scores for three rounds.
@ line 4 | A matching list of names
A separate list holds the players' names, in the same order as the rows.
@ line 5 | A counter for the row number
A counter, starting at row zero.
@ line 6 | Loop through each row
Then we loop through the rows.
@ line 7 | Look up the name for this row
Line seven uses the counter to find the matching name.
@ line 8 | sum() of the row
Line eight prints the name, the row of scores, and the row's total using sum.
@ line 9 | Next row
And line nine moves the counter on.
@ predict 6 | Who scores the most?
Add up each row in your head. Who has the highest total?
@ run | Mia wins with 27
Run. Asha, twenty four. Leo, twenty one. Mia, twenty seven. Mia wins! This is the same idea as a spreadsheet: rows of data, with a total at the end of each row.

## CODE | pixel_art.py
```python
heart = ["0110110",
         "1111111",
         "1111111",
         "0111110",
         "0011100",
         "0001000"]
for row in heart:
    print(row.replace("1", "#").replace("0", " "))
print(heart[0][1], heart[5][0])
```
@ say
Here's a fun one. Every picture on your screen is a grid of tiny dots called pixels. Let's draw a picture from a grid of ones and zeros.
@ line 1-6 | Six rows: 1 = coloured pixel, 0 = empty
This grid has six rows. This time each row is a string, and a string is a sequence of characters, so it works like a row of squares too. A one means a coloured pixel, and a zero means an empty one. Can you see a shape hiding in the numbers?
@ line 7 | Loop through the rows
Line seven loops through the rows.
@ line 8 | Swap 1 for # and 0 for a space
Line eight prints each row, after replacing every one with a hash, and every zero with a space. We chain two replace methods, one after the other.
@ predict 6 | What picture will appear?
What picture do you think will appear? Look at the pattern of ones.
@ line 9 | Two single pixels: row 0 col 1, and row 5 col 0
And line nine prints two single pixels using two indexes: row zero column one, and row five column zero.
@ run | A heart made of pixels
Run. A heart! Then a one and a zero: the pixel at row zero column one is coloured, and the one at row five column zero is empty. Real images work exactly like this, except each pixel stores a colour instead of just a one or a zero, and there are millions of them. Your phone's screen is one gigantic grid.

## STUDY | Common mistakes
@ table Mistake | What happens ; board[1, 1] | TypeError: use two sets of brackets [1][1] ; board[3][0] on a 3×3 board | IndexError: rows go 0 to 2 ; mixing up row and column | the X lands in the wrong square ; forgetting a comma between rows | SyntaxError or odd results
Common grid mistakes. Writing both indexes inside one set of brackets with a comma gives a TypeError. Use two separate pairs of brackets. Going past the edge gives an IndexError, just like a normal list. Mixing up rows and columns puts things in the wrong square with no error at all. And forgetting the comma between rows causes errors that can be confusing.

## REVISE | Quick revise
@ point A grid is a list of rows; each row is a list
A grid is a list of rows, and each row is a list.
@ point grid[row][col]: row first, then column
To find one square, use the row first, then the column.
@ point Change a square: grid[r][c] = value
Change a square with the indexes and an equals sign.
@ point Print neatly: for row in grid: print(" ".join(row))
And print a grid neatly with a loop and join.

## PRACTICE | Change the centre
@ task Make a 3×3 board of "." characters.\n1. Put an "X" in the centre and an "O" in each corner\n2. Print the board neatly with a loop
Your turn. Make a three by three board, filled with dots. Put an X in the centre, and an O in all four corners. Then print the board neatly using a loop.
@ hint Corners: [0][0], [0][2], [2][0], [2][2]
Hint: the four corners are row zero column zero, row zero column two, row two column zero, and row two column two.
@ pause 15
Pause the video and try it.

## ANSWER | corners.py
```python
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
```
@ line 1-3
The empty board.
@ line 4
X in the centre.
@ line 5-8
And an O in each corner.
@ line 9-10
Then the loop prints each row.
@ run
Run. O, dot, O. Dot, X, dot. O, dot, O. A perfect pattern. Well done!

## OUTRO
Fantastic! You can now build and change grids, which is how many games store their boards and maps. Next time, we'll meet dictionaries, which store information with labels instead of index numbers. Like, share and subscribe, and keep coding. Happy Learning!
