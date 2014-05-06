Feature: Edit Deck
  In order to change the name or attributes of a deck
  As a User
  I want to edit a deck
  
  Background:
    Given I am logged in as "testuser"
    And the deck "Datenbanken" exists in my portfolio
    And I see the edit deck dialog
    
  Scenario: Change the name of a deck
    Given the deck "Moderne Datenbanken" does not exist in my portfolio
    When I change the value of the field "name" to "Moderne Datenbanken"
    Then the deck has the name "Moderne Datenbanken"
    
  Scenario: A deck with that name already exists
    Given the deck "Moderne Datenbanken" exists in my portfolio
    When I change the value of the field "name" to "Moderne Datenbanken"
    Then I see the message "Ein Stapel mit diesem Namen existiert bereits"
