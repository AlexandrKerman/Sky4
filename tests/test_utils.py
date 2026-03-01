from unittest.mock import mock_open, patch

from src import utils


def test_get_json():
    with patch("builtins.open", mock_open(read_data='[{"key1": 1, "key2": 2}, {"key1": 3, "key2": 4}]')):
        assert utils.get_from_json("data/test.json") == [{"key1": 1, "key2": 2}, {"key1": 3, "key2": 4}]
    with patch("builtins.open", mock_open(read_data="[]")):
        assert utils.get_from_json("data/test.json") == []
    assert utils.get_from_json("data/test") == []



