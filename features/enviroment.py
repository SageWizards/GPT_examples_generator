from behave import fixture
from fastapi.testclient import TestClient

from src.gpt_examples_generator.app import app


@fixture(name="examples_generator")
def before_all(context, scenario):
    context.client = TestClient(app)
