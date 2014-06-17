Feature: Edit Card
  To add information or correct errors
  As a User
  I want to edit a given card
  
  Background:
    Given I am logged in as "testuser"
    And the deck "Datenbanken" exists in my portfolio
    And the card "foo?" exists in the deck "Datenbanken"
    
  Scenario: Change the value of field
    When I change the value of the field "<field_name>" to "<new_value>"
    Then the card has the field "<field_name>" set to "<new_value>"

  Examples:
    | field_name | new_value |
    | back       | barbar    |
    | front      | foofoo?   |
