from .common import *
from .partials.util import get_secret

# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
DEBUG = get_secret('DEBUG') != 'False'
ALLOWED_HOSTS = ['cato-cms.herokuapp.com', '127.0.0.1']
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

PROD_APPS = [
    'storages',
    'graphene_django'
]

INSTALLED_APPS += PROD_APPS

if get_secret('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

USE_S3 = (get_secret('USE_S3') == 'True')

if USE_S3:
    # AWS settings
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None

    # S3 static files
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'projectCato.storage_backends.StaticStorage'

    # S3 media files
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'projectCato.backends.s3boto3.S3Boto3Storage'
