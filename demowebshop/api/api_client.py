import allure
import requests
from requests import session

from demowebshop import app
from demowebshop.data.data import Data
from demowebshop.helpers import logger


class ApiClient:
    def __init__(self, base_url=Data.BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def build_url(self, path):
        return self.base_url + path

    @property
    def auth_cookie(self):
        url = self.build_url("/login")
        data = {"Email": Data.LOGIN, "Password": Data.PASSWORD, "RememberMe": False}
        response = self.session.post(url = url, data = data, allow_redirects = False)
        logger.log_http_response(response)
        logger.log_http_response_in_allure(response)
        try:
            cookie = response.cookies.get("NOPCOMMERCE.AUTH")
            logger.basic_logger.info(f"Получена авторизационная cookie: {cookie[:9]}...")
            return cookie
        except Exception as e:
            logger.error(f"Ошибка при получении cookie: {e}")
            raise RuntimeError

    @allure.step("Добавление продукта с {product_id} в корзину через API")
    def add_product_in_cart(self, product_id, quantity):
        url = self.build_url(f'/addproducttocart/details/{product_id}/1')
        data = {f'addtocart_{product_id}.EnteredQuantity': {quantity}}
        response = self.session.post(url = url, data = data, allow_redirects = False)
        logger.log_http_response(response)
        logger.log_http_response_in_allure(response)
        return response
