FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

RUN apk add --no-cache \
					build-base \
					bash \
					postgresql-dev \
					gcc \
					python3-dev \
					libffi-dev \
					# Pillow
					jpeg-dev \
                    zlib-dev

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

ENTRYPOINT ./utilities/wait-for-it.sh database:5432 --strict -- ./utilities/hack.sh
