from .common import *
from decouple import config
from .partials.util import get_secret


DEBUG = False
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
ALLOWED_HOSTS = ['*']

SECRET_KEY = "tx)9sy7p**md@4^fdps003e15qlkn8(px1=@9)agvi%2u=sdyv"
# SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# if get_secret('DATABASE_URL'):
#     import dj_database_url
#     DATABASES = {
#         'default': dj_database_url.config()
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_FILE_OVERWRITE = False

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
