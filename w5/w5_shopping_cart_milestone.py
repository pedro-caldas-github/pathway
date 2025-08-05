items = []
prices = []
index = []

while True:
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        items.append(item)
        prices.append(price)
        index.append(len(items)-1)
        print(f"Item {item} added to cart")
    elif choice == "2":
        print("Cart:")
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i + 1}. {item}: ${price}")
        print("\n")
    elif choice == "3":
        print("Cart:")
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i + 1}. {item}: ${price}")
        print("\n")
        print("What item would you like to remove?")
        remove_choice = input("Enter the number: ")
        for i in range(len(items)):
            if i == int(remove_choice):
                items.pop(int(remove_choice)-1)
                prices.pop(int(remove_choice)-1)
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i + 1}. {item}: ${price}")
        print("\n")

    elif choice == "4":
        total = 0
        for i, price in enumerate(prices):
            total += price
        print(f"Total: ${total}")
        print("\n")
    else:
        break
