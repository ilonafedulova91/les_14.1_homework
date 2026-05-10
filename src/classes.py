from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """The abstract base class"""

    @abstractmethod
    def __str__(self):
        pass


class ReprMixin:
    """A mixin that provides __repr__ method"""

    def __init__(self, *args, **kwargs):
        print(f"Был создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


class Product(ReprMixin, BaseProduct):
    """This class represents a product"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input("Цена снижается. Подтвердить? (y/n): ")
            if answer.lower() != "y":
                return

        self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать разные типы продуктов")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data: dict, products: list = None):
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        if products:
            for product in products:
                if product.name == name:
                    product.quantity += quantity

                    if price > product.price:
                        product.price = price

                    return product

        return cls(name, description, price, quantity)


class Category(BaseProduct):
    """This class represents a category"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только продукты")
            if product.quantity == 0:
                raise ZeroQuantityError("Нельзя добавить товар с нулевым количеством")

        except ZeroQuantityError as e:
            print(e)

        except TypeError as e:
            print(e)

        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        return self.__products

    @property
    def products_str(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def __str__(self):
        total_amount = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_amount} шт."

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0


class CategoryIterator:
    """This class represents a category iterator"""

    def __init__(self, category: Category):
        self.__products = category.products
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__products):
            result = self.__products[self.__index]
            self.__index += 1
            return result
        raise StopIteration


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Order(BaseProduct):
    """This class represents an order"""

    def __init__(self, product: Product, quantity: int):
        try:
            if not isinstance(product, Product):
                raise TypeError("В заказ можно передать только Product")
            if product.quantity == 0:
                raise ZeroQuantityError("Нельзя создать заказ с нулевым товаром")

        except Exception as e:
            print(e)
            raise

        else:
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity
        finally:
            print("Обработка создания заказа завершена")

    def __str__(self):
        return f"Заказ: {self.product.name}, {self.quantity} шт. на сумму {self.total_price} руб."


class ZeroQuantityError(Exception):
    """This class represents a zero quantity error"""

    pass
