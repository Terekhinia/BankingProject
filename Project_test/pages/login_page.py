from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def click_button_customer_login(self):
        click_button_customer = self.browser.find_element(*LoginPageLocators.BUTTON_CUSTOMMER_LOGIN)
        click_button_customer.click()

    def click_button_bank_manager_login(self):
        click_button_bank_manager = self.browser.find_element(*LoginPageLocators.BUTTON_BANK_MANAGER_LOGIN)
        click_button_bank_manager.click()