from pickletools import uint1


class Product:
    """
    Класс Продукты
    """

    # name: str
    # description: str
    # price: float
    # quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        :param name: str - name
        :param description: str -description
        :param price: int - price
        :param quantity: int - quantity
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            if new_price < self.price:
                print(
                    f"Устанавливаемая цена ({new_price} р.) ниже текущей ({self.price} р.). Применить изменения? y/n"
                )
                match input("Ответ: ").strip().lower():
                    case "y":
                        self.__price = new_price
                        print(f"Установлена цена {new_price} р.")
                    case "n":
                        print(f"Изменения отменены. Прежняя цена {self.price} р. не изменилась.")
                    case _:
                        print("Invalid command. No changes...")

        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict, category_objects: list) -> object:
        """
        Создаёт новый объект класса или обновляет текущий, если имя уже занято.
        """
        for category in category_objects:
            for product in category.product_objects:
                if product_data["name"].lower() == product.name.lower():
                    product.quantity += product_data["quantity"]
                    product.__price = max(product_data["price"], product.price)
                    return product
        return cls(**product_data)


class Category:
    """
    Класс Категории
    """

    name: str
    description: str
    __products: list[Product]
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        :param name: str - name
        :param description: str - description
        :param products: list[object] - list of Product objects
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)} шт.'

    def add_product(self, product_obj: Product) -> None:
        """
        Создаёт новый объект класса
        """
        self.__products.append(product_obj)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Возвращает __products в виде списка строк
        """
        return "\n".join([str(i) for i in self.__products])

    @property
    def product_objects(self) -> list:
        """
        Возвращает __products в виде объектов
        """
        return self.__products




