#FROM python:3.9.7-slim-buster
FROM nikolaik/python-nodejs:python3.10-nodejs20

RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD ["bash","start.sh"]

#render only
RUN python keep_alive.py
