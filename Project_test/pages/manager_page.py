from .base_page import BasePage
from .locators import ManagerPageLocators

class ManagerPage(BasePage, ManagerPageLocators):

    def click_tab_add_customer(self):
        tab_add_customer = self.browser.find_element(*ManagerPageLocators.TAB_ADD_CUSTOMMER)
        tab_add_customer.click()

    def click_tab_open_account(self):
        tab_add_customer = self.browser.find_element(*ManagerPageLocators.TAB_OPEN_ACCOUNT)
        tab_add_customer.click()

    def click_tab_customer(self):
        tab_add_customer = self.browser.find_element(*ManagerPageLocators.TAB_CUSTOMMER)
        tab_add_customer.click()

    def fill_first_name(self, first_name):
        placeholder_first_name = self.browser.find_element(*ManagerPageLocators.PLACEHOLDER_FIRST_NAME)
        placeholder_first_name.send_keys(first_name)

    def fill_last_name(self, last_name):
        placeholder_first_name = self.browser.find_element(*ManagerPageLocators.PLACEHOLDER_LAST_NAME)
        placeholder_first_name.send_keys(last_name)

    def fill_post_code(self, post_code):
        placeholder_post_code = self.browser.find_element(*ManagerPageLocators.PLACEHOLDER_POST_CODE)
        placeholder_post_code.send_keys(post_code)

    def click_button_add_customer(self):
        button_add_customer = self.browser.find_element(*ManagerPageLocators.BUTTON_ADD_CUSTOMMER)
        button_add_customer.click()

    def search_customer_name(self, customer):
        choose_customer = self.browser.find_element(*ManagerPageLocators.choose_customer(self, customer))
        choose_customer.click()

    def search_currency(self, currency):
        choose_customer = self.browser.find_element(*ManagerPageLocators.choose_currency(self, currency))
        choose_customer.click()

    def click_button_process(self):
        button_add_process = self.browser.find_element(*ManagerPageLocators.BUTTON_PROCESS)
        button_add_process.click()

    def fill_customer_id(self, browser):
        alert = browser.switch_to.alert
        alert_text = alert.text
        global account_id
        account_id = alert_text.split(': ')[-1]

    def fill_search_customer(self, customer_name):
        placeholder_search_customer = self.browser.find_element(*ManagerPageLocators.PLACEHOLDER_SEARCH_CUSTOMER)
        placeholder_search_customer.send_keys(customer_name)

    def get_first_name_customer(self):
        get_first_name = self.browser.find_element(*ManagerPageLocators.SERCH_CASTOMER_FIRST_NAME)
        return get_first_name.text

    def get_last_name_customer(self):
        get_last_name = self.browser.find_element(*ManagerPageLocators.SERCH_CASTOMER_LAST_NAME)
        return get_last_name.text

    def get_post_code_customer(self):
        get_post_code = self.browser.find_element(*ManagerPageLocators.SERCH_CASTOMER_POST_CODE)
        return get_post_code.text

    def get_customer_id(self):
        customer_id = self.browser.find_element(*ManagerPageLocators.FILL_CUSTOMER_ID)
        return customer_id.text

    def check_first_name(self, expected_first_name, actual_first_name):
        assert expected_first_name == actual_first_name, "Имя созданного тестового пользователя не совпадает с именем в таблице"

    def check_last_name(self, expected_last_name, actual_last_name):
        assert expected_last_name == actual_last_name, "Фамилия созданного тестового пользователя не совпадает с фамилией в таблице"

    def check_post_code(self, expected_post_code, actual_post_code):
        assert expected_post_code == actual_post_code, "Почтовый индекс созданного тестового пользователя не совпадает с почтовым индексом в таблице"

    def check_customer_id(self, expected_customer_id, actual_customer_id):
        assert expected_customer_id == actual_customer_id, "user_id тестового пользователя не совпадает с user_id в таблице"

    def click_delete(self):
        button_delete = self.browser.find_element(*ManagerPageLocators.BUTTON_DELETE)
        button_delete.click()

    def get_quantity_string_in_table_users(self):
        x = BasePage.names_list_cycle_text(self, "//table[@class='table table-bordered table-striped']/tbody/tr")
        return len(x)

    def check_delete_user(self, actual_number):
        assert actual_number == 0, "Запись с пользователем не удалена"