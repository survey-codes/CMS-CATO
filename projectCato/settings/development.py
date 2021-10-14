from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p)$s^_is49gaum8)yy-hlgkl8+bwc*9lxvlq5_73#9y5qqeln*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


def show_toolbar(request):
    """
    The default callback checks if the IP is internal, but docker's IP
    addresses are not in INTERNAL_IPS, so we force the display in dev mode
    :param request: The intercepted request
    :return: True
    """
    return True


# CORS Config: install django-cors-headers and uncomment the following to allow CORS from any origin
DEVELOPMENT_APPS = [
    'debug_toolbar',
    'corsheaders',
    'graphene_django'
]

INSTALLED_APPS += DEVELOPMENT_APPS

DEVELOPMENT_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE += DEVELOPMENT_MIDDLEWARE

CORS_ORIGIN_ALLOW_ALL = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    'SKIP_TEMPLATE_PREFIXES': (
        'django/forms/widgets/',
        'admin/widgets/',
        'menus/',
        'pipeline/',
    ),
}

GRAPHENE = {
    # "SCHEMA": "infrastucture.dataaccess.main.schema.schema"
    "SCHEMA": "presentation.views.schema.schema"
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# Database for CI/CD github actions
if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
           'ENGINE': 'django.contrib.gis.db.backends.postgis',
           'NAME': 'postgres',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': '127.0.0.1',
           'PORT': '5432',
        }
    }

# Database for development purposes (See docker-compose file)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }

CELERY_BROKER_URL = 'amqp://catocms:catocms@broker:5672/'
