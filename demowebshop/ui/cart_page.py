import allure
from selene import browser, have, be

from demowebshop.data.data import Data


class CartPage:
    @allure.step("Открыта страница корзины")
    def open(self):
        browser.open(Data.CART_URL)

    @allure.step("В корзине есть продукт {product_name}")
    def cart_should_have_product(self, product_name):
        browser.element('.cart-item-row').should(have.text(product_name))

    @allure.step("В корзине есть продукт {product_name} в количестве {quantity}")
    def cart_should_have_product_with_quantity(self, product_name, quantity):
        browser.element('.cart-item-row').should(have.text(product_name))
        browser.element('.qty-input').should(have.value(str(quantity)))

    @allure.step("В корзине есть продукты {product_names}")
    def cart_should_have_products(self, product_names):
        cart_items = browser.all('.cart-item-row')
        for idx, product_name in enumerate(product_names):
            cart_items[idx].should(have.text(product_name))

    @property
    def products_id_in_cart(self):
        """Получение id товаров для использования при очистке корзины"""
        return [element.get_attribute('value') for element in browser.all('input[name=removefromcart]').locate()]

    @staticmethod
    @allure.step("Очистка корзины")
    def remove_all_products_from_cart():
        for element in browser.all('input[name=removefromcart]'):
            element.should(be.clickable).click()
        browser.element('input[name=updatecart]').click()
