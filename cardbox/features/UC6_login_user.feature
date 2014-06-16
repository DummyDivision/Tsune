Feature: Sign in
  In order to use Tsune
  As a User
  I want to sign in

  Background:
    Given I go to the admin login page

  Scenario: Sign in is successful
    When I enter "vagrant" and "vagrant"
    Then I am on the admin login page