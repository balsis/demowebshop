import allure
import pytest
from selene import browser

from demowebshop import app
from demowebshop.data.data import Data
from demowebshop.helpers import logger


@pytest.fixture(scope = "function")
def authorised_user(quit_browser):
    with allure.step("Выставление cookies для авторизованного пользователя"):
        auth_cookie = app.api.auth_cookie
        browser.open(Data.BASE_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
        logger.basic_logger.info(f"Cookie для авторизованного пользователя выставлена: {auth_cookie[:9]}")
        yield browser
        # TODO implement cart clearing via API
        app.cart.remove_all_products_from_cart()


@pytest.fixture(scope = "function", autouse = True)
@allure.step("Инициализация браузера")
def quit_browser():
    yield browser.quit()
