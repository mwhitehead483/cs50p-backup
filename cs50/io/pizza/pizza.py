import csv
import sys
from sys import argv
from tabulate import tabulate


def showTable(filename):
    table_data = []

    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            table_data.append(row)

    headers = table_data[0]
    rows = table_data[1:]
    #
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

def check_commandline():
    # 1. Check if the user provided enough arguments
    # len(sys.argv) includes the script name, so 2 means: script_name + 1 argument
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    try:
        showTable(sys.argv[1])
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    check_commandline()
