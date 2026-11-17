# M5-04_Testing - test_is_even.py
def is_even(n):
    return n % 2 == 0

assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True
assert is_even(-2) == True
print("All tests passed!")
