from .pages.customer_page import CustomerPage
from .pages.data_page import TestUser2
import time


def test_login_user(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    page = CustomerPage(browser, url)
    page.open()
    name = f'{TestUser2.FIRST_NAME} {TestUser2.LAST_NAME}'
    page.search_your_name(name)
    page.click_button_login()
    actual_name = page.get_welcome()
    page.check_welcome(expected_name=name, actual_name=actual_name)