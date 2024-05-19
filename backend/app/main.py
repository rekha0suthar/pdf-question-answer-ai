from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import upload, question
from app.database import engine, Base

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Your frontend URL
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(question.router, prefix="/question", tags=["question"])


# Create database tables
Base.metadata.create_all(bind=engine)