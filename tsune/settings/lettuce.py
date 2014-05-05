from .ci import *

# Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Lettuce
LETTUCE_SERVER_PORT = 9000

INSTALLED_APPS += ('lettuce.django',)
