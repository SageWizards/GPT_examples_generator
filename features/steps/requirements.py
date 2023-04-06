import configparser
import os

from behave import given, then, when


@given('the project requirements file "{filename}"')
def given_project_requirements_file(context, filename):
    """Set the project requirements file path"""
    context.req_file = os.path.join(os.getcwd(), filename)


@given('the project setup configuration file "{filename}"')
def given_project_setup_configuration_file(context, filename):
    """Set the project setup configuration file path"""
    context.cfg_file = os.path.join(os.getcwd(), filename)


@when('I check if "{package_name}" is in the requirements or setup.cfg')
def when_check_package_requirements(context, package_name):
    """Check if a package is in the requirements file or setup.cfg"""
    with open(context.req_file, "r") as req_file:
        requirements = req_file.readlines()
        context.package_present = any(package_name in req for req in requirements)

    config = configparser.ConfigParser()
    config.read(context.cfg_file)
    install_requires = config.get("options", "install_requires", fallback="").split(
        "\n"
    )
    context.package_present = (
        context.package_present or package_name in install_requires
    )


@then('"{package_name}" should be present in the requirements or setup.cfg')
def then_verify_package_requirements(context, package_name):
    """Verify that a package is present in the requirements file or setup.cfg"""
    assert (
        context.package_present
    ), f"{package_name} not found in requirements file or setup configuration file"
