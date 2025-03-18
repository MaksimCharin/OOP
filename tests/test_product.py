import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_new_product(phone):
    assert Product.new_product(phone).name == "Samsung Galaxy S23 Ultra"
    assert Product.new_product(phone).description == "256GB, Серый цвет, 200MP камера"
    assert Product.new_product(phone).price == 180000.0
    assert Product.new_product(phone).quantity == 5


def test_product_price(second_product):
    assert second_product.price == 210000.0


def test_product_price_setter(capsys, second_product):
    new_price = -100
    second_product.price = new_price
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    new_price = 800
    second_product.price = new_price
    assert second_product.price == 800


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product, product2):
    assert product + product2 == 2580000.0

def test_product_add_error(product):
    with pytest.raises(TypeError):
        result = product + 1
