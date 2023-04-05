import subprocess

import requests
from behave import given, then


@given("I have fastapi installed")
def step_impl(context):
    try:
        subprocess.check_call(["behave", "--version"])
    except subprocess.CalledProcessError:
        assert False, "Behave is not installed"


@given('I make a call to the fastapi app on "localhost:4848/"')
def fastapi_call(context):
    """Make a call to the fastapi app"""
    context.response = requests.get("http://localhost:4848/")


@then("we should get a response with status code 200")
def response_code_200(context):
    """Verify that the response code is 200 OK"""
    assert (
        context.response.status_code == 200
    ), f"Expected status code 200, but got {context.response.status_code}"


@given('I make a call to the fastapi app on "localhost:4848/docs"')
def fastapi_docs_call(context):
    """Make a call to the fastapi app docs"""
    context.response = requests.get("http://localhost:4848/docs")
