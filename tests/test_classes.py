from unittest.mock import patch

from src import classes


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
    assert len(category_obj.products) == 1

    category_obj.add_product(product_obj)
    assert category_obj.product_objects[0].name == "product_1"
    assert len(category_obj.products) == 2
