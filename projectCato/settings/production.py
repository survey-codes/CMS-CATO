from .common import *
from .partials.util import get_secret

# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
DEBUG = get_secret('DEBUG') != 'False'
ALLOWED_HOSTS = ['cato-cms.herokuapp.com', '127.0.0.1']
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

PROD_APPS = [
    'storages',
    'graphene_django',
    'djcelery_email'
]

INSTALLED_APPS += PROD_APPS

# TODO: Check NGINX approach for CORS management instead django cors
PROD_MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware'
]

MIDDLEWARE += PROD_MIDDLEWARE

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

##########
# S3 #
##########
USE_S3 = (get_secret('USE_S3') == 'True')

if USE_S3:
    # AWS settings
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_ACL = None

    # S3 static files
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'projectCato.storage_backends.StaticStorage'

    # S3 media files
    MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'projectCato.storage_backends.PublicMediaStorage'

##########
# CELERY #
##########
CELERY_BROKER_USE_SSL = True
CELERY_BROKER_URL = get_secret('CLOUDAMQP_URL')
CELERY_RESULT_BACKEND = get_secret('CLOUDAMQP_URL', 'amqp://')
CELERY_BROKER_POOL_LIMIT = 1
CELERY_BROKER_CONNECTION_TIMEOUT = 10
CELERY_TASK_SERIALIZER = 'json'

CELERY_SEND_TASK_ERROR_EMAILS = True
ADMINS = (
    ('admin', 'daniel.restrepo@unillanos.edu.co'),
)

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
