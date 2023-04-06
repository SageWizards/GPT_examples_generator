@wip
Feature: basic fastapi configuration
    Scenario: given a fastapi app, when it is started, then it should show the API docs on the http://localhost:4848/docs endpoint
        Given FastAPI is installed
        And I make a call to the fastapi app on "http://localhost:4848/docs"
        Then we should get a response with status code 200
