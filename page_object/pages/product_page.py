from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def click_button_cart(self):
        button_cart = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_cart.click()

    def get_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        return name_product.text

    def get_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        return price_product.text

    def get_name_product_in_cart(self):
        name_product_in_cart = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_CART)
        return name_product_in_cart.text

    def get_price_product_in_cart(self):
        name_price_in_cart = self.browser.find_element(*ProductPageLocators. PRICE_PRODUCT_IN_CART)
        return name_price_in_cart.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Сообщение об успехе отображается, но не должно"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Сообщение об успехе не исчезает, а должно"

    def click_first_item(self):
        first_item = self.browser.find_elements(*ProductPageLocators.ITEMS)
        first_item[0].click()

    def check_name_product_to_page_product(self, name_product, name_product_in_cart):
        assert name_product == name_product_in_cart

    def check_name_price_to_page_product(self, name_price, name_price_in_cart):
        assert name_price == name_price_in_cart