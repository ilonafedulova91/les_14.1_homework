# Проект: Классы Product и Category

## Описание

Проект реализует систему управления товарами и категориями с использованием ООП:

- базовый класс `Product`
- наследники: `Smartphone`, `LawnGrass`
- класс `Category`
- итератор `CategoryIterator`

Добавлена поддержка:
- инкапсуляции
- наследования
- перегрузки операторов
- строкового представления
- валидации данных

---

## Структура проекта

- `Product` — класс товара  
- `Category` — класс категории товаров
- `LawnGrass` — газонная трава  
- `Category` — категории товаров  
- `CategoryIterator` — итератор по товарам  
- `load_data_from_json` — функция загрузки данных из JSON  
- `tests/` — тесты (pytest)

---

## Класс Product

### Описание

Класс представляет отдельный товар.

### Атрибуты

- `name: str` — название товара  
- `description: str` — описание товара  
- `price: float` — цена товара  
- `quantity: int` — количество на складе  

### Пример использования

```python
product = Product("iPhone 15", "512GB", 210000.0, 8)
```
## Класс Smartphone (наследник Product)

### Дополнительные атрибуты
- `efficiency: float` — производительность
- `model: str` — модель
- `memory: int` — память
- `color: str` — цвет

## Класс LawnGrass (наследник Product)

### Дополнительные атрибуты
- `country: str` — страна
- `germination_period: str` — срок прорастания
- `color: str` — цвет

## Класс Category

### Описание

Класс представляет категорию товаров.

### Атрибуты экземпляра

- `name: str` - название категории
- `description: str` - описание категории
- `products: list[Product]` -список товаров

### Атрибуты класса

- `category_count: int` - общее количество категорий
- `product_count: int` - общее количество товаров

### Особенности
- При создании новой категории:
    - увеличивается `category_count`
    - увеличивается `product_count` на количество товаров в категории

### Пример использования
```python
category = Category("Смартфоны", "Описание", [product1, product2])
```

## Итератор CategoryIterator
Позволяет перебирать товары категории:
```python
for product in CategoryIterator(category):
    print(product)
```

## Загрузка данных из JSON

### Функция
```python
load_data_from_json(file_path: str) -> list[Category]
```

### Описание
Функция читает JSON-файл и создает объекты классов `Category` и `Product`.

### Пример JSON
```JSON
[
  {
    "name": "Смартфоны",
    "description": "Описание категории",
    "products": [
      {
        "name": "iPhone",
        "description": "512GB",
        "price": 200000.0,
        "quantity": 5
      }
    ]
  }
]
```

### Пример использования
```python
categories = load_data_from_json("data.json")
```

## Тестирование

Для тестирования используется `pytest`.

### Проверяется:
- создание объектов
- работа геттеров/сеттеров
- защита типов
- сложение товаров
- наследование
- итерация

### Запуск тестов
```Bash
pytest
```

## Запуск проекта

Пример запуска основного файла:

```Bash
python main.py
```

## Требования
- Python 3.10+
- pytest (для тестов)