import fitz  # PyMuPDF
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Hide the root Tkinter window
Tk().withdraw()

# Prompt the user to select a PDF file
pdf_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")], title="Select the PDF file")
if not pdf_path:
    print("No file selected.")
    exit()

# Load the PDF
document = fitz.open(pdf_path)

# List to store images for each PDF page
images = []

# Render each page and add it to the images list
for page_num in range(document.page_count):
    page = document.load_page(page_num)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    images.append(img)

# Define the separation size (in pixels)
separation_size = 20

# Calculate total height for the combined image including separations
total_height = sum(img.height for img in images) + (len(images) - 1) * separation_size
max_width = max(img.width for img in images)

# Create a new blank image with the combined dimensions
combined_image = Image.new("RGB", (max_width, total_height), "black")  # 'white', 'black' or other color for separation

# Paste each image into the combined image with separation
current_y = 0
for img in images:
    combined_image.paste(img, (0, current_y))
    current_y += img.height + separation_size  # Add the image height plus separation

# Set the output path to the same directory as the PDF file, with the same name
output_path = os.path.splitext(pdf_path)[0] + '.jpg'
combined_image.save(output_path, 'JPEG')

print(f"Combined JPEG saved as {output_path}")
