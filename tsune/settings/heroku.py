from .base import *

if get_env_variable("DATABASE_URL") is not None:
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()