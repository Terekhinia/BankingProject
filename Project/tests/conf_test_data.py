"""
Модуль содержит методы для настройки тестовых данных необходимых для прохождения тестов
"""
from Project.base.base_page import BasePage
from Project.pages.manager_page import ManagerPage
from Project.pages.customer_page import CustomerPage
from Project.data.data_page import TestUser1, URL

def test_create_user1(browser):
    page = ManagerPage(browser)
    page.open(URL.MANAGER)
    page.click_tab_add_customer()
    page.fill_first_name(TestUser1.FIRST_NAME)
    page.fill_last_name(TestUser1.LAST_NAME)
    page.fill_post_code(TestUser1.POST_CODE)
    page.click_button_add_customer()
    page.close_alert()
    page.click_tab_open_account()
    customer_name = f'{TestUser1.FIRST_NAME} {TestUser1.LAST_NAME}'
    page.search_customer_name(customer_name)
    page.search_currency(TestUser1.CURRENCY)
    page.click_button_process()
    page.close_alert()

def test_logging_user1(browser):
    test_create_user1(browser)  # Функция для заведения User1
    page = CustomerPage(browser)
    page_base = BasePage(browser)
    page.open(URL.CUSTOMER)
    page_base.waiting(1)
    name = f'{TestUser1.FIRST_NAME} {TestUser1.LAST_NAME}'
    page.search_your_name(name)
    page.click_button_login()

