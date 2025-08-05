products = []
prices = []
index = []

while True:
    prod = input("What item would you like to add? ")
    if prod == "quit":
        break

    price = input("What is the price of the item? ")
    if price == "quit":
        break

    products.append(prod)
    prices.append(price)
    index.append(len(products))

    print("Item added to list.")

print("---")
for i in range(len(products)):
    print(f"Item: {index[i]}\n Product: {products[i]} \n Price: {prices[i]}")