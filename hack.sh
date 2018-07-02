#!/bin/sh


STATIC_DIR=/code/static
if [ ! -d $STATIC_DIR || ! -z "$(ls -A $STATIC_DIR)" ]; then
	python manage.py collectstatic
fi

python manage.py makemigrations me
python manage.py makemigrations posts
python manage.py makemigrations profiles
python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@example.com', is_superuser=True).delete(); User.objects.create_superuser('${SUPERUSER_NAME}', '${email}', '${SUPERUSER_PWD}')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000
