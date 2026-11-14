def snake(data):
    result = ""
    for char in data:
        if char in data:
            if char.isupper():
                result += "_" + char.lower()
            else:
                result += char
    return result

def main():
    word = input("Give me a word: " )
    print("camelCase: " + word)
    print("snake_case: " + snake(word))

main()

