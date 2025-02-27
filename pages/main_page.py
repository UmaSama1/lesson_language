from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def __init__(self, *args, **kwargs):
            super(MainPage, self).__init__(*args, **kwargs)


    def go_to_cart(self):
        link = self.browser.find_element(By.XPATH, "//a[@href='/en-gb/basket/']")
        link.click()






