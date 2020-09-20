from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pytest

import time
import math

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"]


class TestLesson:

    @pytest.mark.parametrize("url", links[:])
    def test_function(self, browser, url):
        # Login
        browser.get("https://stepik.org/catalog?auth=login&language=en")
        nam = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="login"]')))
        nam.send_keys("alexandr.bezpalyi@gmail.com")
        password = browser.find_element_by_css_selector('input[name="password"]')
        password.send_keys("Fhutjgnthbrc1!")
        submit = browser.find_element_by_css_selector("button.sign-form__btn.button_with-loader")
        submit.click()
        # Check if login is successful
        navbar = "div.drop-down__toggler.drop-down-toggler > button.navbar__profile-toggler"
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, navbar)))
        time.sleep(10) # Strange error after login in FF, don't know why :(
        browser.get(url)
        try:
            solve_again = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn.white")))
            solve_again.click()
        except TimeoutException:
            pass
        answer = math.log(int(time.time()))
        css = "textarea.string-quiz__textarea.ember-text-area.ember-view"
        text_area = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
        text_area.send_keys(str(answer))

        submit = browser.find_element_by_css_selector("button.submit-submission")
        submit.click()
        result = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.attempt__message > div > pre.smart-hints__hint")))
        assert result.text == "Correct!"
