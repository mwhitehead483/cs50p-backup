def main():
    split_print()

def split_print():
    text = input("Enter a sentence: ")
    result = "...".join(text.split())
    print(result)

main()
