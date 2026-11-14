
bag = {}
def add_item(item):
    if item in bag:
        bag[item] += 1
    else:
        bag[item] = 1

def main():
    while True:
        try:
            item = input().strip().lower()
            add_item(item)
        except EOFError:
            print()
            break

    for item, qty in sorted(bag.items()):
        print(f"{qty} {item.upper()}")

if __name__ == "__main__":
    main()

