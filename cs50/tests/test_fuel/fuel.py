def convert(text):
    # Split the string into numerator and denominator
    try:
        numerator, denominator = text.split("/")
    except ValueError:
        raise ValueError("Invalid format")

    # Check if both parts are digits
    if not (numerator.isdigit() and denominator.isdigit()):
        raise ValueError("Numerator and denominator must be integers.")

    num = int(numerator)
    den = int(denominator)

        # Check for valid fraction range and no division by zero
    if den == 0 :
        raise ZeroDivisionError("Denominator cannot be zero.")
    if num > den:
        raise ValueError("Numerator cannot be greater than denominator.")

    fraction = (num / den) * 100
    return round(fraction)


def gauge(percent):
    if percent <= 1:  # <= 1%
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"

#  Possible values are None, E, F, or a percent
def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            # Prompt the user again if an invalid fraction or division by zero occurs
            pass

if __name__ == "__main__":
    main()
