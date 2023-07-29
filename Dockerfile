# pulling the official Docker image.
FROM python:3.11.1-slim

# set work dir
WORKDIR /app

#set env variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN  apt-get update
RUN apt-get install git libpq-dev -y

# install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project.
COPY . .
