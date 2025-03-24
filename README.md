# Домашняя работа. Введение в ООП.

## Описание:
Созданы классы Product и Category.
Добавлены классы Smartphone и LawnGrass, которые наследуются от класса Product.
Добавлен абстрактный класс BaseProduct.
Добавлен миксин PrintMixin, который при создании объекта распечатывает в консоль информацию о том, 
от какого класса и с какими параметрами был создан объект.
Миксин добавлен в цепочку наследования класса *Product*

Для класса Product определены следующие свойства: 
- название (name), 
- описание (description), 
- цена (price), 
- количество в наличии (quantity).

Для класса Category определены следующие свойства: 
- название (name), 
- описание (description), 
- список товаров категории (products).
- атрибуты, которые хранят в себе количество категорий и количество товаров.

Класс Smartphone наследуется от класса Product и расширен следующими атрибутами: 
- производительность (efficiency),
- модель (model), 
- объем встроенной памяти (memory).
- цвет (color)

Класс LawnGrass наследуется от класса Product и расширен следующими атрибутами:
- производитель (country),
- срок прорастания (germination_period),
- цвет (color)

Абстрактный класс BaseProduct является родительским для классов продуктов и содержит в себе общий метод для всех классов

```
    @abstractmethod
    def __add__(self, other) -> float:
        pass
```
Добавлена обработка возможных исключений. На функционал написаны тесты.

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
Пример тестов для проверки класса Smartphone:

```
def test_smartphone_product_init(smartphone_product_1):
    assert smartphone_product_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product_1.price == 180000.0
    assert smartphone_product_1.quantity == 5
    assert smartphone_product_1.efficiency == 95.5
    assert smartphone_product_1.model == "S23 Ultra"
    assert smartphone_product_1.memory == 256
    assert smartphone_product_1.color == "Серый"


def test_smartphone_product_add(smartphone_product_1, smartphone_product_2):
    assert smartphone_product_1 + smartphone_product_2 == 2580000.0


def test_smartphone_product_add_error(smartphone_product_1, lawn_grass_product_1):
    with pytest.raises(TypeError):
        result = smartphone_product_1 + lawn_grass_product_1
```
Пример тестов для проверки миксина PrintMixin:
```
def test_print_mixin(capsys):
    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
```