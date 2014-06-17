Feature: Create Card
  In order to have something to learn
  As a User
  I want to create a card in a given deck
  
  Background:
    Given I am logged in as "testuser"
    And the deck "Datenbanken" exists in my portfolio
  
  Scenario: Create a new card in a specified deck
    Given the card "foobar?" does not exist in the deck "Datenbanken"
    When I create a card in the deck "Datenbanken" with the front set to "foobar?" and the back set to "bar"
    Then the card "foobar?" exists in the deck "Datenbanken"
    And the card has the field "back" set to "bar"
