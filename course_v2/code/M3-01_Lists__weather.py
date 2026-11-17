# M3-01_Lists - weather.py
temps = [18, 21, 25, 19, 23, 27, 22]
print("Days recorded:", len(temps))
print("Hottest:", max(temps))
print("Coldest:", min(temps))
total = sum(temps)
average = total / len(temps)
print("Average:", round(average, 1))
