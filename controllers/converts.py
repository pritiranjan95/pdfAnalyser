from utils import app
from fastapi import APIRouter
from fastapi import File,UploadFile
from services.analyser import PDFAnalyser

router = APIRouter()

@router.get("/converter_info")
def info():
    return "converter info"

@router.post("/convert_to_pdf/")
def convert_to_pdf_file(pdf_file:UploadFile):
    analyser = PDFAnalyser()
    analyser.onPDF(pdf_file)
    data = {
        "image_texts":analyser.pdf_image_texts
    }
    return data

@router.post("/upload_img/")
def upload_img_file(img_file:UploadFile):
    analyser = PDFAnalyser()
    analyser.onImg(img_file)
    data = {
        "image_texts":analyser.image_texts
    }
    return data
    

