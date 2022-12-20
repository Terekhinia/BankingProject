from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_SEE_BASKET = (By.XPATH, '//a[contains(text(),"Посмотреть корзину")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    SECTION_ALLPRODUCTS = (By.XPATH, '//a[contains(text(),"Все товары")]')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    FIELD_EMAIL = (By.NAME, "registration-email")
    FIELD_PASSWORD1 = (By.NAME, "registration-password1")
    FIELD_PASSWORD2 = (By.NAME, "registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.XPATH, '//*[@user_id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    NAME_PRODUCT_IN_CART = (By.XPATH, '//*[@user_id="messages"]/div[1]/div/strong')
    PRICE_PRODUCT_IN_CART = (By.XPATH, '//*[@user_id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@user_id="messages"]/div[1]/div')
    ITEMS = (By.CLASS_NAME, "row")

class BasketPageLocators():
    STATUS_BASKET = (By.XPATH, '//p[contains(text(),"Ваша корзина пуста")]')