import pytest


def test_lawn_grass_product_init(lawn_grass_product_1):
    assert lawn_grass_product_1.name == "Газонная трава"
    assert lawn_grass_product_1.description == "Элитная трава для газона"
    assert lawn_grass_product_1.price == 500.0
    assert lawn_grass_product_1.quantity == 20
    assert lawn_grass_product_1.germination_period == "7 дней"
    assert lawn_grass_product_1.country == "Россия"
    assert lawn_grass_product_1.color == "Зеленый"


def test_lawn_grass_product_add(lawn_grass_product_1, lawn_grass_product_2):
    assert lawn_grass_product_1 + lawn_grass_product_2 == 16750.0


def test_smartphone_product_add_error(lawn_grass_product_2, smartphone_product_1):
    with pytest.raises(TypeError):
        result = lawn_grass_product_2 + smartphone_product_1
