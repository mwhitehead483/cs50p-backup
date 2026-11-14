import re
import sys

def convert(s):
    # Matches formats like: 9:00 AM to 5:00 PM, 9 AM to 5 PM, 9:00 AM to 5 PM, 9 AM to 5:00 PM
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("ValueError")

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start_time = convert_to_24hr(start_hour, start_min, start_period)
    end_time = convert_to_24hr(end_hour, end_min, end_period)

    return f"{start_time} to {end_time}"


def convert_to_24hr(hour_str, minute_str, period):
    hour = int(hour_str)
    minute = int(minute_str) if minute_str else 0

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{minute:02d}"

def time_str_padding(s):
    return f"'{s}'".ljust(12)

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        sys.exit(e)

if __name__ == "__main__":
    main()

