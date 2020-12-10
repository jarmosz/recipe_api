FROM python:3.9-alpine
MAINTAINER Wojciech Jarmosz

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pipenv install --system --deploy --ignore-pipfile

RUN adduser -D user
USER user