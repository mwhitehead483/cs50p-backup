import argparse
from pyfiglet import Figlet

# 1. Set up the argument parser
parser = argparse.ArgumentParser(description="Render ASCII art text using figlet fonts.")
parser.add_argument("-f", "--font", default="slant", help="The font to use for rendering")

# 2. Parse the arguments from the command line
args = parser.parse_args()

# 3. Use the captured argument
f = Figlet(font=args.font)
message = input("Input: ")
print(f.renderText(message))
