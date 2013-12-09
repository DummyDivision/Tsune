from lettuce import step,world,before,after
from pyvirtualdisplay import Display
from splinter import Browser

@before.all
def start_browser():
    # Prepare webdriver and virtual display for headless browser.
    print "Prepare virtual display..."
    world.display = Display(visible=0, size=(800, 600))
    world.display.start()
    print "Fire up headless browser..."
    world.browser = Browser()

    # django_url cannot be used to refer to tsune_root as django
    # integration is faulty in current lettuce.
    world.tsune_root = 'http://127.0.0.1:8000'

@after.all
def quit_browser(total):
    print "Gracefully quit headless browser..."
    world.browser.quit()
    world.display.stop()

# User and login related steps.
@step (u'I am on (.*)')
def am_on_page(step, page):
    # Web driver: Check if on page.
    assert False, 'This step must be implemented'

@step(u'I enter "([^"]*)" and "([^"]*)"')
def enter_username_and_password(step, username, password):
    # Web driver: fill in data and hit enter.
    assert False, 'This step must be implemented'

@step(u'"([^"]*)" is the name of a registered user')
def is_the_name_of_registered_user(step, username):
    # Check the db.
    assert False, 'This step must be implemented'

@step(u'user password is set to "([^"]*)"')
def password_is_set_to(step, password):
    # Check db.
    assert False, 'This step must be implemented'
    	
@step(u'user password is wrong')
def password_is_wrong(step):
    # Check db.
    assert False, 'This step must be implemented'

@step(u'I see the message "([^"]*)"')
def see_message(step, message):
    # Web driver: find message on page.
    assert False, 'This step must be implemented'

@step(u'"([^"]*)" is not the name of a registered user')
def user_is_not_registered(step, username):
    # Check db.
    assert False, 'This step must be implemented'

# create card
@step(u'I am logged in')
def am_logged_in(step):
    assert False, "this step must be implemented"

@step(u'the deck "([^"]*)"( already)? exists in my portfolio')
def deck_exists(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'the card "([^"]*)" does not exist in the deck "([^"]*)"')
def card_doesnt_exist_in_deck(step, card, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I create a card in the deck "([^"]*)" with the fields:')
def create_card_in_deck(step, deck):
     # Check db.
     # Re-use other steps!
    assert False, "this step must be implemented"

@step(u'the card "([^"]*)" exists in the deck "([^"]*)"')
def card_exist_in_deck(step, card, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'the card has the field "([^"]*)" set to ([^"]*)')
def card_has_field_set_to(step, field, text):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I create a card in the deck "([^"]*)" with the field "([^"]*)" set to "([^"]*)"')
def create_card_with_field_set_to(step, deck, field, text):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I create a card in the deck "([^"]*)" with the field "([^"]*)" left blank')
def create_card_with_field_left_blank(step, deck, field):
     # Check db.
    assert False, "this step must be implemented"

# Create deck

@step(u'the deck "([^"]*)" does not exist in my portfolio')
def deck_doesnt_exists(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I create the deck "([^"]*)"')
def create_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I go to (.*)')
def go_to_page(step, page):
     # Web driver: Got to page
    assert False, "this step must be implemented"

@step(u'I see the deck "([^"]*)" in my portfolio')
def see_deck_in_portfolio(step, deck):
    # Web driver.
    assert False, "this step must be implemented"

# Edit card

@step(u'I see the (.*) dialog')
def see_dialog(step, dialog):
     # Web driver: check if on dialog.
    assert False, "this step must be implemented"

@step(u'I change the value of the field "([^"]*)" to "([^"]*)"')
def change_value_of_field(step, field_name, new_value):
     # Check db.
    assert False, "this step must be implemented"

@step(u'the card has the field "([^"]*)" set to "([^"]*)"')
def field_set_to_value(step, field_name, new_value):
     # Check db.
    assert False, "this step must be implemented"

# Edit deck

@step(u'I change the value of the field "([^"]*)" to "([^"]*)"')
def change_value_of_field(step, field, new_value):
     # Check db.
    assert False, "this step must be implemented"

@step(u'the deck has the name "([^"]*)"')
def deck_has_the_name(step, newname):
     # Check db.
    assert False, "this step must be implemented"

# Learn deck
@step(u'there are ([0-9]+) or more unlearned cards in the deck "([^"]*)"')
def unlearned_cards_in_deck(step, number, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I enter the learning dialog for the deck "([^"]*)"')
def enter_learning_dialog_for_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I see the (.*?) of the (.*)')
def see_view_of_dbobject(step, view, dbobject):
    # Web driver: See if the view of the dbobject is shown right now.
    assert False, "this step must be implemented"

@step(u'there are ([0-9]+) unlearned cards in the deck "([^"]*)"')
def unlearned_cards_in_deck(step, number, deck):
     # Check db.
    assert False, "this step must be implemented"


@step(u'I am in the learning dialog for the deck "([^"]*)"')
def in_learning_dialog_for_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I rate this card "([^"]*)"')
def rate_card(step, rating):
     # Check db.
    assert False, "this step must be implemented"

@step(u'the card is rescheduled according to the rating "([^"]*)"')
def card_is_rescheduled_according_to_ranking(step, rating):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I click the button "[^"]*"')
def click_button(step, button):
    # Web driver: find message on page.
    assert False, "this step must be implemented"
