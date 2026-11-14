def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Max 6 letter, numbers must be at the end, min two letters at the beginning

def is_valid(s):
    count = 0
    # 1. First two characters must be letters
    if len(s) < 2  or not (s[0].isalpha() and s[1].isalpha()):
        return False
    # 2. Len between 2 and 6
    if not (2 <= len(s) <= 6) or not s.isalnum():
        return False
    # 3
    digit_found = False
    # Loop through remaining characters, if digit found, no alphas allowed
    for char in s[2:]:
        if char.isdigit() and not digit_found and char == '0':
            return False
        elif char.isdigit():
            digit_found = True
        if digit_found and char.isalpha():
            return False
    return True

main()

