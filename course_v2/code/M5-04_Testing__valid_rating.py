# M5-04_Testing - valid_rating.py
def is_valid_rating(text):
    if not text.isdigit():
        return False
    number = int(text)
    return 1 <= number <= 5

tests = ["3", "1", "5", "0", "6", "9", "abc", ""]
for t in tests:
    print(f"{t!r:6} -> {is_valid_rating(t)}")
