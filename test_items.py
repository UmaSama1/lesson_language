import time
from selenium.webdriver.common.by import By
links = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
import pytest

def test_find_add_to_basket_button(browser):
    browser.get(links)
    time.sleep(5)
    curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    if 'fr' in curr_language:
        time.sleep(30)
        button = browser.find_element(By.XPATH, "//button[@value='Добавить в корзину']")
        assert 'Добавить в корзину' == button
