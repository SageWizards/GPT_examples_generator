import pkg_resources
import requests
from behave import given, then


@given("FastAPI is installed")
def step_impl(context):
    """Verify that FastAPI is installed"""
    try:
        pkg_resources.get_distribution("fastapi")
    except pkg_resources.DistributionNotFound:
        context.fail("FastAPI is not installed")


@given('I make a call to the fastapi app on "{url}"')
def fastapi_call(context, url):
    """Make a call to the fastapi app"""
    context.response = requests.get(url, timeout=10)


@then("we should get a response with status code {status_code}")
def response_code(context, status_code):
    """Verify that the response code is the expected one"""
    expected_code = int(status_code)
    actual_code = context.response.status_code
    assert (
        actual_code == expected_code
    ), f"Expected status code {expected_code}, but got {actual_code}"
