from .base_auth_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        super().__init__(url=url, driver=driver)

