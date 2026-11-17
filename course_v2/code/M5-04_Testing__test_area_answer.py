# M5-04_Testing - test_area.py
def area(width, height):
    return width * height

assert area(4, 3) == 12
assert area(0, 7) == 0
assert area(1, 9) == 9
print("area() passed!")
