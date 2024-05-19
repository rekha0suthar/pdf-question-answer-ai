# PDF Question Answering Application

This project is a full-stack application that allows users to upload PDF documents and ask questions related to the content of the PDFs. The backend uses FastAPI and Hugging Face Transformers to handle the PDF processing and question-answering tasks, while the frontend is built with React.

# Prerequisites

- Docker
- Docker Compose


# Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rekha0suthar/pdf-question-answer-ai/
cd pdf-question-answer-ai
```

### 2. Create and Configure the .env File in root directory

    HUGGING_FACE_HUB_TOKEN=your_hugging_face_token_here

Setup virtual environment -- for backend

        python3 -m venv venv
        source venv/bin/activate 

## 3. Build and Run the Docker Containers

Adding Docker file in Backend and Frontend also create docker-compose.yml file and requirements.txt file in backend

## backend/Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY ./app /app/app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

// Create upload directory and set permissions -- comment

RUN mkdir /app/uploads && chmod -R 755 /app/uploads

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# frontend/Dockerfile

FROM node:LTS version

WORKDIR /app

COPY ./package.json ./package-lock.json\* /app/
RUN npm install

COPY . /app

CMD ["npm", "start"]

# requirements.txt

fastapi

uvicorn

SQLAlchemy

pydantic

PyMuPDF

transformers

torch

## run below command to start application

docker-compose up --build

## 4. Verify the Application

Frontend: Ensure your frontend is running and accessible at http://localhost:3000.

Backend: Ensure your backend is running and accessible at http://localhost:8000.

# API Documentation

The backend API consists of two main endpoints:

Upload PDF
Ask Question

1.  Upload PDF

    Endpoint: /upload

    Method: POST

    Description: Uploads a PDF file to the server.

    Request Body:

         file: PDF file to be uploaded.

    Response:

         200 OK: PDF uploaded successfully.

         400 Bad Request: Invalid file format or other error.

    Example Request:

        curl -X POST "http://localhost:8000/upload" -F "file=@/path/to/your/file.pdf"

    Example Response:
    {
    "filename": "file.pdf",
    "upload_date": "2024-05-18T10:02:18.661253"
    }

2.  Ask Question

    Endpoint: /question/{doc_id}

    Method: POST

    Description: Asks a question related to the content of the uploaded
    PDF.

    Path Parameters:

        doc_id: ID of the uploaded PDF document.

    Request Body:

        question: The question to be asked.

    Response:

        200 OK: Answer to the question.
        404 Not Found: Document not found.
        400 Bad Request: Invalid question format or other error.

    Example Request:

        curl -X POST "http://localhost:8000/question/1" -H "Content-Type: application/json" -d '{"question": "What is the content of the PDF?"}'

    Example Response:

        {
            "answer": "The PDF contains information about..."
        }

Demo Video

https://github.com/rekha0suthar/pdf-quest-ans-ai/assets/71004640/e61be31b-8c7d-47f2-984b-96c46d555532


