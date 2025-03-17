class Product:
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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            product_price = self.quantity * self.__price
            other_price = other.quantity * other.__price
            total_price = product_price + other_price
            return total_price
        raise TypeError

    @classmethod
    def new_product(cls, product_dict):
        name = product_dict.get("name")
        description = product_dict.get("description")
        price = product_dict.get("price")
        quantity = product_dict.get("quantity")

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
