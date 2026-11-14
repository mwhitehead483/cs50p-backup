def get_fuel_level(text):
    try:
        # Split the string into numerator and denominator
        numerator, denominator = text.split("/")

        # Check if both parts are digits
        if numerator.isdigit() and denominator.isdigit():
            num = int(numerator)
            den = int(denominator)

            # Check for valid fraction range and no division by zero
            if den != 0 and num <= den:
                return float(num / den)

    except (ValueError, ZeroDivisionError):
        pass

    return None

def main():
    while True:
        fraction = input("Fraction: ")
        percent = get_fuel_level(fraction)

        if percent is not None:
            if percent >= 0.99:
                print("F")
                break
            elif percent <= 0.01:  # Caters safely to 0 or very small fractions
                print("E")
                break
            else:
                print(f"{round(percent * 100)}%")
                break

if __name__ == "__main__":
    main()
