# import module
from pdf2image import convert_from_path
 
poppler_path = r"C:\Program Files\poppler-21.10.0\Library\bin"
# Store Pdf with convert_from_path function
images = convert_from_path(pdf_path = 'example.pdf', poppler_path=poppler_path)
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')