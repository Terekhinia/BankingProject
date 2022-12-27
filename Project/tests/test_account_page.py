from Project.tests.conf_test_data import *
from Project.pages.account_page import AccountPage
from Project.base.base_page import BasePage
from Project.data.data_page import *

def test_check_welcom(browser):
    test_logging_user1(browser)
    page = AccountPage(browser)
    actual_name = page.get_welcome()
    name = f'{TestUser1.FIRST_NAME} {TestUser1.LAST_NAME}'
    page.check_welcome(expected_name=name, actual_name=actual_name)

def test_check_logout(browser):
    test_logging_user1(browser)
    page = AccountPage(browser)
    page.click_button_logout()
    page_base = BasePage(browser)
    page_base.webdriverwait_check_url(browser, URL.CUSTOMER)
