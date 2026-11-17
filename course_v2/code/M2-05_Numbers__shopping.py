# M2-05_Numbers - shopping.py
price_text = input("Price of one ice cream? ")
price = float(price_text)
count = 3
total = price * count
print(f"{count} ice creams cost {total}")
print("As text: " + str(total))
