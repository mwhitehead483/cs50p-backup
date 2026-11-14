import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # XXX.XXX.XXX.XXX IP address
    #Matches a single digit from 0 to 9, OR a two-digit number from 10 to 99 (no leading zero), OR 100 to 199, OR 200 to 249, OR 250 to 255.
    pattern = r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    match = re.fullmatch(pattern, ip)
    if not match:
        return False
    #  Check all 4 numbers
    for i in range(1,5):
        octet = int(match.group(i))
        if not (0 <= octet <= 255):
            return False
    return True


if __name__ == "__main__":
    main()
