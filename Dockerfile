FROM python:3.11-slim as builder

WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app ./app
COPY main.py .

CMD ["python", "main.py"]