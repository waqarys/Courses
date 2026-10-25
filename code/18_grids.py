# Lesson 18 — negative indexes, slices, and a grid
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[1:4])
print(numbers[1:5:2])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1][2])  # the 6
print(matrix[0][1])
matrix[1][1] = 10
print(matrix)
