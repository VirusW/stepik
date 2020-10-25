import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="Chrome", help="specify browser for tests")
    parser.addoption("--language", type=str, help="specify language for testing")

@pytest.fixture
def browser(request):
    browser_name: str = request.config.getoption("browser_name")
    language = request.config.getoption('language')
    if browser_name.lower() == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() in ("mozilla", "firefox", 'ff'):
        fp = FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(f"Tests for {browser_name} are not implemented")
    yield browser
    browser.quit()
