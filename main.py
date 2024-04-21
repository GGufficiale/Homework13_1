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

    def __str__(self):
        return f'Название категории: {self.name}, к-во продуктов: {len(self)} шт.'

    def __len__(self):
        """Метод для вывода к-ва продуктов на складе"""
        return sum([i.count for i in self.__products])

    def __iter__(self):
        return iter(self.__products)

    @property
    def products(self):
        return f'{self.__products}'

    @products.setter
    def products(self, product):
        self.__products += product

    @property
    def get_products(self, product):
        """Геттер, который выводит список товаров в нужном формате"""
        product_list = []
        for p in product:
            product_list.append(f"Продукт, {self.__products['price']} руб. Остаток: {self.__products['quantity']} шт.")
        return product_list

    @staticmethod
    def add_product_to_category(self, product):
        """Метод для приема на вход объекта товара и добавления его в список"""
        product_list = []
        for p in product['products']:
            product_list.append(Product(p['name'], p['description'], p['price'], p['quantity']))
        Category(product['name'], product['description'], product_list)
        return product_list


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

    def __str__(self):
        return f'Название продукта: {self.name}, {self.price} руб. Остаток: {len(self)} шт.'

    def __len__(self) -> int:
        """Метод для вывода к-ва товаров на складе"""
        return self.quantity

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

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
        elif self.price > price:
            input("Если вам ок, нажмите 'y', если нет - 'n'")
            if input == 'y':
                self.price = price
            else:
                print('Цена осталась прежней')

    @price.deleter
    def price(self):
        """Делитер для цены товара"""
        print('Цена осталась прежней')
        self.price = None

    @classmethod
    def make_product(cls, **kwagrs):
        return cls(**kwargs)


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
