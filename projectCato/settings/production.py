from .common import *
from .decouple import config
from .partials.util import get_secret


DEBUG = False
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
ALLOWED_HOSTS = ['*']
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

if get_secret('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    POSTGRES_USER = get_secret('POSTGRES_USER')
    POSTGRES_PASSWORD = get_secret('POSTGRES_PASSWORD')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': 'db',
            'PORT': 5432,
        }
    }
