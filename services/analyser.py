from fastapi import UploadFile
from utils.pdf_tools import get_pdf_images
from utils.ocr_tools import convert_img_to_text

class PDFAnalyser:

    def __init__(self) -> None:
        self.pdf_image_texts = []
        self.image_texts = []

    def onPDF(self,file:UploadFile) -> None:
        self.pdf_file = file
        self.pdf_image_names = get_pdf_images(file.file)
        self.pdf_image_texts = []
        img_texts = [convert_img_to_text(image_name) for image_name in self.pdf_image_names]
        text_line = 0
        for text in img_texts:
            self.pdf_image_texts.append(text)
    
    def onImg(self,file:UploadFile) -> None:
        self.pdf_file = file
        img_texts = convert_img_to_text(file.file)
        print(img_texts)
        self.image_texts = img_texts
    
