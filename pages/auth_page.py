from .base_auth_page import BasePage


class AuthPage(BasePage):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        super().__init__(url=self.url, driver=self.driver)

    def get_url(self):
        return self.driver.current_url

