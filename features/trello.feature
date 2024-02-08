Feature: Trello API Automation

   Scenario: Create a New Trello Board
    Given a Trello API key API_KEY
    And a Trello API token TRELLO_TOKEN
    When I create a new Trello board with name Testing_assigment_1 and description This_is_a_test_board
    Then the API returns the new board details
    And I print or save the new board details to assigment_1_info.txt