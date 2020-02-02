#!/bin/sh

#Run the makemigrations command of django
echo "Creating and editing tables in the database ..."
python manage.py makemigrations mali rdc

#Run the migration process
echo "Populating data with inital information"
python manage.py migrate

#And then we create finally the superuser defined in the environment file
echo "Creating the super user"
python manage.py initialuser --username $DJANGO_ADMIN_USERNAME --password $DJANGO_ADMIN_PASSWORD --email $DJANGO_ADMIN_EMAIL --no-input

#Running up the server
echo "Starting the server ..."
python manage.py runserver 0.0.0.0:8000
