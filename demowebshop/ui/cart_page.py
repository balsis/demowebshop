import allure
from selene import browser, have

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

    @allure.step("Проверка, что корзина пуста")
    def cart_should_be_empty(self):
        browser.element('.page-body').should(have.text('Your Shopping Cart is empty!'))

    @allure.step("В корзине есть продукты {product_name_1} и {product_name_2)")
    def cart_should_have_products(self, product_name_1, product_name_2):
        browser.all('.cart-item-row').first.should(have.text(product_name_1))
        browser.all('.cart-item-row').second.should(have.text(product_name_2))
