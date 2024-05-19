from sqlalchemy.orm import Session
from . import models, schemas

def create_pdf_document(db: Session, pdf: schemas.PDFDocumentCreate):
    db_pdf = models.PDFDocument(filename=pdf.filename)
    db.add(db_pdf)
    db.commit()
    db.refresh(db_pdf)
    return db_pdf

def get_pdf_document(db: Session, pdf_id: int):
    return db.query(models.PDFDocument).filter(models.PDFDocument.id == pdf_id).first()
