from django.core.management import call_command
from django.test.simple import DjangoTestSuiteRunner

from lettuce import before, after, world
from logging import getLogger
from pyvirtualdisplay import Display
from splinter import Browser
from guardian.models import User

logger = getLogger(__name__)
logger.info("Loading the terrain file...")
logger.info("Loading functions and variables for world...")

def user_present(username):
    """ Checks the database if a user for a given username exists.
    """
    if User.objects.filter(username=username).count():
        return True
    return False
world.user_present = user_present

@before.runserver
def setup_database(actual_server):
    world.test_runner = DjangoTestSuiteRunner(interactive=False)
    DjangoTestSuiteRunner.setup_test_environment(world.test_runner)
    world.created_db = DjangoTestSuiteRunner.setup_databases(world.test_runner)
    call_command('syncdb', interactive=False, verbosity=0)
    call_command('migrate', verbosity=0)
    call_command('loaddata', 'LettuceFixtures.json', verbosity=0)

@after.runserver
def teardown_database(actual_server):
    """    This will destroy your test database after all of your tests have executed.
    """
    logger.info("Destroying the test database ...")

    DjangoTestSuiteRunner.teardown_databases(world.test_runner, world.created_db)

@before.all
def start_browser():
    """ Prepare webdriver and virtual display for headless browser.
    """
    logger.info("Prepare virtual display...")
    world.display = Display(visible=0, size=(800, 600))
    world.display.start()
    logger.info("Fire up headless browser...")
    world.browser = Browser()

@after.all
def quit_browser(total):
    """ Destroy headless browser and virtual display.
    """
    logger.info("Gracefully quit headless browser...")
    world.browser.quit()
    world.display.stop()