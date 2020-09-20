import time

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="Chrome", help="specify browser for tests")


@pytest.fixture
def browser(request):
    browser_name: str = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        browser = webdriver.Chrome()
    elif browser_name.lower() in ("mozilla", "firefox"):
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"Tests for {browser_name} are not implemented")
    yield browser
    browser.quit()
