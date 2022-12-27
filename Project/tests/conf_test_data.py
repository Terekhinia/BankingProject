"""
Модуль содержит методы для настройки тестовых данных необхожимых для прохождения тестов
"""
from Project.pages.manager_page import ManagerPage
from Project.pages.customer_page import CustomerPage
from Project.data.data_page import *
import time

def test_create_user1(browser):
    page = ManagerPage(browser)
    page.open(URL.MANAGER)
    page.click_tab_add_customer()
    page.fill_first_name(TestUser1.FIRST_NAME)
    page.fill_last_name(TestUser1.LAST_NAME)
    page.fill_post_code(TestUser1.POST_CODE)
    page.click_button_add_customer()
    browser.switch_to.alert.accept()
    page.click_tab_open_account()
    customer_name = f'{TestUser1.FIRST_NAME} {TestUser1.LAST_NAME}'
    page.search_customer_name(customer_name)
    page.search_currency(TestUser1.CURRENCY)
    page.click_button_process()
    browser.switch_to.alert.accept()

def test_logging_user1(browser):
    test_create_user1(browser)  # Функция для заведения User1
    page = CustomerPage(browser)
    page.open(URL.CUSTOMER)
    time.sleep(0.5)  # Не успевает свормироваться переменная поэтому оставил явное ожидание
    name = f'{TestUser1.FIRST_NAME} {TestUser1.LAST_NAME}'
    page.search_your_name(name)
    page.click_button_login()

