Feature: Random comic
  To motivate the user after learning cards
  As a User
  I want to see a random comic when I have no more cards to learn in a deck.

  Background:
    Given I am logged in
    And the deck "Datenbanken" exists in my portfolio
    And I have no more cards to learn in "Datenbanken"
    And I see the deck list

  Scenario: No more cards to learn
    When I try to learn the deck "Datenbanken"
    Then I see a random comic

  Scenario: Problems with XKCD
    When I try to learn the deck "Datenbanken"
    Then I see the tape measure comic