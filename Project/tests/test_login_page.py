from Project.base.base_page import BasePage
from Project.pages.login_page import LoginPage
from Project.data.data_page import URL
import time

def test_check_title(browser):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    page = BasePage(browser)
    page.open(url)
    page.check_title()

def test_check_button_home(browser):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    page_base = BasePage(browser)
    page_login = LoginPage(browser)
    page_login.open(url)
    page_login.click_button_customer_login()
    time.sleep(0.5)
    url_customer = browser.current_url
    page_base.check_url(url_customer, URL.CUSTOMER)
    page_base.go_to_home()
    url_home = browser.current_url
    page_base.check_url(url_home, URL.HOME)
    page_login.click_button_bank_manager_login()
    time.sleep(0.5)
    url_manager = browser.current_url
    page_base.check_url(url_manager, URL.MANAGER)
    page_base.go_to_home()
    url_home = browser.current_url
    page_base.check_url(url_home, URL.HOME)

