from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def wait_for_element(self, locator, timeout: int):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def go_to_site(self):
        return self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found{locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def is_element_except(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_not_except(self, how, what): #можно убрать и ожидать false
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return True
        return False