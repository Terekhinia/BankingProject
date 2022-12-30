from Project.base.base_page import BasePage
from Project.pages.login_page import LoginPage
from Project.data.data_page import URL

def test_check_title(browser):
    page = BasePage(browser)
    page.open(URL.HOME)
    page.check_title()

def test_check_button_home(browser):
    page_base = BasePage(browser)
    page_login = LoginPage(browser)
    page_login.open(URL.HOME)
    page_login.click_button_customer_login()
    page_base.webdriverwait_check_url(URL.HOME)
    page_login.click_button_customer_login()
    page_base.webdriverwait_check_url(URL.CUSTOMER)
    page_base.go_to_home()
    page_base.webdriverwait_check_url(URL.HOME)
    page_login.click_button_bank_manager_login()
    page_base.webdriverwait_check_url(URL.MANAGER)
    page_base.go_to_home()
    page_base.webdriverwait_check_url(URL.HOME)

