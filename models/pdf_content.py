from pydantic import BaseModel

class PdfContent(BaseModel):
    id: str  | None=None
    image_text:str | None=None
    text: str | None=None
    