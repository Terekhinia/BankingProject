import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path='Project/webdrivers/chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()
