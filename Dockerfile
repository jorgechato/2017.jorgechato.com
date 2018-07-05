FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

ENTRYPOINT ./utilities/wait-for-it.sh database:5432 --strict -- ./utilities/hack.sh
