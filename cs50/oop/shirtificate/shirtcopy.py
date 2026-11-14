from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

# 1. Open the image using Pillow
image_path = "shirtificate.png"
img = Image.open(image_path)
orig_width, orig_height = img.size

# 2. CREATE 'draw' AND INITIALIZE FONT
draw = ImageDraw.Draw(img)

# Bulletproof font loading (tries local ttf first, falls back gracefully to default with size)
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
except IOError:
    try:
        font = ImageFont.truetype("LiberationSans-Bold.ttf", 18)
    except IOError:
        try:
            font = ImageFont.load_default(size=20)
        except TypeError:
            font = ImageFont.load_default()

text = "Michael Whitehead took CS50"

# 3. Calculate text positioning inside the image dimensions
bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]
text_x = (orig_width - text_w) / 2
text_y = (orig_height - text_h) / 3  # Positioned roughly 1/3 down the shirt

# 4. Draw the text in white onto the image
draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

# 5. Save the modified image temporarily so FPDF can read it
modified_image_path = "output_shirt.png"
img.save(modified_image_path)

# --- FPDF SECTION ---
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.set_font("helvetica", "B", 26)
pdf.cell(0, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

# Choose your desired width in millimeters
img_w = 190
img_h = (orig_height / orig_width) * img_w

# A4 dimensions
page_w = 210
page_h = 297

printable_w = page_w - pdf.l_margin - pdf.r_margin
printable_h = page_h - pdf.t_margin - pdf.b_margin

x_center = pdf.l_margin + (printable_w - img_w) / 2
y_center = pdf.t_margin + (printable_h - img_h) / 2

# Insert the modified image
pdf.image(modified_image_path, x=x_center, y=y_center, w=img_w, h=img_h)

# Output the final PDF
pdf.output("shirtificate.pdf")
