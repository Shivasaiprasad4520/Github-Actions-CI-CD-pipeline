FROM  python:3.11.1-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
