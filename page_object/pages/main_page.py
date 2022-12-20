from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def select_section_allproducts(self):
        section_allproducts = self.browser.find_element(*MainPageLocators.SECTION_ALLPRODUCTS)
        section_allproducts.click()

