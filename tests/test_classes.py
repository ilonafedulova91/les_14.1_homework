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


def test_category_count(categories):
    assert Category.category_count == 1


def test_product_count(categories):
    assert Category.product_count == 2


def test_add_product(categories):
    new_product = Product("product_3", "description_3", 1000, 20)

    categories.add_product(new_product)

    assert "product_3" in categories.products


def test_products_str(categories):
    result = categories.products

    assert isinstance(result, str)
    assert "product_1" in result
    assert "100" in result


def test_new_product():
    data = {
        "name": "new_name",
        "description": "new_description",
        "price": 700,
        "quantity": 3,
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "new_name"
    assert product.description == "new_description"


def test_new_product_list_merge():
    product_0 = Product("product_0", "description_0", 100, 5)

    data = {
        "name": "product_0",
        "description": "description_new",
        "price": 700,
        "quantity": 3,
    }

    product = Product.new_product(data, products=[product_0])

    assert product.quantity == 8
    assert product.price == 700


def test_price_setter():
    product = Product("product_0", "description_0", 100, 5)

    product.price = 300

    assert product.price == 300


def test_price_setter_negative():
    product = Product("product_0", "description_0", 100, 5)

    product.price = -100

    assert product.price == 100
