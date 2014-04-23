from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': 'db.sqlite3',
        }
}

INSTALLED_APPS += 'django_jenkins'

PROJECT_APPS = {
    'cardbox',
}