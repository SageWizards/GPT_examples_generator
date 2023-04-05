@wip
Feature: basic fastapi configuration
    Scenario: given a fastapi app, when it is started, then it should be running on port 4848
        Given I have fastapi installed
        And I make a call to the fastapi app on "localhost:4848/"
        Then we should get a response with status code 200

    Scenario: given a fastapi app, when it is started, then it should show the API docs
        Given I have fastapi installed
        And I make a call to the fastapi app on "localhost:4848/docs"
        Then we should get a response with status code 200
