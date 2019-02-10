FROM python:3.7.2-alpine3.9

RUN apk update && \
    apk add --no-cache git bash bash-completion jpeg-dev zlib-dev

RUN apk add --no-cache --virtual .build-deps build-base linux-headers \ 
    && pip3 install pip --upgrade \   
    && pip3 install Pillow \
    && apk del .build-deps

RUN git clone https://github.com/ShayK3113/build-craft.git
