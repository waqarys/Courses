# M3-05_Grids - pixel_art.py
heart = ["0110110",
         "1111111",
         "1111111",
         "0111110",
         "0011100",
         "0001000"]
for row in heart:
    print(row.replace("1", "#").replace("0", " "))
print(heart[0][1], heart[5][0])
