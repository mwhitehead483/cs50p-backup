def collect():
    total = 0
    price = 50  # The total cost of the coke

    while total < price:
        amount_due = price - total
        print(f"Amount Due: {amount_due}")

        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            total += coin

    # Once the loop finishes, total is >= 50
    change = total - price
    print(f"Change owed: {change}")

def main():
    collect()

main()
