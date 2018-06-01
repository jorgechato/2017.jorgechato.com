FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT [ "gunicorn chato.wsgi" ]