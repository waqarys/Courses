# M5-02_Parameters_and_Return - area.py
def area(width, height):
    return width * height

room = area(4, 3)
print("Room:", room, "square metres")
garden = area(10, 6)
print("Garden:", garden)
print("Total:", room + garden)
print("A 5 by 5 square:", area(5, 5))
