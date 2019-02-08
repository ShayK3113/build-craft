FROM python:3.6.8-jessie

RUN apt-get update && \
    apt-get install -y python3-distutils-extra git

RUN git clone https://github.com/ShayK3113/build-craft.git
