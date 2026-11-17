# M4-04_Elif - traffic_light.py
colour = input("Light colour? ").lower()
if colour == "red":
    print("Stop")
elif colour == "amber":
    print("Get ready")
elif colour == "green":
    print("Go")
else:
    print("That's not a traffic light colour!")
