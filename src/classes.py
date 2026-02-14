class Product:
    """
    Класс Продукты
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        :param name: str - name
        :param description: str -description
        :param price: int - price
        :param quantity: int - quantity
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс Категории
    """

    name: str
    description: str
    products: list[object]
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list[object]):
        """
        :param name: str - name
        :param description: str - description
        :param products: list[object] - list of Product objects
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count = len(self.products)
