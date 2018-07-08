#!/bin/sh


python manage.py collectstatic

python manage.py makemigrations posts
python manage.py makemigrations work
python manage.py makemigrations events
python manage.py makemigrations home
python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@example.com', is_superuser=True).delete(); User.objects.create_superuser('${SUPERUSER_NAME}', '${email}', '${SUPERUSER_PWD}')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000
