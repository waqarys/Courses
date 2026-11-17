# M4-05_Complex_Conditions - delivery.py
total = 32
is_member = False
if total >= 50 or is_member:
    print("Free delivery!")
elif total >= 30 and not is_member:
    print("Delivery costs 2 coins.")
else:
    print("Delivery costs 5 coins.")
