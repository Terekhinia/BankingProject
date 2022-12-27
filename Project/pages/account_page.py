"""
Модуль содержит методы и локаторы для работы с начальной страницей Account
"""
from Project.base.base_page import BasePage
from selenium.webdriver.common.by import By

class AccountPage(BasePage):

    BUTTON_LOGOUT = (By.XPATH, "//*[@class = 'btn logout']")
    WELCOME = (By.XPATH, "//*[@class = 'fontBig ng-binding']")

    def click_button_logout(self):
        """Клик по кнопке - Logout"""
        button_login = self.find_element(self.BUTTON_LOGOUT)
        button_login.click()

    def get_welcome(self):
        """Получение текста приветственного сообщения"""
        welcome = self.find_element(self.WELCOME)
        return welcome.text

    @staticmethod
    def check_welcome(expected_name, actual_name):
        """Проверка текста приветственного сообщения"""
        assert expected_name == actual_name, 'Приветственное сообщение не совпадает!'
