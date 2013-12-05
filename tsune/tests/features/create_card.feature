Feature: Create Card
  In order to have something to learn
  As a User
  I want to create a card in a given deck
  
  Background:
    Given I am logged in
    And the deck "Datenbanken" exists in my portfolio
  
  Scenario: Create a new card in a specified deck
    Given the card "foo?" does not exist in the deck "Datenbanken"
    When I create a card in the deck "Datenbanken" with the fields:
      | front  | back |
      | "foo?" |"bar" |
    Then the card "foo?" exists in the deck "Datenbanken"
    And the card has the field "back" set to "bar"
    And I see the message "Karte wurde erstellt"
  
  Scenario: A card with this front already exists in the specified deck
    Given the card "foo?" exists in the deck "Datenbanken"
    When I create a card in the deck "Datenbanken" with the field "front" set to "foo?"
    Then I see the message "Diese Karte existiert bereits"
    
  Scenario: Required field was left blank
    When I create a card in the deck "Datenbanken" with the field "<field_name>" left blank
    Then I see the message "<field_name> muss angegeben sein"
  
  Examples:
    | field_name |
    | front      |
    | back       |
