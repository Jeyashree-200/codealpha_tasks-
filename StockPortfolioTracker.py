# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 330,
    "AMZN": 135
}

portfolio = {}
total_value = 0

print("=" * 45)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 45)

while True:
    stock = input("Enter Stock Name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))

    portfolio[stock] = quantity

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value

    print(f"{stock}")
    print(f"Price    : ${price}")
    print(f"Quantity : {quantity}")
    print(f"Value    : ${value}")
    print("-" * 25)

print("Total Investment = $", total_value)

# Save to text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO\n\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}  Qty:{quantity}  Value:${value}\n")

    file.write(f"\nTotal Investment = ${total_value}")

print("\nPortfolio saved to portfolio.txt")
