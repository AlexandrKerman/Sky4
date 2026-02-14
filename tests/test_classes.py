def test_product(product_obj):
    assert product_obj.name == "product_1"
    assert product_obj.description == "Some product 1 description"
    assert product_obj.price == 50.90
    assert product_obj.quantity == 4


def test_category(category_obj):
    assert category_obj.name == "category_1"
    assert category_obj.description == "Some category 1 description"
    assert category_obj.products == []
    assert category_obj.product_count == 0
    assert category_obj.category_count == 1
