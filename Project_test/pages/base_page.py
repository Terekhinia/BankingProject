from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_home(self):
        btn_home = self.browser.find_element(*BasePageLocators.BUTTON_HOME)
        btn_home.click()

    def check_title(self):
        title = self.browser.title
        assert title == "XYZ Bank"

    def url_check(self, expected_url, actual_url):
        assert actual_url in expected_url

    def names_list_cycle_text(self, line):
        lst = list()
        for element in self.browser.find_elements_by_xpath(line):
            lst.append(element)
        return lst
