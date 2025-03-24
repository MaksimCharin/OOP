from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Описание класса продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        if quantity == 0:
            raise ValueError("Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")

        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            product_price = self.quantity * self.__price
            other_price = other.quantity * other.__price
            total_price = product_price + other_price
            return total_price
        raise TypeError

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


if __name__ == '__main__':
    product = Product.new_product({'name': 'a', 'description': 'b', 'price': 1, 'quantity': 2})

