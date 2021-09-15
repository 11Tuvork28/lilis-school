# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PORT=8800
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install uwsgi
COPY . /code/

