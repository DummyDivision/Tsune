from .base import *

#SOUTH_TESTS_MIGRATE=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': 'db.sqlite3',
        }
}

INSTALLED_APPS += ('django_jenkins',)

PROJECT_APPS = {
    'cardbox',
    'deckglue',
    'memorize',
}

