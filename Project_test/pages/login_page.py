from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    BUTTON_CUSTOMMER_LOGIN = (By.CSS_SELECTOR, "[ng-click='customer()']")
    BUTTON_BANK_MANAGER_LOGIN = (By.CSS_SELECTOR, "[ng-click='manager()']")

    def click_button_customer_login(self):
        click_button_customer = self.browser.find_element(self.BUTTON_CUSTOMMER_LOGIN)
        click_button_customer.click()

    def click_button_bank_manager_login(self):
        click_button_bank_manager = self.browser.find_element(self.BUTTON_BANK_MANAGER_LOGIN)
        click_button_bank_manager.click()