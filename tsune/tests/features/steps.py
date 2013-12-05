from lettuce import *

# User and login related steps.
@step ("I am on the login page")
def on_tsune_homepage(step):
    # Web driver: Go to /user/login/.
    assert False, 'This step must be implemented'

@step(u'I enter "([^"]*)" and "([^"]*)"')
def enter_username_and_password(step, username, password):
    # Web driver: fill in data and hit enter.
    assert False, 'This step must be implemented'

@step('"([^"]*)" is the name of a registered user')
def is_the_name_of_registered_user(step, username):
    # Check the db.
    assert False, 'This step must be implemented'

@step('user password is set to "([^"]*)"')
def password_is_set_to(step, password):
    # Check db.
    assert False, 'This step must be implemented'
    	
@step('I am on the main page')
def see_main_page(step):
    # Web driver: check if on "/"
    assert False, 'This step must be implemented'

@step(u'user password is wrong')
def password_is_wrong(step):
    # Check db.
    assert False, 'This step must be implemented'

@step('I see the message "Sign in fehlgeschlagen: falsches Passwort"')
def see_main_page(step):
    # Web driver: find message on page.
    assert False, 'This step must be implemented'

@step('"([^"]*)" is not the name of a registered user')
def user_is_not_registered(step, username):
    # Check db.
    assert False, 'This step must be implemented'

@step('I see the message "Sign in fehlgeschlagen: User "testuser" existiert nicht"')
def see_main_page(step):
     # Web driver: find message on page.
    assert False, 'This step must be implemented'

# create card
@step('I am logged in')
def im_logged_in(step):
     # Web driver: check if on "/"
    assert False, "this step must be implemented"

@step('the deck "([^"]*)" exists')
def deck_exists(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('the card "([^"]*)" does not exist in the deck "([^"]*)"')
def card_doesnt_exist_in_deck(step, card, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('I create a card in the deck "([^"]*)" with the fields:')
def create_card_in_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('the card "([^"]*)" exists in the deck "([^"]*)"')
def card_exist_in_deck(step, card, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('the card has the field "([^"]*)" set to ([^"]*)')
def card_set_field(step, field, text):
     # Check db.
    assert False, "this step must be implemented"

@step('I see the message "[^"*]"')
def see_message(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"

"""
@step('I see the message "Karte wurde erstellt"')
def see_message_card_created(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"
"""
@step('I create a card in ([^"]*) with the field "([^"]*)" set to ([^"]*)')
def card_has_field_set_to(step, deck, field, text):
     # Check db.
    assert False, "this step must be implemented"
"""
@step('I see the message "Diese Karte existiert bereits"')
def see_message_card_exist_already(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"
"""
@step('I create a card in ([^"]*) with the field "([^"]*)" left blank') ##?
def card_has_field_left_blank(step, deck, field):
     # Check db.
    assert False, "this step must be implemented"

@step('I see the message "<field_name> muss angegeben sein"')
def see_message_left_blank(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"

# Create deck

@step('the deck "([^"]*)" does not exists in my portfolio')
def deck_doesnt_exists(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('I create the deck "([^"]*)"')
def create_card_in_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('go to my portfolio')
def card_exist_in_deck(step):
     # Web driver: check if on portfolio.
    assert False, "this step must be implemented"

@step('I see the deck "[^"*]" in my portfolio')
def see_message(step):
    # Web driver.
    assert False, "this step must be implemented"

@step('the deck "([^"]*)" does already exist in my portfolio')
def deck_exist_in_portfolio(step, deck):
     # Check db.
    assert False, "this step must be implemented"

"""
@step('I see the message "Dieses Deck existiert bereits"')
def see_message_deck_exist_already(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"
"""

# Edit card
@step('I see the edit card dialog')
def see_edit_card_dialog(step):
     # Web driver: check if on "edit card dialog"
    assert False, "this step must be implemented"

@step('I change the value of the field "<field_name>" to "<new_value>"')
def change_value_of_field(step):
     # Check db.
    assert False, "this step must be implemented"

@step('the card has the field "<field_name>" set to "<new_value>"')
def field_set_to_value(step):
     # Check db.
    assert False, "this step must be implemented"

# Edit deck
@step('I see the edit deck dialog')
def see_edit_deck_dialog(step):
     # Web driver: check if on "edit deck dialog"
    assert False, "this step must be implemented"

@step('I change the value of the field "name" to "([^"]*)"')
def change_value_of_name_field(step,newname):
     # Check db.
    assert False, "this step must be implemented"

@step('the deck has the name "([^"]*)"')
def deck_has_the_name(step, newname):
     # Check db.
    assert False, "this step must be implemented"

@step('I see the error message "Ein Stapel mit diesem Namen existiert bereits"')
def see_error_message_deck_exists(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"

# Learn deck
@step('there are 1 or more unlearned cards in the deck "([^"]*)"')
def unlearned_cards_in_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('I enter the learning dialog for the deck "([^"]*)"')
def enter_learning_dialog_for_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('I see the front of the first unlearned card')
def see_front_of_card(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"


@step('there are 0 unlearned cards in the deck "([^"]*)"')
def unlearned_cards_in_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

"""@step('I will see the message "Keine weiteren Karten zu lernen.')
def see_no_more_cards_to_learn(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented" """

@step(' I am in the learning dialog for the deck "([^"]*)"')
def in_learning_dialog_for_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step('I see the front of a card')
def see_front_of_card(step):
     # Web driver.
    assert False, "this step must be implemented"

@step('I click the button "Antwort anzeigen"')
def click_button_show_answer(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"

@step('I see the back of the card')
def see_back_of_card(step):
     # Web driver.
    assert False, "this step must be implemented"

@step('I rate this card "<rating>"')
def rate_card(step):
     # Check db.
    assert False, "this step must be implemented"

@step('the card is rescheduled according to the rating "<rating>"')
def card_is_rescheduled_according_to_ranking(step):
     # Check db.
    assert False, "this step must be implemented"

@step('I see the front of the next card')
def see_front_next_card(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"

@step('I see the back of the card')
def see_back_of_card(step):
     # Check db.
    assert False, "this step must be implemented"

@step('I click on the button "Bearbeiten"')
def click_button_edit(step):
    # Web driver: find message on page.
    assert False, "this step must be implemented"
