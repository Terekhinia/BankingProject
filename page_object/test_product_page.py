import pytest
from .pages.product_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

@pytest.mark.test_user
class TestAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, url)
        page.open()
        page.register_new_user()
        base_page = BasePage(browser, url='http://selenium1py.pythonanywhere.com/ru/accounts/profile/')
        base_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        text_name_product = page.get_name_product()
        text_price_product = page.get_price_product()
        page.click_button_cart()
        text_name_product_in_cart = page.get_name_product_in_cart()
        text_price_product_in_cart = page.get_price_product_in_cart()
        page.check_name_product_to_page_product(text_name_product, text_name_product_in_cart)
        page.check_name_price_to_page_product(text_price_product, text_price_product_in_cart)

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    text_name_product = page.get_name_product()
    text_price_product = page.get_price_product()
    page.click_button_cart()
    text_name_product_in_cart = page.get_name_product_in_cart()
    text_price_product_in_cart = page.get_price_product_in_cart()
    page.check_name_product_to_page_product(text_name_product, text_name_product_in_cart)
    page.check_name_price_to_page_product(text_price_product, text_price_product_in_cart )


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.click_button_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.click_button_cart()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasePage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def  test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = ProductPage(browser, url)
    page.open()
    page.click_first_item()
    page.go_to_cart()
    url_basket = browser.current_url # фиксируем url страницы на которую  перешли после клика
    basketpage = BasketPage(browser, url=url_basket)
    basketpage.url_check(url_basket, 'basket/') # проверяем что зафиксированный url соответствует странице корзины
    basketpage.check_status_basket_for_empty()