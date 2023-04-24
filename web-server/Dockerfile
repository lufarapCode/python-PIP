FROM python:3.10

WORKDIR /app-webService
COPY requirements.txt /app-webService/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app-webService/requirements.txt

COPY . /app-webService

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]