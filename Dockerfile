FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --user -r requirements.txt

COPY . /app/

CMD python3 manage.py runserver_plus 0.0.0.0:7253 --cert-file certificate/foo
