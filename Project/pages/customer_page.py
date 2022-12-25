"""
Модуль содержит методы и локаторы для работы со страницей Customer
"""
from Project.base.base_page import BasePage
from selenium.webdriver.common.by import By

class CustomerPage(BasePage):
    BUTTON_LOGIN = (By.XPATH, "//*[@class = btn.btn-default")
    WELCOME = (By.XPATH, '//*[@class = fontBig.ng-binding')

    def choose_your_name(self, name):
        """Составление XPATH-запроса для поиска локатора с пользователем из выпадающего списка"""
        line = f"//select[@id='userSelect']/option[text()='{name}']"
        CHOOSE_YOUR_NAME = (By.XPATH, line)
        return CHOOSE_YOUR_NAME

    def search_your_name(self, name):
        """Выбор пользователя из выпадающего списка

        Args:
            name: имя/фамилия пользователя. Пример "Harry Potter"
        """
        your_name = self.find_element(self.choose_your_name(name))
        your_name.click()

    def click_button_login(self):
        """Клик по кнопке - Login"""
        button_login = self.find_element(self.BUTTON_LOGIN)
        button_login.click()

    def get_welcome(self):
        """Получение текста приветственного сообщения"""
        welcome = self.find_element(self.WELCOME)
        return welcome.text

    @staticmethod
    def check_welcome(expected_name, actual_name):
        """Проверка текста приветственного сообщения"""
        assert expected_name == actual_name, 'Приветственное сообщение не совпадает!'
