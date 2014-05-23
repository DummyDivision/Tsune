from lettuce.django import django_url
from lettuce import step,world
from cardbox.card_model import Card


# Steps first appearing in UC1 - Create Card.
@step(u'I am logged in as "([^"]*)"')
def am_logged_in(step, username):
    assert world.user_is_authenticated(username), 'User "' + username +'" is not logged in.'

@step(u'the deck "([^"]*)" exists in my portfolio')
def deck_exists(step, deckname):
    # TODO: Nur solche Decks beachten, die auch dem User zugeordnet sind.
    assert world.deck_present(deckname), deckname + ' does not exit in the user portfolio'

@step(u'the card "([^"]*)" does not exist in the deck "([^"]*)"')
def card_doesnt_exist_in_deck(step, cardfront, decktitle):
    card_present = world.card_from_deck_present(cardfront, decktitle)
    assert card_present == False, 'The card ' + cardfront + ' is present in ' + decktitle + '.'

@step(u'When I create a card in the deck "([^"]*)" with the front set to "([^"]*)" and the back set to "([^"]*)"')
def create_card_in_deck_with_front_and_back(step, deckname, cardfront, cardback):
    deck = world.get_deck(deckname)
    card = Card(front=cardfront ,back=cardback, deck=deck)
    card.save()

@step(u'the card "([^"]*)" exists in the deck "([^"]*)"')
def card_exists_in_deck(step, cardfront, decktitle):
     assert world.card_from_deck_present(cardfront, decktitle), cardfront + 'does not exist in ' + decktitle

@step(u'the card has the field "([^"]*)" set to ([^"]*)')
def card_has_field_set_to(step, field, text):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I see the message "([^"]*)"')
def see_message(step, message):
    # Web driver: find message on page.
    assert world.browser.is_text_present(message), 'Expected message was not found.'

@step(u'I create a card in the deck "([^"]*)" with the field "([^"]*)" left blank')
def create_card_with_field_left_blank(step, deck, field):
     # Check db.
    assert False, "this step must be implemented"

# Steps first appearing in UC2 - Learn Deck.

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

@step(u'I click the button "[^"]*"')
def click_button(step, button):
    # Web driver: find message on page.
    assert False, "this step must be implemented"

@step(u'I rate this card "([^"]*)"')
def rate_card(step, rating):
     # Check db.
    assert False, "this step must be implemented"

@step(u'the card is rescheduled according to the rating "([^"]*)"')
def card_is_rescheduled_according_to_ranking(step, rating):
    # Check db.
    assert False, "this step must be implemented"

@step(u'I see the (.*) dialog')
def see_dialog(step, dialog):
    # Web driver: check if on dialog.
    assert False, "this step must be implemented"

# Steps first appearing in UC3 - Edit Card.

@step(u'I create a card in the deck "([^"]*)" with the field "([^"]*)" set to "([^"]*)"')
def create_card_with_field_set_to(step, deck_title, field_name, value):
    #TODO: Create card via the browser.
    deck = world.get_deck(deck_title)
    if field_name == 'front':
        card = Card(front=value ,back='testback', deck=deck)
    elif field_name == 'back':
        card = Card(front='testfront' ,back=value, deck=deck)
    world.context_card = card # Make this card accessible through the context.

@step(u'I change the value of the field "([^"]*)" to "([^"]*)"')
def change_value_of_card_field(step, field_name, new_value):
    card = world.context_card
    if field_name == 'front':
        card.front = new_value
    elif field_name == 'back':
        card.back == new_value
    assert card.save(), "Changes could not be saved"

@step(u'the card has the field "([^"]*)" set to "([^"]*)"')
def field_set_to_value(step, field_name, value):
    card = world.context_card
    if field_name == 'front':
        assert card.front == value
    assert card.back == value

# Steps first appearing in UC4 - Create Deck.

@step(u'I create the deck "([^"]*)"')
def create_deck(step, deck):
     # Check db.
    assert False, "this step must be implemented"

@step(u'I go to (.*)')
def go_to_page(step, page):
    if page in world.page_map.keys():
        url = world.page_map[page]
        world.response = world.browser.visit(django_url(url))

@step(u'I see the deck "([^"]*)" in my portfolio')
def see_deck_in_portfolio(step, deck):
    # Web driver.
    assert False, "this step must be implemented"

# Steps first appearing in UC5 - Edit Deck.

@step(u'the deck "([^"]*)" does not exist in my portfolio')
def deck_doesnt_exists(step, deck):
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

# Steps first appearing in UC6 - Login User.

@step(u'"([^"]*)" is the name of a registered user')
def is_the_name_of_registered_user(step, username):
    user_is_present = world.user_present(username=username)
    assert user_is_present, 'The user ' + username + ' does not exist.'

@step(u'the password of "([^"]*)" is set to "([^"]*)"')
def password_is_set_to(step, username, password):
    user = world.get_user(username)
    password_is_correct = user.check_password(password)
    assert password_is_correct, password + ' is not the password for user ' + username

@step(u'I enter "([^"]*)" and "([^"]*)"')
def enter_username_and_password(step, username, password):
    # Web driver: fill in data and hit enter.
    world.browser.fill("username", username)
    world.browser.fill("password", password)
    world.browser.find_by_value('login').click()

@step (u'I am on (.*)')
def am_on_page(step, page):
    expected_url = ""
    if page in world.page_map.keys():
        expected_url = world.page_map[page]
    assert world.browser.url == django_url(expected_url), 'The url seems to be wrong.'

@step(u'"([^"]*)" is not the name of a registered user')
def is_not_the_name_of_registered_user(step, username):
    user_is_not_present = world.user_present(username=username) == False
    assert user_is_not_present, 'The user ' + username + 'does exist.'