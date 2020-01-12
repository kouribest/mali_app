from python:3.7

arg DJANGO_ADMIN_USERNAME
arg DJANGO_ADMIN_PASSWORD
arg DOMAIN

env APP_HOME = /opt/app

workdir $APP_HOME

copy . .

run pip install --no-cache-dir -r requirements.txt

entrypoint python manage.py runserver 0.0.0.0:8001
