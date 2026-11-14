import sys
from sys import argv

def buy_bitcoin(qty):
    bitcoin_price = float(97845.0243)
    total = bitcoin_price * float(qty)
    print(f"${total:,.4f}")

def main():
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
        
    try:
        # Try converting the string to a float
        qty = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    buy_bitcoin(float(sys.argv[1]))

if __name__ == "__main__":
    main()
