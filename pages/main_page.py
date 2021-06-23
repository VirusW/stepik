from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium import webdriver


class MainPage(BasePage):

    def go_to_link_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
