"""
Модуль содержит методы и локаторы для работы со страницей Manager
"""
from Project.base.base_page import BasePage
from selenium.webdriver.common.by import By

class ManagerPage(BasePage):

    TAB_ADD_CUSTOMMER = (By.XPATH, "//*[@ng-class='btnClass1']")
    TAB_OPEN_ACCOUNT = (By.XPATH, "//*[@ng-class='btnClass2']")
    TAB_CUSTOMMER = (By.XPATH, "//*[@ng-class='btnClass3']")
    PLACEHOLDER_FIRST_NAME = (By.XPATH, "//*[@ng-model='fName']")
    PLACEHOLDER_LAST_NAME = (By.XPATH, "//*[@ng-model='lName']")
    PLACEHOLDER_POST_CODE = (By.XPATH, "//*[@ng-model='postCd']")
    BUTTON_ADD_CUSTOMMER = (By.XPATH, "//*[@class='btn btn-default']")
    BUTTON_PROCESS = (By.XPATH, "//*[text()='Process']")
    PLACEHOLDER_SEARCH_CUSTOMER = (By.XPATH, "//*[@ng-model='searchCustomer']")
    SERCH_CASTOMER_FIRST_NAME = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[1]")
    SERCH_CASTOMER_LAST_NAME = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[2]")
    SERCH_CASTOMER_POST_CODE = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[3]")
    FILL_CUSTOMER_ID = (By.XPATH, "//*[@[class='ng-binding ng-scope']")
    BUTTON_DELETE = (By.XPATH, "//*[@ng-click='deleteCust(cust)']")
    STRING_TABLE_WITH_USERS = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody/tr")

    @staticmethod
    def choose_customer(custom: str):
        """Составление XPATH-запроса для поиска локатора с созданным пользователем из выпадающего списка"""
        line = f"//option[text()='{custom}']"
        CHOOSE_CUSTOMER = (By.XPATH, line)
        return CHOOSE_CUSTOMER

    @staticmethod
    def choose_currency(currency: str):
        """Составление XPATH-запроса для поиска локатора с валютой для созданного пользователя из выпадающего списка"""
        line = f"//option[text()='{currency}']"
        CHOOSE_CURRENCY = (By.XPATH, line)
        return CHOOSE_CURRENCY

    def click_tab_add_customer(self):
        """Кликнуть на вкладку Add Customer"""
        tab_add_customer = self.browser.find_element(self.TAB_ADD_CUSTOMMER)
        tab_add_customer.click()

    def click_tab_open_account(self):
        """Кликнуть на вкладку Open Account"""
        tab_add_customer = self.browser.find_element(self.TAB_OPEN_ACCOUNT)
        tab_add_customer.click()

    def click_tab_customer(self):
        """Кликнуть на вкладку Customers"""
        tab_add_customer = self.browser.find_element(self.TAB_CUSTOMMER)
        tab_add_customer.click()

    def fill_first_name(self, first_name):
        """Заполнение поля 'First Name' на вкладке Add Customer"""
        placeholder_first_name = self.browser.find_element(self.PLACEHOLDER_FIRST_NAME)
        placeholder_first_name.send_keys(first_name)

    def fill_last_name(self, last_name):
        """Заполнение поля 'Last Name' на вкладке Add Customer"""
        placeholder_first_name = self.browser.find_element(self.PLACEHOLDER_LAST_NAME)
        placeholder_first_name.send_keys(last_name)

    def fill_post_code(self, post_code):
        """Заполнение поля 'Post Code' на вкладке Add Customer"""
        placeholder_post_code = self.browser.find_element(self.PLACEHOLDER_POST_CODE)
        placeholder_post_code.send_keys(post_code)

    def click_button_add_customer(self):
        """Кликнуть на кнопку 'Add Customer' во вкладке Add Customer"""
        button_add_customer = self.browser.find_element(self.BUTTON_ADD_CUSTOMMER)
        button_add_customer.click()

    def search_customer_name(self, customer):
        """Кликнуть на выпадающий список 'Customer Name' во вкладке Open Account"""
        choose_customer = self.browser.find_element(self.choose_customer(customer))
        choose_customer.click()

    def search_currency(self, currency):
        """Кликнуть на выпадающий список 'Currency' во вкладке Open Account"""
        choose_customer = self.browser.find_element(self.choose_currency(currency))
        choose_customer.click()

    def click_button_process(self):
        """Кликнуть на кнопку 'Process' во вкладке Open Account"""
        button_add_process = self.browser.find_element(self.BUTTON_PROCESS)
        button_add_process.click()

    def fill_search_customer(self, customer_name):
        """Заполнение поля 'Serch Customer' во вкладке Customers"""
        placeholder_search_customer = self.browser.find_element(self.PLACEHOLDER_SEARCH_CUSTOMER)
        placeholder_search_customer.send_keys(customer_name)

    def get_first_name_customer(self):
        """Получить значение First Name в таблице во вкладке Customers"""
        get_first_name = self.browser.find_element(self.SERCH_CASTOMER_FIRST_NAME)
        return get_first_name.text

    def get_last_name_customer(self):
        """Получить значение Last Name в таблице во вкладке Customers"""
        get_last_name = self.browser.find_element(self.SERCH_CASTOMER_LAST_NAME)
        return get_last_name.text

    def get_post_code_customer(self):
        """Получить значение Post Code в таблице во вкладке Customers"""
        get_post_code = self.browser.find_element(self.SERCH_CASTOMER_POST_CODE)
        return get_post_code.text

    def get_customer_id(self):
        """Получить id созданного пользователя из таблицы во вкладке Customers"""
        customer_id = self.browser.find_element(self.FILL_CUSTOMER_ID)
        return customer_id.text

    @staticmethod
    def check_first_name(expected_first_name, actual_first_name):
        """Сравнение ожидаемого и полученного из таблицы Customer значения First Name"""
        assert expected_first_name == actual_first_name, "Имя созданного тестового пользователя не совпадает с именем в таблице"

    @staticmethod
    def check_last_name(expected_last_name, actual_last_name):
        """Сравнение ожидаемого и полученного из таблицы Customer значения Last Name"""
        assert expected_last_name == actual_last_name, "Фамилия созданного тестового пользователя не совпадает с фамилией в таблице"

    @staticmethod
    def check_post_code(expected_post_code, actual_post_code):
        """Сравнение ожидаемого и полученного из таблицы Customer значения Post Code"""
        assert expected_post_code == actual_post_code, "Почтовый индекс созданного тестового пользователя не совпадает с почтовым индексом в таблице"

    @staticmethod
    def check_customer_id(expected_customer_id, actual_customer_id):
        """Сравнение ожидаемого и полученного из таблицы Customer значения id"""
        assert expected_customer_id == actual_customer_id, "user_id тестового пользователя не совпадает с user_id в таблице"

    def click_delete(self):
        """Кликнуть на кнопку 'Delete' в таблице Customer"""
        button_delete = self.browser.find_element(self.BUTTON_DELETE)
        button_delete.click()

    def get_quantity_string_in_table_customer(self):
        """Получение количества строк в таблице Customer"""
        lst = list()
        for element in self.browser.find_elements(self.STRING_TABLE_WITH_USERS):
            lst.append(element)
        return len(lst)

    @staticmethod
    def check_delete_customer(actual_number):
        """Проверка что строки в таблице нет после удаления"""
        assert actual_number == 0,  "Запись с пользователем не удалена"

