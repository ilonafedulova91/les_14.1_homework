import json

import pytest

from src.classes import Category, Product
from src.utils import load_data_from_json


@pytest.fixture
def json_file(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание смартфонов",
            "products": [
                {
                    "name": "iPhone 15",
                    "description": "512GB",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Samsung",
                    "description": "256GB",
                    "price": 180000.0,
                    "quantity": 5,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Описание телевизоров",
            "products": [
                {
                    "name": "LG TV",
                    "description": "4K",
                    "price": 120000.0,
                    "quantity": 3,
                }
            ],
        },
    ]

    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return file_path


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Product.product_count = 0


def test_load_data_from_json(json_file):
    result = load_data_from_json(json_file)

    assert isinstance(result, list)
    assert all(isinstance(cat, Category) for cat in result)
