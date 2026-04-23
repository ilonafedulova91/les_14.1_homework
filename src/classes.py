class Product:
    """This class represents a product"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        if not isinstance(other, Product):
            return NotImplemented
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


class Category:
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
        self.__products.append(product)
        Category.product_count += 1

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
