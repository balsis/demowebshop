import allure

from demowebshop import app


@allure.parent_suite("demowebshop")
@allure.suite("Корзина")
@allure.epic("demowebshop")
@allure.feature("Корзина")
@allure.sub_suite("Добавление товаров в корзину")
@allure.story("Добавление товаров в корзину")
class TestAddProductInCart:

    @allure.title("Добавление одного товара в корзину")
    def test_add_one_product_in_cart(self, authorised_user):
        app.api.add_product_in_cart(product_id = 13)
        app.cart.open()
        app.cart.cart_should_have_product('Computing and Internet')

    @allure.title("Добавление нескольких позиций одного товара в корзину")
    def test_add_one_product_with_some_quantity_in_cart(self, authorised_user):
        app.api.add_product_in_cart(product_id = 13, quantity = 3)
        app.cart.open()
        app.cart.cart_should_have_product_with_quantity(product_name = 'Computing and Internet', quantity = 3)

    @allure.title("Добавление нескольких товаров в корзину")
    def test_add_few_products_in_cart(self, authorised_user):
        app.api.add_product_in_cart(product_id = 13)
        app.api.add_product_in_cart(product_id = 45)
        app.cart.open()
        app.cart.cart_should_have_products(['Computing and Internet', 'Fiction'])
