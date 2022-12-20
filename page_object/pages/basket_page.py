from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_status_basket_for_empty(self):
        assert self.is_element_present(*BasketPageLocators.STATUS_BASKET)
