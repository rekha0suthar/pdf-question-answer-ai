# backend/Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY ./app /app/app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Create upload directory and set permissions
RUN mkdir /app/uploads && chmod -R 755 /app/uploads

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
