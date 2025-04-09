import allure

from demowebshop import app


@allure.parent_suite("demowebshop")
@allure.suite("Корзина")
@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.sub_suite("Добавление товаров в корзину")
@allure.story("Добавление товаров в корзину")
@allure.title("Добавление одного товара в корзину")
def test_add_product_in_cart(authorised_user):
    app.api.add_product_in_cart(product_id = 13, quantity = 3)
    app.cart.open()
    app.cart.cart_should_have_product(product_name = 'Computing and Internet')

