import time
import pytest
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLoginFromMainPage():

    def test_guest_should_see_login_link(self, browser, language):
        url = f"http://selenium1py.pythonanywhere.com/{language}/"
        page = BasePage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser, language):
        url = f"http://selenium1py.pythonanywhere.com/{language}/"
        page = BasePage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, url)
        login_page.should_be_login_page()


def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasePage(browser, url)
    page.open()
    page.go_to_cart()
    url_basket = browser.current_url
    basketpage = BasketPage(browser, url=url_basket )
    basketpage.url_check(url_basket, 'basket/')
    basketpage.check_status_basket_for_empty()
