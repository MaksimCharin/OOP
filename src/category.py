from src.product import Product


class Category:
    """Описание класса с категорией товара"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0


    def add_product(self, product: Product):
        """Добавление единичного товара в список товаров"""
        self.__products.append(product)

        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return product_str
