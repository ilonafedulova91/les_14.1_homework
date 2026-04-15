import pytest

from src.classes import Category, Product


@pytest.fixture
def products():
    return [
        Product("product_1", "description_1", 100, 5),
        Product("product_2", "description_2", 500, 10),
    ]


@pytest.fixture
def categories(products):
    Category.category_count = 0
    Category.product_count = 0
    return Category("category_1", "description_1", products)


def test_product_init():
    product = Product("product_1", "description_1", 100, 5)
    assert product.name == "product_1"
    assert product.description == "description_1"
    assert product.price == 100
    assert product.quantity == 5


def test_category_init(categories):
    assert categories.name == "category_1"
    assert categories.description == "description_1"
    assert len(categories.products) == 2


def test_category_count(categories):
    assert Category.category_count == 1


def test_product_count(categories):
    assert Category.product_count == 2
