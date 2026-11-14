def main():
    # Example usage:
    phrase = input("Enter a phrase with emoji: ")
    result = convert(phrase)
    print(result)



def convert(phrase):

    emoticons = {
        ":-)": "🙂",
        ":)": "🙂",
        ":-(": "🙁",
        ":(": "🙁"
    }

    for emoticon, emoji in emoticons.items():
        phrase = phrase.replace(emoticon, emoji)

    return phrase


main()
