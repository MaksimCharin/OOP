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
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        self.__products.append(product)

        Category.product_count += 1

    @property
    def products(self):
        product_str = ""

        for product in self.__products:
            product_str += f"{str(product)}\n"

        return product_str

    @property
    def products_in_list(self):
        return self.__products
