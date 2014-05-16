from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/vagrant/test-database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
        }
}

DEBUG=True
TEMPLATE_DEBUG=True

INSTALLED_APPS += (
    'django_jenkins',
)

PROJECT_APPS = {
    'cardbox',
    'deckglue',
    'memorize',
    'cardimporter'
}

