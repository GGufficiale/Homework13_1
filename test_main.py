import pytest
from main import Category
from main import Product


@pytest.fixture
def product1():
    return Product('топ', 'для занятия спортом', 599, 10)


@pytest.fixture
def product2():
    return Product('топ2', 'для занятия спортом2', 599, 10)


@pytest.fixture
def category_object(product1, product2):
    """Тест получает на вход класс Category для удобства дальнейшей работы"""
    return Category('одежда', 'для спорта',
                    [product1, product2])


def test_init_category(category_object, product1, product2):
    """
    Тест проверяет корректность инициализации объектов класса Category.
    Также тест считает количество продуктов и категорий.
    """
    assert category_object.name == 'одежда'
    assert category_object.description == 'для спорта'
    assert category_object.products == [product1, product2]
    assert category_object.all_categories == 1
    assert category_object.all_unique_goods == 2


@pytest.fixture
def product_object():
    """Тест получает на вход класс Product для удобства дальнейшей работы"""
    return Product('Одежда', 'для занятия спортом', 599, 10)


def test_init_product(product_object):
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product_object.name == 'Одежда'
    assert product_object.description == "для занятия спортом"
    assert product_object.price == 599
    assert product_object.quantity == 10
