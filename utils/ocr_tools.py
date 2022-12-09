from PIL import Image
import pytesseract

def convert_img_to_text(image_name:str):
    image = Image.open(image_name)
    img_text = pytesseract.image_to_string(image)
    return img_text