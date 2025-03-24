import json
import os

from config import DATA_DIR
from src.category import Category
from src.product import Product

file_path = os.path.join(DATA_DIR, "products.json")


def read_json(path: str) -> list:
    """Получение данных о товарах из json-файла"""
    with open(path, "r", encoding="UTF-8") as products_file:
        products_data = json.load(products_file)
        return products_data


def create_objects_from_json(data):
    """Заполнение классов информацией из файла"""
    categories = []
    for category in data:
        products = []
        for item in category["products"]:
            products.append(Product(**item))
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    raw_data = read_json(file_path)
    print(create_objects_from_json(raw_data))
    prod_data = create_objects_from_json(raw_data)
    print(prod_data[0].description)
