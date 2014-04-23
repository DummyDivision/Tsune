import os
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
    raise ImproperlyConfigured(error_msg)

def try_env_variable(var_name):
    """ Get the environment variable or return None """
    try:
        return os.environ[var_name]
    except KeyError:
        return None

def get_secret(secret_name, secret_present):
    """ Get the environment variable and return success """
    result = try_env_variable(secret_name)
    if result is None:
        return None, False
    else:
        return result, secret_present