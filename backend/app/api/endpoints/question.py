from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas, deps
from sqlalchemy.orm import Session
from app.utils import nlp_processing

router = APIRouter()

## Method to handle User's question
@router.post("/{doc_id}", response_model=str)
async def ask_question(doc_id: int, request: schemas.QuestionRequest, db: Session = Depends(deps.get_db)):
    pdf_doc = db.query(models.PDFDocument).filter(models.PDFDocument.id == doc_id).first()
    if not pdf_doc:
        raise HTTPException(status_code=404, detail="PDF document not found")
    
    answer = nlp_processing.get_answer_from_pdf(pdf_doc, request.question)
    return answer