from unittest.mock import patch

import pytest

from src.classes import Category, CategoryIterator, Product


def test_product(product_obj):
    assert product_obj.name == "product_1"
    assert product_obj.description == "Some product 1 description"
    assert product_obj.price == 50.90
    assert product_obj.quantity == 4


def test_category(category_obj):
    assert category_obj.name == "category_1"
    assert category_obj.description == "Some category 1 description"
    assert category_obj.product_count == 1
    assert category_obj.category_count == 1


def test_new_product(category_obj):
    pr_data = {
        "name": "Samsung Galaxy C23 Ultra",
        "price": 1200,
        "description": "256GB, Серый цвет, 200MP камера",
        "quantity": 2,
    }
    first_test_product = Product.new_product(pr_data, [category_obj])
    assert first_test_product.price == 1200


def test_price(product_obj):
    with patch("builtins.input", return_value="y"):
        product_obj.price = 10
        assert product_obj.price == 10

    with patch("builtins.input", return_value="n"):
        product_obj.price = 5
        assert product_obj.price == 10


def test_add_product(category_obj, product_obj):
    category_obj.add_product(product_obj)
    assert category_obj.product_objects[0].name == "product_1"
    assert category_obj.products == ("product_1, 50.9 руб. Остаток: 4 шт.\n" "product_1, 50.9 руб. Остаток: 4 шт.")

    with pytest.raises(TypeError):
        category_obj.add_product(0)


def test_add(product_obj):
    from src.classes import LawnGrass, Smartphone

    res = product_obj + product_obj
    assert res == product_obj.price * product_obj.quantity * 2

    res = sum([product_obj])
    assert res == product_obj.price * product_obj.quantity

    smartpone1 = Smartphone("smart_1", "smart_desc", 50000, 1, 100, "S1", 512, "blue")
    smartpone2 = Smartphone("smart_2", "smart_desc", 40000, 2, 100, "S2", 1024, "black")
    res = smartpone1 + smartpone2
    assert res == 130000

    grass = LawnGrass("grass_1", "grass_desc", 1000, 2, "Russia", 5, "green")
    with pytest.raises(TypeError):
        res = grass + smartpone2


def test_str_product(product_obj):
    assert str(product_obj) == "product_1, 50.9 руб. Остаток: 4 шт."


def test_str_category(category_obj):
    assert str(category_obj) == "category_1, количество продуктов: 4 шт."


def test_add_categories():
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
            ],
        }
    ]

    result_data = Category.add_categories(data)

    assert result_data[0].name == "Смартфоны"
    assert result_data[0].product_objects[0].name == "Samsung Galaxy C23 Ultra"
    assert result_data[0].products == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert isinstance(result_data[0], Category)
    assert isinstance(result_data[0].products, str)
    assert isinstance(result_data[0].product_objects[0], Product)

    assert Category.add_categories([]) == []


def test_iterator():
    data = Category.add_categories(
        [
            {
                "name": "test_category",
                "description": "Cat_description",
                "products": [
                    {"name": "product_1", "description": "product_desc_1", "price": 1200, "quantity": 2},
                    {"name": "product_2", "description": "product_desc_2", "price": 800, "quantity": 5},
                ],
            },
        ]
    )
    expected = ["product_1, 1200 руб. Остаток: 2 шт.", "product_2, 800 руб. Остаток: 5 шт."]
    for product, ex in zip(CategoryIterator(data[0]), expected):
        assert str(product) == ex


def test_smartphone():
    from src.classes import Smartphone

    smartpone = Smartphone("smart_1", "smart_desc", 50000, 4, 100, "S1", 512, "blue")

    assert str(smartpone) == "smart_1, 50000 руб. Остаток: 4 шт."


def test_printmixin(capsys):
    from src.classes import PrintMixin

    data = Category.add_categories(
        [
            {
                "name": "test_category",
                "description": "Cat_description",
                "products": [
                    {"name": "product_1", "description": "product_desc_1", "price": 1200, "quantity": 2},
                    {"name": "product_2", "description": "product_desc_2", "price": 800, "quantity": 5},
                ],
            },
        ]
    )

    captured = capsys.readouterr()
    assert captured.out == (f"{repr(data[0].product_objects[0])}\n" f"{repr(data[0].product_objects[1])}\n")
