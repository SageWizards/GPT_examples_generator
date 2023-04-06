Feature: Verify packages installation

    Scenario: FastAPI is installed
        Given the project requirements file "requirements.txt"
        And the project setup configuration file "setup.cfg"
        When I check if "fastapi" is in the requirements or setup.cfg
        Then "fastapi" should be present in the requirements or setup.cfg

    Scenario: Uvicorn is installed
        Given the project requirements file "requirements.txt"
        And the project setup configuration file "setup.cfg"
        When I check if "uvicorn" is in the requirements or setup.cfg
        Then "uvicorn" should be present in the requirements or setup.cfg
