FROM python:3.11-slim

WORKDIR /app

COPY jokes.py .
COPY index.html .

EXPOSE 8080

CMD ["python", "jokes.py"]
