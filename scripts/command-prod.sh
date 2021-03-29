#!/bin/sh

python manage.py migrate
python manage.py loaddata initial.json
python manage.py collectstatic --noinput
