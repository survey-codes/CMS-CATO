FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/src
ENV DJANGO_SETTINGS_MODULE=projectCato.settings.production
ENV ENVIRONMENT production
ENV DJANGO_SECRET_KEY "tx)9sy7p**md@4^fdps003e15qlkn8(px1=@9)agvi%2u=sdyv"
ENV PORT 8010

RUN apt-get update

# OS dependencies
RUN apt-get install gettext -y; apt-get --assume-yes install binutils libproj-dev gdal-bin python3-gdal

# Setup workdir
RUN mkdir /src
WORKDIR /src

# Python dependencies
COPY requirements.txt /src/
RUN pip install -r /src/requirements.txt

# Test dependencies
COPY test-requirements.txt /src/
RUN pip install -r /src/test-requirements.txt

COPY . /src

# Install assets
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate menus
RUN python manage.py migrate

# run gunicorn
CMD gunicorn --workers 4 --log-level info --timeout 300 --bind 0.0.0.0:$PORT projectCato.wsgi:application
