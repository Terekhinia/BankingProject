from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    """Базовый класс для работы с основными методами браузера и элементами"""
    BUTTON_HOME = (By.XPATH, "//*[@ng-click='home()']")

    def __init__(self, browser: EventFiringWebDriver, timeout: int = 10):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, timeout)
        self.browser.implicitly_wait(timeout)

    # def find_element_located(self, link, timeout=5):
    #     WbDrW = WebDriverWait(self.driver, timeout)
    #     return WbDrW.until(EC.presence_of_element_located(link))

    def find_element(self, locator) -> WebElement:
        return self.browser.find_element(by=locator[0], value=locator[1])

    def find_elements(self, locator) -> list[WebElement]:
        return self.browser.find_elements(by=locator[0], value=locator[1])

    def open(self, url):
        """Открыть страницу"""
        self.browser.get(url=url)

    def go_to_home(self):
        """Переход на домашнюю страницу"""
        btn_home = self.find_element(self.BUTTON_HOME)
        btn_home.click()

    def check_title(self):
        """Проверка заголовка страницы"""
        title = self.browser.title
        assert title == "XYZ Bank", "Заголовок страницы не верный"

    @staticmethod
    def check_url(expected_url, actual_url):
        """Проверка url`а текущей страницы"""
        assert actual_url in expected_url, 'Url текущей страницы не совпадает'


    def webdriverwait_check_url(self, url):
        """Проверка url`а текущей страницы с ожиданием"""
        self.wait.until(EC.url_contains(url))

    @staticmethod
    def waiting(sec):
        time.sleep(sec)


