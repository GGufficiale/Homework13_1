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
        self.__products = products

        Category.all_unique_goods += len(set([product.name for product in products]))
        Category.all_categories += 1

    @property
    def products(self):
        return f'{self.__products}'

    @products.setter
    def products(self, products):
        self.__products = products

    @property
    def get_products(self):
        """Геттер, который выводит список товаров в нужном формате"""
        return f"Продукт, {self.__products['price']} руб. Остаток: {self.__products['quantity']} шт."


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

    def __repr__(self):
        return f'Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})'

    @classmethod
    def make_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if price >= 0:
            print('введена некорректная цена')



def load_data_from_file():
    """Загрузка данных из файла .json"""
    with open("products.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    for product in data:
        products_list = []
        for p in product['products']:
            products_list.append(Product(p['name'], p['description'], p['price'], p['quantity']))
        Category(product['name'], product['description'], products_list)
        return products_list


def make_products_list():
    """Загрузка данных из файла .json"""
    with open("products.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    for product in data:
        products_list = []
        for p in product['products']:
            products_list.append(p)

