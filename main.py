import json
from abc import ABC, abstractmethod


class Category:
    name: str
    description: str
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

    def __repr__(self):
        return f'Category(name={self.name}, description={self.description}, products={self.products})'

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
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError

    @property
    def get_products_list(self, product):
        """Геттер, который выводит список товаров в нужном формате"""
        product_list = []
        for _ in product:
            product_list.append(f"Продукт, {self.__products['price']} руб. Остаток: {self.__products['quantity']} шт.")
        return product_list

    @staticmethod
    def add_product_to_category(product):
        """Метод для приема на вход объекта товара и добавления его в список"""
        product_list = []
        for p in product['products']:
            product_list.append(Product(p['name'], p['description'], p['price'], p['quantity']))
            if p['quantity'] == 0:
                raise ValueError('Товар с нулевым количеством не может быть добавлен')
            break
        Category(product['name'], product['description'], product_list)
        return product_list


class Abstract(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def price(self):
        pass


class MixinConsoleLog:
    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(map(str, self.__dict__.values()))})"


class Product(Abstract, MixinConsoleLog):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__()
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity

        if isinstance(self, self.__class__):
            print(MixinConsoleLog.__repr__(self))

    def __repr__(self):
        return (f'Product(name={self.name}, description={self.description}, '
                f'price={self.price}, quantity={self.quantity})')

    def __str__(self):
        return f'Название продукта: {self.name}, {self.price} руб. Остаток: {len(self)} шт.'

    def __len__(self) -> int:
        """Метод для вывода к-ва товаров на складе"""
        return self.quantity

    def __add__(self, other):
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError('Нельзя складывать товары разных типов')

    @classmethod
    def make_product(cls, **kwagrs):
        return cls(**kwargs)

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


class SmartPhone(Product, MixinConsoleLog):
    def __init__(self, name, description, price, quantity, power: float, model, memory, colour):
        super().__init__(name, description, price, quantity)
        self.power = power
        self.model = model
        self.memory = memory
        self.colour = colour

    def __add__(self, other) -> float:
        """ Метод для определения полной стоимости товаров на складе """
        if type(self) is SmartPhone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError('Нельзя складывать товары разных типов')


class Grass(Product, MixinConsoleLog):
    def __init__(self, name, description, price, quantity, country, growth_time, colour):
        super().__init__(name, description, price, quantity)
        self.power = country
        self.model = growth_time
        self.colour = colour

    def __add__(self, other) -> float:
        """ Метод для определения полной стоимости товаров на складе """
        if isinstance(other, Grass):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
