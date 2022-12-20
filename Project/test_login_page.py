import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.data_page import URL
import time

def test_check_title(browser):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    page = BasePage(browser, url)
    page.open()
    page.check_title()

def test_check_button_home(browser):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    page_base = BasePage(browser, url)
    page_login = LoginPage(browser, url)
    page_login.open()
    page_login.click_button_customer_login()
    time.sleep(0.5)
    url_customer = browser.current_url
    page_base.url_check(url_customer, URL.CUSTOMER)
    page_base.go_to_home()
    url_home = browser.current_url
    page_base.url_check(url_home, URL.HOME)
    page_login.click_button_bank_manager_login()
    time.sleep(0.5)
    url_manager = browser.current_url
    page_base.url_check(url_manager, URL.MANAGER)
    page_base.go_to_home()
    url_home = browser.current_url
    page_base.url_check(url_home, URL.HOME)