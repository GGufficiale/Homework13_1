import json


class Category:
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.categories = 0
        self.unique_goods = 0


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


def load_data_from_file():
    """Загрузка данных из файла .json"""
    with open("products.json") as file:
        data = json.load(file)
        product_list = []
        for product in data:
            product_list.append(Category(product['name'], product['description'], product["products"]))
    return product_list
