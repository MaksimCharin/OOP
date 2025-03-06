from src.category import Category
from src.product import Product


def test_category_init(phone_category, tv_category):
    assert phone_category.name == "Смартфоны"
    assert (
        phone_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert phone_category.name == "Смартфоны"
    assert len(phone_category.products_in_list) == 3

    assert phone_category.category_count == 2
    assert tv_category.category_count == 2

    assert phone_category.product_count == 4
    assert tv_category.product_count == 4


def test_category_and_product():

    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Описание смартфонов", [product1, product2, product3])

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert Category.category_count == 1
    assert Category.product_count == 3

    expected_products_str = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert category.products == expected_products_str

    assert category.products_in_list == [product1, product2, product3]

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category.add_product(product4)

    assert Category.product_count == 4
    expected_products_str += "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    assert category.products == expected_products_str

    new_product_dict = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    new_product = Product.new_product(new_product_dict)

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

    new_product.price = 800
    assert new_product.price == 800

    new_product.price = -100
    assert new_product.price == 800