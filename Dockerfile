# Specify the base image:
FROM python:3.10-slim-bullseye
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENV PG_HOST=postgres
ENV PG_PORT=5432
ENV PG_USER=postgres
ENV PG_PASSWORD=postgres
ENV PG_DATABASE=posgtres


CMD piccolo migrations new home --auto && piccolo migrations forwards all && python main.py