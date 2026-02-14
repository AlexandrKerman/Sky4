from unittest.mock import mock_open, patch

from src import utils
from src.classes import Category, Product


def test_get_json():
    with patch("builtins.open", mock_open(read_data='[{"key1": 1, "key2": 2}, {"key1": 3, "key2": 4}]')):
        assert utils.get_from_json("data/test.json") == [{"key1": 1, "key2": 2}, {"key1": 3, "key2": 4}]
    with patch("builtins.open", mock_open(read_data="[]")):
        assert utils.get_from_json("data/test.json") == []
    assert utils.get_from_json("data/test") == []


def test_convert_dict_list():
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
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        }
    ]

    result_data = utils.convert_dict_list(data)

    assert utils.convert_dict_list([]) == []
    assert result_data[0].name == "Смартфоны"
    assert result_data[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert isinstance(result_data[0], Category)
    assert isinstance(result_data[0].products, list)
    assert isinstance(result_data[0].products[0], Product)
