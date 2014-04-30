Feature: Sign in
  In order to use Tsune
  As a User
  I want to sign in

  Background:
    Given I go to the login page

  Scenario: Sign in is successful
    Given "testuser" is the name of a registered user
    And user password is set to "Pa$$w0rd"
    When I enter "testuser" and "Pa$$w0rd"
    Then I am on the main page

  Scenario: Sign in failed because of an incorrect password
    Given "testuser" is the name of a registered user
    And user password is set to "Pa$$w0rd"
    When I enter "testuser" and "WrongPa$$w0rd"
    Then I see the message "Fehler! Benutzername oder Passwort sind ungültig."

  Scenario: Sign in failed because of an invalid username
    Given "NoTestuser" is not the name of a registered user
    When I enter "NoTestuser" and "Pa$$w0rd"
    Then I see the message "Fehler! Benutzername oder Passwort sind ungültig."
