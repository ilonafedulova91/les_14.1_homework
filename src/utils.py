import json

from src.classes import Category, Product


def load_data_from_json(file_path: str):
    """This function loads data from a json file"""
    categories_list = []

    with open(file_path, "r", encoding="utf-8") as file:
        categories = json.load(file)

        for category in categories:
            products = []

            for product in category["products"]:
                product = Product(
                    name=product["name"],
                    description=product["description"],
                    price=product["price"],
                    quantity=product["quantity"],
                )
                products.append(product)

            category = Category(
                name=category["name"],
                description=category["description"],
                products=products,
            )
            categories_list.append(category)

    return categories_list
