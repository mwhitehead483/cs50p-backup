import sys
import os
from PIL import Image, ImageOps

def pasteImage(person_path, shirt_path, output_path="output.jpg"):
    # 1. Open both images
    print("processing image")
    person_image = Image.open(person_path)
    shirt_image = Image.open(shirt_path)

    # 2. Resize/Fit the person image to match the shirt's size
    target_size = shirt_image.size
 #   fitted_person = ImageOps.fit(person_image, target_size, Image.Resampling.LANCZOS)
     fitted_person = ImageOps.fit(person_image, target_size)

    # 3. Paste the shirt onto the person image using the shirt as a transparency mask
    fitted_person.paste(shirt_image, (0, 0), shirt_image)

    # 4. Save using the provided output path and display
    fitted_person.save(output_path)
    print(f"Successfully saved to {output_path}")


def check_commandline():
    # CS50 Shirt expects exactly 2 command-line arguments: [script.py, input.jpg, output.jpg]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    person_file = sys.argv[1]
    output_file = sys.argv[2]
    shirt_file = "shirt.png"

    # Split extensions
    _, ext_input = os.path.splitext(person_file)
    _, ext_output = os.path.splitext(output_file)

    # Valid extensions per CS50
    valid_extensions = (".jpg", ".jpeg", ".png")

    # Check if extensions are valid
    if ext_input.lower() not in valid_extensions or ext_output.lower() not in valid_extensions:
        sys.exit("Invalid output")

    # Check that input and output file extensions match
    if ext_input.lower() != ext_output.lower():
        sys.exit("Input and output have different extensions")

    # Ensure input file exists
    if not os.path.exists(person_file):
        sys.exit("Input does not exist")

    # Pass paths to pasteImage
    pasteImage(person_file, shirt_file, output_file)

if __name__ == "__main__":
    check_commandline()
