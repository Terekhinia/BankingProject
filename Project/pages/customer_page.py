from .base_page import BasePage
from .locators import CustomerPageLocators

class CustomerPage(BasePage, CustomerPageLocators):

    def search_your_name(self, name):
        your_name = self.browser.find_element(*CustomerPageLocators.choose_your_name(self, name))
        your_name.click()

    def click_button_login(self):
        button_login = self.browser.find_element(*CustomerPageLocators.BUTTON_LOGIN)
        button_login.click()

    def get_welcome(self):
        """"""
        welcome = self.browser.find_element(*CustomerPageLocators.WELCOME)
        return welcome.text

    def check_welcome(self, expected_name, actual_name):
        assert expected_name == actual_name