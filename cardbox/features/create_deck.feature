Feature: Create Deck
  In order to have a place to add some cards to
  As a User
  I want to create a deck in my portfolio
  
  Background: 
    Given I am logged in
    
  Scenario: Create a new deck in user portfolio
    Given the deck "Datenbanken" does not exist in my portfolio
    When I create the deck "Datenbanken"
    And I go to my portfolio
    Then I see the deck "Datenbanken" in my portfolio
    
  Scenario: Attempt to create a deck in user portfolio that already exists
    Given the deck "Datenbanken" already exists in my portfolio
    When I create the deck "Datenbanken"
    Then I see the message "Deck existiert bereits"
