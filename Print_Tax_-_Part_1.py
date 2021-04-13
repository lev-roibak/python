name = 0
price = 0
while name != "coffee":
    name = input('What is the product name?\n')

while price != "12.5":
    price = input('What is the price in NIS (without V.A.T)?\n')

price2 = float(price) + float(price) * 0.17
price3 = float(price) * 0.17
print(f"The price of coffee is {price} NIS + {price3} VAT = {price2} TOTAL.")