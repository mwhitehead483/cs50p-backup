import inflect
p = inflect.engine()
words = []

while(True):
    try:
        name = input("Name: ")
        words.append(name)
        output = p.join(words)
    except EOFError:
        print()
        break
print(f"Adieu, adieu, to {output}")
