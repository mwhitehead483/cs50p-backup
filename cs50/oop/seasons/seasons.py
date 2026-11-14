from datetime import date,datetime
import inflect
import sys

p = inflect.engine()

def main():
    dob = input("Date of Birth: ").strip()
    try:
        delta = minutes_passed(dob)
        words = p.number_to_words(delta, andword="")
        print(f"{words.capitalize()} minutes")
    except ValueError:
        sys.exit("Invalid Date")


def minutes_passed(dob):
    birth_date = date.fromisoformat(dob)
    today = date.today()
    delta = today - birth_date
    minutes = delta.days * 24 * 60
    return minutes

if __name__ == "__main__":
    main()
