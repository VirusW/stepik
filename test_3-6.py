from selenium import webdriver
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
        browser.get('https://stepik.org/catalog?language=en')
        time.sleep(5)
        sel = "a.navbar__auth.navbar__auth_login.st-link.st-link_style_button.ember-link.ember-view"
        login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, sel)))
        login.click()

        nam = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="login"]')))
        nam.send_keys("alexandr.bezpalyi@gmail.com")
        password = browser.find_element_by_css_selector('input[name="password"]')
        password.send_keys("Fhutjgnthbrc1!")
        submit = browser.find_element_by_css_selector("button.sign-form__btn.button_with-loader")
        submit.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                         "div.drop-down__toggler.drop-down-toggler > button.navbar__profile-toggler")))
        browser.get(url)
        answer = math.log(int(time.time()))
        text_area = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
        text_area.send_keys(str(answer))

        submit = browser.find_element_by_css_selector("button.submit-submission")
        submit.click()
        result = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.attempt__message > div > pre.smart-hints__hint")))
        assert result.text == "Correct!"
