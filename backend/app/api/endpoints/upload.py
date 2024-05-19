from fastapi import APIRouter, UploadFile, Depends, File, HTTPException
from app import crud, schemas, models, deps
from sqlalchemy.orm import Session
import shutil
import os

router = APIRouter()

UPLOAD_DIRECTORY = "/app/uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

## Method to handle Uploaded PDF
@router.post("/", response_model=schemas.PDFDocument)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(deps.get_db)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")
        
    # Save file to local storage
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #Create DB entry
    pdf_doc = models.PDFDocument(filename=file.filename)
    db.add(pdf_doc)
    db.commit()
    db.refresh(pdf_doc)
    return pdf_doc

