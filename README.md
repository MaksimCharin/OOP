# Домашняя работа. Введение в ООП.

## Описание:
Созданы классы Product и Category.

Для класса Product определите следующие свойства: 
- название (name), 
- описание (description), 
- цена (price), 
- количество в наличии (quantity).

Для класса Category определите следующие свойства: 
- название (name), 
- описание (description), 
- список товаров категории (products).
- атрибуты, которые хранят в себе количество категорий и количество товаров.


## Установка:
1. Клонируйте репозиторий:
```
https://github.com/MaksimCharin/OOP.git
```
2. Установите все зависимости, описанные в файле *pyproject.toml*, выполнив команду:
```
poetry install
```

## Использование:

1. С помощью созданного класса Product, мы можем создать экземпляры класса:
```
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
```
2. С помощью созданного класса Category, мы можем создать экземпляры класса:
```
category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
```

## Тестирование:
Тесты проверяют корректность работы Классов.
```
def test_category_init(phone_category, tv_category):
    assert phone_category.name == "Смартфоны"
    assert (
        phone_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert phone_category.name == "Смартфоны"
    assert len(phone_category.products) == 3

    assert phone_category.category_count == 2
    assert tv_category.category_count == 2

    assert phone_category.product_count == 4
    assert tv_category.product_count == 4
```