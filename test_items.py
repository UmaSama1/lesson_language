import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_check_button():
    browser = webdriver.Chrome()
    browser.get('https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    button = browser.find_element(By.XPATH, "//button[@value='Добавить в корзину']")
    assert button == button