from django.conf import settings
from django.core.management import call_command
from django.test.simple import DjangoTestSuiteRunner

from lettuce import before, after, world
from logging import getLogger
import os
from pyvirtualdisplay import Display
from splinter import Browser
from guardian.models import User
from cardbox.deck_model import Deck
from cardbox.card_model import Card
import tsune

try:
	from south.management.commands import patch_for_test_db_setup
except:
	pass

logger = getLogger(__name__)
logger.info("Loading the terrain file...")
logger.info("Loading functions and variables for world...")

def get_user(username):
    """ Returns the first user that matches the username.
    """
    matchresult = User.objects.filter(username=username)
    if matchresult.count() > 0:
        return matchresult[0]
world.get_user = get_user

def user_present(username):
    """ Checks the database if a user for a given username exists.
    """
    if User.objects.filter(username=username).count():
        return True
    return False
world.user_present = user_present

def get_card_from_deck(cardfront, decktitle):
    """ Returns the first card that matches the front in a given deck.
    """
    deck = get_deck(decktitle)
    matchresult = Card.objects.filter(front=cardfront, deck=deck.ID)
    if matchresult.count() > 0:
        return matchresult[0]
world.get_card_from_deck = get_card_from_deck

def card_from_deck_present(cardfront, decktitle):
    """ Checks the database if the card with a given fron exists in the given deck.
    """
    if get_card_from_deck(cardfront, decktitle):
        return True
    return False
world.card_from_deck_present = card_from_deck_present

def get_deck(title):
    """ Returns the first deck that matches the username.
    """
    matchresult = Deck.objects.filter(title=title)
    if matchresult.count() > 0:
        return matchresult[0]
world.get_deck = get_deck

def deck_present(title):
    """ Checks the database if a deck for a given deckname exists.
    """
    if get_deck(title):
        return True
    return False
world.deck_present = deck_present

def user_is_authenticated(username):
    """ Returns true if the user for a given username exists and is currently logged in.
    """
    user = get_user(username)
    if user is not None:
        return user.is_authenticated()
    return False
world.user_is_authenticated = user_is_authenticated

# Maps the page names to the actual urls.
world.page_map = {"the login page": "/user/login/",
                  "the main page":  "/cardbox/",
                  "my portfolio":   "/cardbox/"}

@before.runserver
def setup_database(actual_server):
    world.test_runner = DjangoTestSuiteRunner(interactive=False)
    DjangoTestSuiteRunner.setup_test_environment(world.test_runner)
    settings.DEBUG = True
    call_command('syncdb', settings=tsune.settings.ci,interactive=False, verbosity=0)
    call_command('migrate',settings=tsune.settings.ci, interactive=False, verbosity=0)
    call_command('loaddata', 'LettuceFixtures.json', verbosity=0)

@after.runserver
def teardown_database(actual_server):
    """    This will destroy your test database after all of your tests have executed.
    """
    logger.info("Flushing Database...")
    call_command('flush', interactive=False)
    os.system("rm /vagrant/test-database.db")

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
    logger.info("Remove test-database.db...")
