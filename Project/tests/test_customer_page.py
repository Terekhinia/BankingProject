from Project.base.base_page import BasePage
from Project.tests.conf_test_data import *
from Project.data.data_page import *

def test_login_user(browser):
    test_create_user1(browser)  # Функция для заведения User1
    page = CustomerPage(browser)
    page.open(URL.CUSTOMER)
    name = f'{TestUser1.FIRST_NAME} {TestUser1.LAST_NAME}'
    page.search_your_name(name)
    page.click_button_login()
    page_base = BasePage(browser)
    page_base.webdriverwait_check_url(browser, URL.ACCOUNT)



