import csv
import sys
from tabulate import tabulate



def appendToFile(fileName, cleaned_data):
    """Writes headers and rows to the specified CSV file."""
    with open(fileName, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_data)


#  Reads and cleans fileName
def readTable(filename, cleanedfile):
    cleaned_data = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            # Skip the header row of the input file so it doesn't get processed as data
            next(reader, None)

            for row in reader:
                # Skip any empty rows
                if not row:
                    continue

                # Assuming input format: column 0 = "lastname, firstname", column 1 = "house"
                # strip the quotes, it will not be last name, first name house
                full_name_field = row[0].strip('" ')
                house_field = row[1].strip('" ') if len(row) > 1 else ""

                # Split the name by comma
                name_parts = [p.strip() for p in full_name_field.split(',')]

                if len(name_parts) >= 2:
                    last_name, first_name = name_parts[0], name_parts[1]
                else:
                    last_name, first_name = name_parts[0], ""

                # Store cleanly as [first_name, last_name, house]
                formatted_row = [first_name, last_name, house_field]
                cleaned_data.append(formatted_row)

    except FileNotFoundError:
        print("Error: Input file not found")
        sys.exit(1)

    # 1. Define the correct headers for the output file and table
    headers = ["first", "last", "house"]

    # Combine headers and data rows together
    table_data = [headers] + cleaned_data

    # 2. Write the complete table (including your clean headers) to the output file
    appendToFile(cleanedfile, table_data)

    # 3. Print the table nicely using tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))


def check_commandline():
    # We expect exactly 3 items in sys.argv: [script.py, before.csv, after.csv]
    if len(sys.argv) < 3:
        print("Too few command-line arguments (Expected: python script.py before.csv after.csv)")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("Both files must be CSV files")
        sys.exit(1)

    # Pass the input file (argv[1]) and output file (argv[2]) to readTable
    readTable(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    check_commandline()
