import pytest
from main import Category
from main import Product


@pytest.fixture
def category_object():
    """Тест получает на вход класс Category для удобства дальнейшей работы"""
    return Category('Шоколад', 'Вкусный', ["Риттер Спорт", "Щедрая душа"])


def test_init_category(category_object):
    """
    Тест проверяет корректность инициализации объектов класса Category.
    Также тест считает количество продуктов и категорий.
    """
    assert category_object.name == 'Шоколад'
    assert category_object.description == 'Вкусный'
    assert category_object.products == ["Риттер Спорт", "Щедрая душа"]


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
