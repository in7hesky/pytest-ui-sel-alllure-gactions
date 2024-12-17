FROM python:3.13.1-slim-bookworm

RUN apt update && apt install --no-install-recommends --no-install-suggests chromium -y

WORKDIR /framework

COPY ./requirements.txt /framework

RUN pip install --no-cache-dir -r requirements.txt
