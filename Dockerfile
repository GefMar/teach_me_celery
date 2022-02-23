FROM python:3.8.11-slim

WORKDIR /teach_me_celery

RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3-dev && apt-get -y clean && apt-get -y autoremove

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

