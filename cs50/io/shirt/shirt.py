import sys
import os
from PIL import Image, ImageOps

def pasteImage(person_path, shirt_path, output_path="output.jpg"):
    print("processing image")
    person_image = Image.open(person_path)
    shirt_image = Image.open(shirt_path)

    target_size = shirt_image.size
    fitted_person = ImageOps.fit(person_image, target_size)
    fitted_person.paste(shirt_image, (0, 0), shirt_image)
    fitted_person.save(output_path)
    print(f"Successfully saved to {output_path}")

def check_commandline():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    person_file = sys.argv[1]
    output_file = sys.argv[2]
    shirt_file = "shirt.png"

    _, ext_input = os.path.splitext(person_file)
    _, ext_output = os.path.splitext(output_file)

    valid_extensions = (".jpg", ".jpeg", ".png")

    # Check input extension
    if ext_input.lower() not in valid_extensions:
        sys.exit("Invalid input")

    # Check output extension
    if ext_output.lower() not in valid_extensions:
        sys.exit("Invalid output")

    # Check if input and output extensions match
    if ext_input.lower() != ext_output.lower():
        sys.exit("Input and output have different extensions")

    # Ensure input file exists
    if not os.path.exists(person_file):
        sys.exit("Input does not exist")

    pasteImage(person_file, shirt_file, output_file)

if __name__ == "__main__":
    check_commandline()
