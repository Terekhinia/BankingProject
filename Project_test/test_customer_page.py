from .pages.customer_page import CustomerPage
from .pages.data_page import TestUser2



def test_login_user(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    page = CustomerPage(browser)
    page.open(url)
    name = f'{TestUser2.FIRST_NAME} {TestUser2.LAST_NAME}'
    page.search_your_name(name)
    page.click_button_login()
    actual_name = page.get_welcome()
    page.check_welcome(expected_name=name, actual_name=actual_name)