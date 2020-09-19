from selenium import webdriver
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

    @pytest.fixture
    def browser(self):
        drv = webdriver.Chrome()
        drv.implicitly_wait(10)
        drv.get('https://stepik.org/catalog?language=en')
        login = drv.find_element_by_link_text("Log in")
        login.click()

        name = drv.find_element_by_css_selector('input[name="login"]')
        name.send_keys("alexandr.bezpalyi@gmail.com")
        password = drv.find_element_by_css_selector('input[name="password"]')
        password.send_keys("Fhutjgnthbrc1!")
        submit = drv.find_element_by_css_selector("button.sign-form__btn.button_with-loader")
        submit.click()
        drv.find_element_by_css_selector("div.drop-down__toggler.drop-down-toggler > button.navbar__profile-toggler")
        yield drv
        drv.quit()

    @pytest.mark.parametrize("url", links[:])
    def test_function(self, browser, url):
        browser.get(url)
        answer = math.log(int(time.time()))
        text_area = browser.find_element_by_css_selector("textarea")
        text_area.send_keys(str(answer))

        submit = browser.find_element_by_css_selector("button.submit-submission")
        submit.click()
        result = browser.find_element_by_css_selector("div.attempt__message > div > pre.smart-hints__hint")
        assert result.text == "Correct!"



