def menu_lookup(key):
    # Dictionary
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    for item, price in menu.items():
        if  item.lower() == key.lower():
            return item, price
    return None, 0.0

def processOrder():
        total = float(0.0)
        while True:
            try:
                item = input("Item: ")
                item, price = menu_lookup(item)  # Unpacks both values returned from lookup
                if item is None:
                    continue
                total += price
                # format currency
                print(f"Total:${total:.2f}")
            except EOFError:
                # Control-D to stop loop
                print()
                break


processOrder()
