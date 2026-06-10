# To track the stocks and Investment

stocks = {
    "BSE SENSEX": 180,
    "TSLA": 250,
    "NIFTY-50": 150
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Total Investment =", total)
else:
    print("Stock not found")