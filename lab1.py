def lab1():
    items = []
    prices = []
    running = True
 
    while running:
        item = input("Enter the item (Enter to quit): ").strip()
        if item == "":
            running = False
        else:
            price = input(f"Enter the price of {item}: $").strip()
            if price.replace(".", "", 1).isdigit():
                price = float(price)
                if 0 <= price <= 200:
                    items.append(item)
                    prices.append(price)
                else:
                    print("Invalid price (the price must be from 0 to 200).")
            else:
                print("Invalid input (please enter a number).")
    average = sum(prices) / len(items)
    print(f"The number of items you purchased: {len(items)}")
    print(f"The total price of your items is: ${sum(prices):.2f}")
    print(f"Average prices: {average:.2f}")
    print(f"The Highest item is: {max(prices)}")
    print(f"The Lowest item is: {min(prices)}")
 
lab1()
 
