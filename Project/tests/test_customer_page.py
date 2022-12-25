from Project.pages.customer_page import CustomerPage
from Project.data.data_page import *

def test_login_user(browser):
    page = CustomerPage(browser)
    page.open(URL.CUSTOMER)
    name = f'{TestUser2.FIRST_NAME} {TestUser2.LAST_NAME}'
    page.search_your_name(name)
    page.click_button_login()
    actual_name = page.get_welcome()
    page.check_welcome(expected_name=name, actual_name=actual_name)

