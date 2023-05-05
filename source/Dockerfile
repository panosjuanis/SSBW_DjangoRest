FROM python:3.7-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt --default-timeout=1000 --no-cache-dir
RUN pip install psycopg2-binary
COPY . /code/