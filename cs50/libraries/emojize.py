from emoji import emojize

def printEmoji():
    user_input = input("Input: " )
    print("Output: " + emojize(user_input, language='alias'))

def main():
    printEmoji()


if __name__ == "__main__":
    main()

