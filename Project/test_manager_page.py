from .pages.manager_page import ManagerPage
from .pages.data_page import TestUser1
import time


class TestCheckCreateAndDeleteUser1:
    def setup(self):
        self.user_id = None

    def test_check_fill_name_and_post(self, browser):
        url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        page = ManagerPage(browser, url)
        page.open()
        page.click_tab_add_customer()
        page.fill_first_name(TestUser1.FIRST_NAME)
        page.fill_last_name(TestUser1.LAST_NAME)
        page.fill_post_code(TestUser1.POST_CODE)
        page.click_button_add_customer()
        browser.switch_to.alert.accept()

    def test_check_fill_currency(self, browser):
        url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        TestCheckCreateAndDeleteUser1.test_check_fill_name_and_post(self, browser)
        page = ManagerPage(browser, url)
        page.click_tab_open_account()
        customer_name = f'{TestUser1.FIRST_NAME} {TestUser1.LAST_NAME}'
        page.search_customer_name(customer_name)
        page.search_currency(TestUser1.CURRENCY)
        page.click_button_process()
        alert = browser.switch_to.alert
        alert_text = alert.text
        self.user_id = alert_text[-4:]
        browser.switch_to.alert.accept()

    def test_check_customers(self, browser):
        url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        TestCheckCreateAndDeleteUser1.test_check_fill_currency(self, browser)
        page = ManagerPage(browser, url)
        page.click_tab_customer()
        page.fill_search_customer(TestUser1.FIRST_NAME)
        actual_first_name = page.get_first_name_customer()
        actual_last_name = page.get_last_name_customer()
        actual_post_code = page.get_post_code_customer()
        actual_customer_id = page.get_customer_id()
        page.check_first_name(TestUser1.FIRST_NAME, actual_first_name)
        page.check_last_name(TestUser1.LAST_NAME, actual_last_name)
        page.check_post_code(TestUser1.POST_CODE, actual_post_code)
        page.check_customer_id(expected_customer_id=self.user_id, actual_customer_id=actual_customer_id)

    def test_check_delete_user(self, browser):
        url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        TestCheckCreateAndDeleteUser1.test_check_customers(self, browser)
        page = ManagerPage(browser, url)
        page.click_delete()
        actual_number = page.get_quantity_string_in_table_users()
        page.check_delete_user(actual_number)