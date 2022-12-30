"""
Модуль содержит методы и локаторы для работы со страницей Customer
"""
from Project.base.base_page import BasePage
from selenium.webdriver.common.by import By

class CustomerPage(BasePage):
    BUTTON_LOGIN = (By.XPATH, "//*[@class = 'btn btn-default']")

    def choose_your_name(self, name):
        """Составление XPATH-запроса для поиска локатора с пользователем из выпадающего списка"""
        return (By.XPATH, f"//select[@id='userSelect']/option[text()='{name}']")

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


