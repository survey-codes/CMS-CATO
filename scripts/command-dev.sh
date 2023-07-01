#!/bin/sh

python manage.py migrate
python manage.py loaddata initial templates
python manage.py runserver 0.0.0.0:8000
