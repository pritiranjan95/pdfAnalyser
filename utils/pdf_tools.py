from PyPDF2 import PdfReader
import os
os.makedirs

def get_pdf_images(pdf_file):
    reader = PdfReader(pdf_file)
    images = []
    count = 0

    for page in reader.pages:

        for image_file_object in page.images:
            img_name = os.getcwd()+"/.temp/" +str(count) + image_file_object.name
            with open(img_name,'wb') as fp:
                fp.write(image_file_object.data)
                count += 1
            images.append(img_name)
    return images
        

    