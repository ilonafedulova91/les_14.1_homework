import pytest

from src.classes import BaseClass, Category, CategoryIterator, LawnGrass, Order, Product, Smartphone


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

    assert "product_3" in categories.products_str


def test_products_str(categories):
    result = categories.products_str

    assert isinstance(result, str)
    assert "product_1" in result
    assert "100" in result


def test_product__str__():
    product = Product("product_1", "description_1", 100, 5)
    assert str(product) == "product_1, 100 руб. Остаток: 5 шт."


def test_category__str__(categories):
    result = str(categories)
    assert isinstance(result, str)
    assert "category_1" in result
    assert "15" in result


def test_product__add__():
    product_1 = Product("product_1", "description_1", 100, 5)
    product_2 = Product("product_2", "description_2", 500, 10)

    assert product_1 + product_2 == 5500


def test_category_iterator(categories):
    iterator = CategoryIterator(categories)

    products = list(iterator)

    assert len(products) == 2
    assert isinstance(products[0], Product)


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


def test_smartphone_creation():
    phone = Smartphone("phone_1", "description_1", 100, 5, 90.0, "model_1", 128, "black")

    assert isinstance(phone, Smartphone)
    assert isinstance(phone, Product)
    assert phone.name == "phone_1"
    assert phone.price == 100


def test_lawngrass_creation():
    grass = LawnGrass("grass_1", "description_1", 100, 5, "Greece", "10 days", "green")

    assert isinstance(grass, LawnGrass)
    assert isinstance(grass, Product)
    assert grass.country == "Greece"
    assert grass.quantity == 5


def test_add_same_type():
    phone_1 = Smartphone("phone_1", "description_1", 100, 5, 90.0, "model_1", 128, "black")
    phone_2 = Smartphone("phone_2", "description_2", 500, 25, 99.0, "model_2", 256, "white")

    assert phone_1 + phone_2 == 100 * 5 + 500 * 25


def test_add_different_type():
    phone_1 = Smartphone("phone_1", "description_1", 100, 5, 90.0, "model_1", 128, "black")
    grass_1 = LawnGrass("grass_1", "description_1", 100, 5, "Greece", "10 days", "green")

    with pytest.raises(TypeError):
        _ = phone_1 + grass_1


def test_add_wrong_type_product():
    with pytest.raises(TypeError):
        Category.add_product("string")


def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseClass()


def test_mixin_output(capsys):
    Product("product_1", "description_1", 100, 5)
    captured = capsys.readouterr()
    assert "Был создан объект Product с параметрами:" in captured.out


def test_order_creation():
    product_1 = Product("product_1", "description_1", 100, 5)
    order = Order(product_1, 2)

    assert order.total_price == 200
    assert "Заказ" in str(order)


def test_order_invalid():
    with pytest.raises(TypeError):
        Order("not product", 1)
