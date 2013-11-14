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
