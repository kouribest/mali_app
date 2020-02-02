from python:3.7-alpine

arg DJANGO_ADMIN_USERNAME
arg DJANGO_ADMIN_PASSWORD
arg DJANGO_ADMIN_EMAIL
arg DJANGO_DOMAIN

env APP_HOME = /opt/app

workdir $APP_HOME

RUN apk update && apk --no-cache add bash gcc libc-dev make libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev mariadb-dev build-base jpeg-dev zlib-dev

copy . .

copy django_preparation_entrypoint.sh /opt/app/django_preparation_entrypoint.sh

copy wait-for-it.sh /opt/app/wait-for-it.sh

run pip install --no-cache-dir -r requirements.txt





