import sys
from sys import argv


def linecount():
    try:
        line_count = 0
        with open(sys.argv[1]) as file:
            for line in file:
                # Strip leading/trailing whitespace
                stripped = line.strip()

                # Check if the line is not blank and not a comment
                if stripped and not stripped.startswith("#"):
                    line_count += 1
        print(line_count)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def main():
    # 1. Check if the user provided enough arguments
    # len(sys.argv) includes the script name, so 2 means: script_name + 1 argument
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a PYTHON file")
        sys.exit(1)
    try:
        with open(sys.argv[1]) as file:
            # Your code to process lines goes here
            linecount()
            pass
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

main()
