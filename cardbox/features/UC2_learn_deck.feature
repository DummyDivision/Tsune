Feature: Learn Deck
  In order to remember my stuff
  As a User
  I want to learn a deck
  
  Background:
    Given I am logged in as "testuser"
    And the deck "Datenbanken" exists in my portfolio
    
  Scenario: Enter learning dialog if there are unlearned cards
    Given there are 1 or more unlearned cards in the deck "Datenbanken"
    When I enter the learning dialog for the deck "Datenbanken"
    Then I see the front of the first unlearned card
    
  Scenario: Enter the learning dialog if there are no unlearned cards
    Given there are 0 unlearned cards in the deck "Datenbanken"
    When I enter the learning dialog for the deck "Datenbanken"
    Then I see the message "Keine weiteren Karten zu lernen."
    
  Scenario: See the back of a card in the learing dialog
    Given I am in the learning dialog for the deck "Datenbanken"
    And I see the front of the card
    When I click the button "Antwort anzeigen"
    Then I see the back of the card
    
  Scenario: Rate a card in the learning dialog
    Given I am in the learning dialog for the deck "Datenbanken"
    And I see the back of the card
    When I rate this card "<rating>"
    Then the card is rescheduled according to the rating "<rating>"
    And I see the front of the next card
    
  Examples:
    | rating |
    | Leicht |
    | Normal |
    | Schwer |
    
  Scenario: Open edit card dialog from within learning dialog
    Given I am in the learning dialog for the deck "Datenbanken"
    And I see the back of the card
    When I click the button "Bearbeiten"
    Then I see the edit card dialog
