FROM python:3.5

ADD . /app
WORKDIR /app


RUN pip install tox