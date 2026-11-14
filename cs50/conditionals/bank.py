def main():
    greeting =  input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")


def value(greeting) :
    stripped_greeting = greeting.lower().strip()
    match stripped_greeting:
        case _ if stripped_greeting.startswith("hello"):
            return 0
        case _ if stripped_greeting.startswith("h"):
            return 20
        case _:
            return 100

if __name__ == "__main__":
    main()
