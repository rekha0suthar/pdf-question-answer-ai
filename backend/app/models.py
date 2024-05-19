from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class PDFDocument(Base):
    __tablename__ = "pdf_documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    upload_date = Column(DateTime, default=datetime.utcnow)
