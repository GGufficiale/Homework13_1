import json


class Category:
    name: str
    description: str
    products: list
    all_categories = 0
    all_unique_goods = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.all_unique_goods = set

        Category.all_categories += 1


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity


def load_data_from_file():
    """Загрузка данных из файла .json"""
    with open("products.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    product_list = []
    for product in data:
        product_list.append(product)
    return product_list

