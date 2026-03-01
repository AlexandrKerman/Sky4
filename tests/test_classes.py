from unittest.mock import patch

from src import classes
from src.classes import Category, Product


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
    first_test_product = classes.Product.new_product(pr_data, [category_obj])
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
    print(category_obj.products, "zalupa")
    assert category_obj.products == ("product_1, 50.9 руб. Остаток: 4 шт.\n" "product_1, 50.9 руб. Остаток: 4 шт.")


def test_add(product_obj):
    res = product_obj + product_obj
    assert res == product_obj.price * product_obj.quantity * 2

    res = sum([product_obj])
    assert res == product_obj.price * product_obj.quantity

    res = product_obj + 200
    assert res == product_obj.price * product_obj.quantity + 200

    res = 200 + product_obj
    assert res == product_obj.price * product_obj.quantity + 200


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

