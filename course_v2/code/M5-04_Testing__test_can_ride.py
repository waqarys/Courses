# M5-04_Testing - test_can_ride.py
def can_ride(height):
    return height > 120

assert can_ride(150) == True
assert can_ride(100) == False
assert can_ride(120) == True
print("All tests passed!")
