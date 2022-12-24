from .base_page import BasePage
from selenium.webdriver.common.by import By

class ManagerPage(BasePage):

    TAB_ADD_CUSTOMMER = (By.CSS_SELECTOR, "[ng-class='btnClass1']")
    TAB_OPEN_ACCOUNT = (By.CSS_SELECTOR, "[ng-class='btnClass2']")
    TAB_CUSTOMMER = (By.CSS_SELECTOR, "[ng-class='btnClass3']")
    PLACEHOLDER_FIRST_NAME = (By.CSS_SELECTOR, "[ng-model='fName']")
    PLACEHOLDER_LAST_NAME = (By.CSS_SELECTOR, "[ng-model='lName']")
    PLACEHOLDER_POST_CODE = (By.CSS_SELECTOR, "[ng-model='postCd']")
    BUTTON_ADD_CUSTOMMER = (By.CSS_SELECTOR, "[class='btn btn-default']")
    BUTTON_PROCESS = (By.XPATH, "//*[text()='Process']")
    PLACEHOLDER_SEARCH_CUSTOMER = (By.CSS_SELECTOR, "[ng-model='searchCustomer']")
    SERCH_CASTOMER_FIRST_NAME = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[1]")
    SERCH_CASTOMER_LAST_NAME = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[2]")
    SERCH_CASTOMER_POST_CODE = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[3]")
    FILL_CUSTOMER_ID = (By.CSS_SELECTOR, "[class='ng-binding ng-scope']")
    BUTTON_DELETE = (By.CSS_SELECTOR, "[ng-click='deleteCust(cust)']")
    STRING_TABLE_WITH_USERS = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody/tr")

    @staticmethod
    def choose_customer(custom: str):
        line = f"//option[text()='{custom}']"
        CHOOSE_CUSTOMER = (By.XPATH, line)
        return CHOOSE_CUSTOMER

    @staticmethod
    def choose_currency(currency: str):
        line = f"//option[text()='{currency}']"
        CHOOSE_CURRENCY = (By.XPATH, line)
        return CHOOSE_CURRENCY

    def click_tab_add_customer(self):
        tab_add_customer = self.browser.find_element(self.TAB_ADD_CUSTOMMER)
        tab_add_customer.click()

    def click_tab_open_account(self):
        tab_add_customer = self.browser.find_element(self.TAB_OPEN_ACCOUNT)
        tab_add_customer.click()

    def click_tab_customer(self):
        tab_add_customer = self.browser.find_element(self.TAB_CUSTOMMER)
        tab_add_customer.click()

    def fill_first_name(self, first_name):
        placeholder_first_name = self.browser.find_element(self.PLACEHOLDER_FIRST_NAME)
        placeholder_first_name.send_keys(first_name)

    def fill_last_name(self, last_name):
        placeholder_first_name = self.browser.find_element(self.PLACEHOLDER_LAST_NAME)
        placeholder_first_name.send_keys(last_name)

    def fill_post_code(self, post_code):
        placeholder_post_code = self.browser.find_element(self.PLACEHOLDER_POST_CODE)
        placeholder_post_code.send_keys(post_code)

    def click_button_add_customer(self):
        button_add_customer = self.browser.find_element(self.BUTTON_ADD_CUSTOMMER)
        button_add_customer.click()

    def search_customer_name(self, customer):
        choose_customer = self.browser.find_element(self.choose_customer(customer))
        choose_customer.click()

    def search_currency(self, currency):
        choose_customer = self.browser.find_element(self.choose_currency(currency))
        choose_customer.click()

    def click_button_process(self):
        button_add_process = self.browser.find_element(self.BUTTON_PROCESS)
        button_add_process.click()

    def fill_search_customer(self, customer_name):
        placeholder_search_customer = self.browser.find_element(self.PLACEHOLDER_SEARCH_CUSTOMER)
        placeholder_search_customer.send_keys(customer_name)

    def get_first_name_customer(self):
        get_first_name = self.browser.find_element(self.SERCH_CASTOMER_FIRST_NAME)
        return get_first_name.text

    def get_last_name_customer(self):
        get_last_name = self.browser.find_element(self.SERCH_CASTOMER_LAST_NAME)
        return get_last_name.text

    def get_post_code_customer(self):
        get_post_code = self.browser.find_element(self.SERCH_CASTOMER_POST_CODE)
        return get_post_code.text

    def get_customer_id(self):
        customer_id = self.browser.find_element(self.FILL_CUSTOMER_ID)
        return customer_id.text

    @staticmethod
    def check_first_name(expected_first_name, actual_first_name):
        assert expected_first_name == actual_first_name, "Имя созданного тестового пользователя не совпадает с именем в таблице"

    @staticmethod
    def check_last_name(expected_last_name, actual_last_name):
        assert expected_last_name == actual_last_name, "Фамилия созданного тестового пользователя не совпадает с фамилией в таблице"

    @staticmethod
    def check_post_code(expected_post_code, actual_post_code):
        assert expected_post_code == actual_post_code, "Почтовый индекс созданного тестового пользователя не совпадает с почтовым индексом в таблице"

    @staticmethod
    def check_customer_id(expected_customer_id, actual_customer_id):
        assert expected_customer_id == actual_customer_id, "user_id тестового пользователя не совпадает с user_id в таблице"

    def click_delete(self):
        button_delete = self.browser.find_element(self.BUTTON_DELETE)
        button_delete.click()

    def names_list_cycle_text(self, line):
        lst = list()
        for element in self.browser.find_elements(line):
            lst.append(element)
        return lst

    def get_quantity_string_in_table_users(self):
        x = self.names_list_cycle_text(self.STRING_TABLE_WITH_USERS)
        return len(x)

    @staticmethod
    def check_delete_user(actual_number):
        assert actual_number == 0,  "Запись с пользователем не удалена"