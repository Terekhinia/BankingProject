from .base_page import BasePage
from selenium.webdriver.common.by import By

class CustomerPage(BasePage):
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".btn.btn-default")
    WELCOME = (By.CSS_SELECTOR, '.fontBig.ng-binding')

    def choose_your_name(self, name):
        line = f"//select[@id='userSelect']/option[text()='{name}']"
        CHOOSE_YOUR_NAME = (By.XPATH, line)
        return CHOOSE_YOUR_NAME

    def search_your_name(self, name):
        your_name = self.browser.find_element(self.choose_your_name(name))
        your_name.click()

    def click_button_login(self):
        button_login = self.browser.find_element(self.BUTTON_LOGIN)
        button_login.click()

    def get_welcome(self):
        welcome = self.browser.find_element(self.WELCOME)
        return welcome.text

    @staticmethod
    def check_welcome(expected_name, actual_name: str):
        assert expected_name == actual_name, 'Заголовок приветствия не верный'