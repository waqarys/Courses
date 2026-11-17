# M4-06_Match_Case - calculator.py
a = float(input("First number: "))
op = input("Operation (+ - * /): ")
b = float(input("Second number: "))
match op:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*" | "x":
        result = a * b
    case "/":
        result = a / b
    case _:
        result = "unknown operation"
print("Result:", result)
