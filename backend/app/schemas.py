from pydantic import BaseModel
from datetime import datetime

class PDFDocumentBase(BaseModel):
    filename: str

class PDFDocumentCreate(PDFDocumentBase):
    pass

class PDFDocument(PDFDocumentBase):
    id: int
    upload_date: datetime

    class Config:
        from_attributes=True

class QuestionRequest(BaseModel):
    question: str