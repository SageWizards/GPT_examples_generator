import subprocess

import requests
from behave import given, then


@given("FastAPI is installed")
def step_impl(context):
    """Verify that FastAPI is installed."""
    output = subprocess.check_output(["pip", "show", "fastapi"], text=True)
    assert "Name: fastapi" in output, "FastAPI is not installed"


@given('I make a call to the fastapi app on "{url}"')
def fastapi_call(context, url):
    """Make a call to the fastapi app."""
    context.response = requests.get(url)
    assert context.response.status_code == 200


@then("we should get a response with status code {status_code}")
def check_response_code(context, status_code):
    """Verify that the response code is the expected one."""
    assert context.response.status_code == int(
        status_code
    ), "The response code is not the expected one"
