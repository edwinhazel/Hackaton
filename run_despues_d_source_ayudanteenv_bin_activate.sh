#!/bin/bash

sudo nano ./Ayudante/Ayudante/settings.py

echo "Creating Ayudante/static"

sudo pip3 django django-widget-tweaks

python3 ./Ayudante/manage.py makemigrations

python3 /Ayudante/manage.py migrate

sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf
