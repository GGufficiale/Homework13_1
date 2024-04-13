import pytest
from main import Category
from main import Product


@pytest.fixture
def category_object():
    """Тест получает на вход класс Category для удобства дальнейшей работы"""
    return Category(str, str, list)


def test_init_category(category_object):
    """
    Тест проверяет корректность инициализации объектов класса Category.
    Также тест считает количество продуктов и категорий.
    """
    assert category_object.name == str
    assert category_object.description == str
    assert category_object.products == list
    assert category_object.categories >= 0
    assert category_object.unique_goods >= 0


@pytest.fixture
def product_object():
    """Тест получает на вход класс Product для удобства дальнейшей работы"""
    return Product(str, str, float, int)


def test_init_product(product_object):
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product_object.name == str
    assert product_object.description == str
    assert product_object.price == float
    assert product_object.quantity == int

