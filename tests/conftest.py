import pytest

from src import classes


@pytest.fixture()
def product_obj():
    product_1 = {"name": "product_1", "description": "Some product 1 description", "price": 50.90, "quantity": 4}
    return classes.Product(**product_1)


@pytest.fixture()
def category_obj():
    category_1 = {"name": "category_1", "description": "Some category 1 description", "products": []}
    return classes.Category(**category_1)
