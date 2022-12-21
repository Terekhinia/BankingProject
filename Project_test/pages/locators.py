from selenium.webdriver.common.by import By


class BasePageLocators():
    BUTTON_HOME = (By.CSS_SELECTOR, "[ng-click='home()']")

class LoginPageLocators():
    BUTTON_CUSTOMMER_LOGIN = (By.CSS_SELECTOR, "[ng-click='customer()']")
    BUTTON_BANK_MANAGER_LOGIN = (By.CSS_SELECTOR, "[ng-click='manager()']")

class ManagerPageLocators():
    TAB_ADD_CUSTOMMER = (By.CSS_SELECTOR, "[ng-class='btnClass1']")
    TAB_OPEN_ACCOUNT = (By.CSS_SELECTOR, "[ng-class='btnClass2']")
    TAB_CUSTOMMER = (By.CSS_SELECTOR, "[ng-class='btnClass3']")
    PLACEHOLDER_FIRST_NAME = (By.CSS_SELECTOR, "[ng-model='fName']")
    PLACEHOLDER_LAST_NAME = (By.CSS_SELECTOR, "[ng-model='lName']")
    PLACEHOLDER_POST_CODE = (By.CSS_SELECTOR, "[ng-model='postCd']")
    BUTTON_ADD_CUSTOMMER = (By.CSS_SELECTOR, "[class='btn btn-default']")
    BUTTON_PROCESS = (By.XPATH, "//*[text()='Process']")
    PLACEHOLDER_SEARCH_CUSTOMER = (By.CSS_SELECTOR, "[ng-model='searchCustomer']")
    SERCH_CASTOMER_FIRST_NAME = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[1]")
    SERCH_CASTOMER_LAST_NAME = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[2]")
    SERCH_CASTOMER_POST_CODE = (By.XPATH, "//*[contains(@ng-repeat, 'cust in Customers')]/td[3]")
    FILL_CUSTOMER_ID = (By.CSS_SELECTOR, "[class='ng-binding ng-scope']")
    BUTTON_DELETE = (By.CSS_SELECTOR, "[ng-click='deleteCust(cust)']")
    STRING_TABLE_WITH_USERS = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody/tr")

    def choose_customer(self, custom):
        line = f"//option[text()='{custom}']"
        CHOOSE_CUSTOMER = (By.XPATH, line)
        return CHOOSE_CUSTOMER

    def choose_currency(self, currency):
        line = f"//option[text()='{currency}']"
        CHOOSE_CURRENCY = (By.XPATH, line)
        return CHOOSE_CURRENCY

class CustomerPageLocators():
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".btn.btn-default")
    WELCOME = (By.CSS_SELECTOR, '.fontBig.ng-binding')

    def choose_your_name(self, name):
        line = f"//select[@id='userSelect']/option[text()='{name}']"
        CHOOSE_YOUR_NAME = (By.XPATH, line)
        return CHOOSE_YOUR_NAME