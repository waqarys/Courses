# M4-04_Elif - weather.py
temp = int(input("Temperature in °C: "))
if temp >= 30:
    advice = "shorts, a hat and water"
elif temp >= 20:
    advice = "a T-shirt"
elif temp >= 10:
    advice = "a jumper"
elif temp >= 0:
    advice = "a coat and scarf"
else:
    advice = "everything! It's freezing"
print(f"At {temp}°C, wear {advice}.")
