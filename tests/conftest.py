import time

import allure
import pytest
from selene import browser
from selene.support import webdriver

from demowebshop import app
from demowebshop.helpers import logger


@pytest.fixture(scope = "function")
def authorised_user(setup_browser):
    with allure.step("Выставление cookies для авторизованного пользователя"):
        auth_cookie = app.api.auth_cookie
        browser.open('https://demowebshop.tricentis.com/')
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
        logger.basic_logger.info(f"Cookie для авторизованного пользователя выставлена: {auth_cookie[:9]}")
        yield browser
        # TODO implement cart clearing via API
        app.cart.remove_all_products_from_cart()


@pytest.fixture(scope = "function", autouse = True)
@allure.step("Инициализация браузера")
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    yield
    browser.quit()
