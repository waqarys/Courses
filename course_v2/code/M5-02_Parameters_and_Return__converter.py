# M5-02_Parameters_and_Return - converter.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def describe(celsius):
    f = c_to_f(celsius)
    if celsius >= 30:
        feel = "hot"
    elif celsius >= 15:
        feel = "mild"
    else:
        feel = "cold"
    return f"{celsius}°C is {f}°F and feels {feel}"

for temp in [0, 20, 35]:
    print(describe(temp))
