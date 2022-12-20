from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert '/login/' in url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), ""

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = 'Qw%#%$#^$&*1234VdFK!'
        indicate_email = self.browser.find_element(*LoginPageLocators.FIELD_EMAIL)
        indicate_email.send_keys(email)
        indicate_password1 = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD1)
        indicate_password1.send_keys(password)
        indicate_password2 = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD2)
        indicate_password2.send_keys(password)
        btn_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        btn_register.click()