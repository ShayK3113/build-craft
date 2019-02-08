FROM python:3.7.2-alpine3.9

RUN apk update && \
    apk add git bash bash-completion

RUN git clone https://github.com/ShayK3113/build-craft.git
