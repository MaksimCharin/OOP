from src.product import Product


class Smartphone(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, self.__class__):
            product_price = self.quantity * self.price
            other_price = other.quantity * other.price
            total_price = product_price + other_price
            return total_price
        raise TypeError


if __name__ == '__main__':
    smart = Smartphone.new_product(
        {"name": "Samsung Galaxy S23 Ultra",
         "description": "256GB, Серый цвет, 200MP камера",
         "price": 180000.0,
         "quantity": 5,
         "efficiency": 95.5,
         "model": "S23 Ultra",
         "memory": 256,
         "color": "Серый"
         })
