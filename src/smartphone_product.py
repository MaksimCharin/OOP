from src.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) == type(other):
            product_price = self.quantity * self.price
            other_price = other.quantity * other.price
            total_price = product_price + other_price
            return total_price
        raise TypeError
