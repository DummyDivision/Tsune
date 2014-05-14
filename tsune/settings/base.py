from environment import *
from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(2)  # Gets absolute project path for file creation et al

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENCODING': 'UTF-8',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Pa$$w0rd',
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-DE'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'guardian',
    'deckglue',
    'south',
    'social.apps.django_app.default',
    'memorize',
    'authentication',
    'cardbox',
    'markitup',
    'profiles',
    'inplaceeditform',
    'comic',
    'cardimporter',
    'upload',
)

AUTH_PROFILE_MODULE = 'profiles.UserProfile'

# Django sites configuration
SITE_ID = 1

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DEBUG = False

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child('templates')
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tsune.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tsune.wsgi.application'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Settings for user authentication.
LOGIN_URL = '/user/login/'
LOGOUT_URL = '/user/logout/'
LOGIN_REDIRECT_URL = '/cardbox/'

# Settings for guardian
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.dropbox.DropboxOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
ANONYMOUS_USER_ID = -1

# Settings for social auth
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Settings for Markitup
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True, 'extensions': ['cardimporter.markdown_ext.superscript',
                                                                           'cardimporter.markdown_ext.subscript',
                                                                           'cardimporter.markdown_ext.mathjax',
                                                                           'cardimporter.markdown_ext.underline']})
MARKITUP_PREVIEW_FILTER = (
    'markdown.markdown', {'safe_mode': True, 'extensions': ['cardimporter.markdown_ext.superscript',
                                                            'cardimporter.markdown_ext.subscript',
                                                            'cardimporter.markdown_ext.mathjax',
                                                            'cardimporter.markdown_ext.underline']})
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markituptsu'


# InPlaceEdit Settings
INPLACEEDIT_EVENT = "click"

ADAPTOR_INPLACEEDIT = {'markitup': 'profiles.fields.AdaptorMarkItUp'}

# Fancy logic to generate or load SECRET_KEY
if try_env_variable("SECRET_KEY") is None:
    secret_file = PROJECT_DIR.child('settings').child('secrets.py')
    try:
        open(secret_file).read().strip()
    except IOError:
        try:
            import random

            SECRET_KEY = ''.join(
                [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret_temp = "SECRET_KEY = '" + SECRET_KEY + "'"
            secret = file(secret_file, 'w')
            secret.write(secret_temp)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % secret_file)
else:
    SECRET_KEY = get_env_variable("SECRET_KEY")

try:
    from .secrets import *
except ImportError:
    pass

SECRETS_PRESENT = True

# Social Auth: Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SECRETS_PRESENT = get_secret("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", SECRETS_PRESENT)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET, SECRETS_PRESENT = get_secret("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", SECRETS_PRESENT)

# Social Auth: Facebook
SOCIAL_AUTH_FACEBOOK_KEY, SECRETS_PRESENT = get_secret("SOCIAL_AUTH_FACEBOOK_KEY", SECRETS_PRESENT)
SOCIAL_AUTH_FACEBOOK_SECRET, SECRETS_PRESENT = get_secret("SOCIAL_AUTH_FACEBOOK_SECRET", SECRETS_PRESENT)

# Social Auth: Dropbox
SOCIAL_AUTH_DROPBOX_OAUTH2_KEY, SECRETS_PRESENT = get_secret("SOCIAL_AUTH_DROPBOX_OAUTH2_KEY", SECRETS_PRESENT)
SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET, SECRETS_PRESENT = get_secret("SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET", SECRETS_PRESENT)
