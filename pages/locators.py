from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')



class ProductPageLocators:

    BASKET_ADD = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    EMPTY_BASKET = (By.ID, "content_inner")
    NOT_EMPTY_BASKET = (By.CLASS_NAME, "basket-items")
