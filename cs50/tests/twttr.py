def shorten(data):
    result = ""
    for char in data:
        if char not in "aeiouAEIOU" :
            result += char
    return result

def main():
    txt = input("Input: ")
    print("Output: " + shorten(txt))

main()
