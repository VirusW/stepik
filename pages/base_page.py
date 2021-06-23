class BasePage():

    def __init__(self, browser, url):
        self.driver = browser
        self.url = url

    def open(self):
        self.driver.get(self.url)

