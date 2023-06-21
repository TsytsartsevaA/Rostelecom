import pytest
from selenium import webdriver
from settings import config
from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(r'drivers\chromedriver.exe')
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def auth_page(driver):
    url = config()['source']['auth_url']
    result = AuthPage(driver=driver, url=url)
    result.open()
    return result


@pytest.fixture(scope='session')
def reg_page(driver):
    url = config()['source']['reg_url']
    result = RegistrationPage(driver=driver, url=url)
    result.open()
    return result