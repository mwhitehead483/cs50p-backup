def parse_date():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        datestr = input("Date: ").strip()

        try:
            # Format 1: MM/DD/YYYY
            if "/" in datestr:
                parts = datestr.split("/")
                if len(parts) != 3:
                    continue
                mm = int(parts[0])
                dd = int(parts[1])
                yyyy = int(parts[2])

            # Format 2: Month Day, Year (e.g., September 8, 1636)
            # e.g. September 8, 1636
            elif "," in datestr:
                clean_str = datestr.replace(",", "")
                parts = clean_str.split()
                if len(parts) != 3:
                    continue
                month_name = parts[0]
                dd = int(parts[1])
                yyyy = int(parts[2])

                if month_name not in months:
                    continue
                mm = months.index(month_name) + 1

            else:
                continue

            # Validate calendar ranges (1-12 for months, 1-31 for days)
            if not (1 <= mm <= 12 and 1 <= dd <= 31):
                continue

            # Return the successfully formatted YYYY-MM-DD string
            return f"{yyyy:04}-{mm:02}-{dd:02}"

        except (ValueError, IndexError):
            # Catches unexpected string-to-int conversions and loops back to input
            pass


def main():
    print(parse_date())


if __name__ == "__main__":
    main()
