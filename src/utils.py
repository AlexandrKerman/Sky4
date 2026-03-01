import json

from src.classes import Category, Product


def get_from_json(path: str) -> list:
    if not path.endswith(".json"):
        return []

    with open(path, "r", encoding="utf-8") as json_file:
        return list(json.load(json_file))

# moved in classes.py, now is Category class method
#
# def convert_dict_list(raw_data: list[dict]) -> list:
#     """
#     Преобразует список словарей raw_data в список объектов Category.
#     """
#     if raw_data:
#         return [
#             Category(
#                 name=category["name"],
#                 description=category["description"],
#                 products=[Product(**product) for product in category["products"]],
#             )
#             for category in raw_data
#         ]
#     return []
