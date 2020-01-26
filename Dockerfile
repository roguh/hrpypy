FROM jfloff/alpine-python:3.8-slim

COPY requirements.txt /requirements.txt
RUN /entrypoint.sh -x

WORKDIR /hrpypy
COPY . .
