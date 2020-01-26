from python:3.7-alpine

arg DJANGO_ADMIN_USERNAME
arg DJANGO_ADMIN_PASSWORD
arg DJANGO_ADMIN_EMAIL
arg DJANGO_DOMAIN

env APP_HOME = /opt/app

workdir $APP_HOME

RUN apk update && apk add gcc libc-dev make libffi-dev openssl-dev python3-dev \
		libxml2-dev libxslt-dev mariadb-dev build-base jpeg-dev zlib-dev

copy mali mali_project rdc stats django_preparation_entrypoint.sh manage.py requirements.txt $APP_HOME/

run chmod 666 requirements.txt

run pip install --no-cache-dir -r requirements.txt

entrypoint ["django_preparation_entrypoint.sh"]


