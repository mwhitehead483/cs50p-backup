from validator_collection import checkers

def is_valid_email(email):
    """Returns True if valid, False otherwise."""
    return checkers.is_email(email)

def main():
    email = input("What is your email address? ")
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
