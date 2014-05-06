Feature: Edit Card
  To add information or correct errors
  As a User
  I want to edit a given card
  
  Background:
    Given I am logged in as "testuser"
    And the deck "Datenbanken" exists in my portfolio
    And the card "foo?" exists in the deck "Datenbanken"
    And I see the edit card dialog
    
  Scenario: Change the value of field
    When I change the value of the field "<field_name>" to "<new_value>"
    Then the card has the field "<field_name>" set to "<new_value>"
    
  Examples:
    | field_name | new_value |
    | front      | foofoo?   |
    | back       | barbar    |
    
  Scenario: Try to change a required a field to blank
    When I change the value of the field "<field_name>" to "<new_value>"
    Then I see the message "<field_name> muss angegeben sein"
  
  Examples:
    | field_name | new_value |
    | front      |           |
    | back       |           |
