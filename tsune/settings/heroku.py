from .base import *

get_env_variable("DATABASE_URL")

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Static asset configuration
STATIC_ROOT = 'staticfiles'