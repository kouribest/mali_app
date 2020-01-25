from python:3.7-alpine

arg DJANGO_ADMIN_USERNAME
arg DJANGO_ADMIN_PASSWORD
arg DJANGO_ADMIN_EMAIL
arg DJANGO_DOMAIN

env APP_HOME = /opt/app

workdir $APP_HOME

RUN apk update && apk add gcc libc-dev make libffi-dev openssl-dev python3-dev \
		libxml2-dev libxslt-dev mariadb-dev build-base jpeg-dev zlib-dev


copy . .

run pip install --no-cache-dir -r requirements.txt

entrypoint python manage.py makemigrations mali rdc --no-input

entrypoint python manage.py initialuser --username=$DJANGO_ADMIN_USERNAME --password=$DJANGO_ADMIN_PASSWORD --email=$DJANGO_ADMIN_EMAIL --no-input

entrypoint python manage.py migrate --no-input

