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
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
