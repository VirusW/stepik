import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_button_add_to_basket_exists(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))
    assert button.tag_name == "button"
    assert button.get_attribute("type") == "submit"
    assert button.text == "Ajouter au panier"
