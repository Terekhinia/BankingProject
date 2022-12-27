"""
Модуль содержит методы и локаторы для работы с начальной страницей Login
"""
from Project.base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    BUTTON_CUSTOMMER_LOGIN = (By.XPATH, "//*[@ng-click='customer()']")
    BUTTON_BANK_MANAGER_LOGIN = (By.XPATH, "//*[@ng-click='manager()']")

    def click_button_customer_login(self):
        """Кликнуть по кнопке 'Customer Login'"""
        click_button_customer = self.find_element(self.BUTTON_CUSTOMMER_LOGIN)
        click_button_customer.click()

    def click_button_bank_manager_login(self):
        """Кликнуть по кнопке 'Bank Manager Login'"""
        click_button_bank_manager = self.find_element(self.BUTTON_BANK_MANAGER_LOGIN)
        click_button_bank_manager.click()


