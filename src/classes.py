from abc import ABC, abstractmethod

from src import exceptions


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict, category_objects: list) -> object:
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class PrintMixin:
    def __init__(self, obj):
        print(repr(obj))


class Product(BaseProduct, PrintMixin):
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
        if not quantity:
            raise exceptions.ZeroQuantityError

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(self)

    def __repr__(self):
        return f'Product("{self.name}", "{self.description}", {self.price}, {self.quantity})'

    def __str__(self) -> str:
        """
        str of object
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        obj + obj, return sum of obj prices
        """
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.price * other.quantity
        if other == 0:  # for sum() and other
            return self.__price * self.quantity + other
        raise TypeError(f"Expected {type(self)}. Got {type(other)}")

    def __radd__(self, other: float | int) -> float | int:
        """
        obj + any, return sum
        """
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.price * other.quantity
        if other == 0:  # for sum() and other
            return self.__price * self.quantity + other
        raise TypeError(f"Expected {type(self)}. Got {type(other)}")

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

    def __str__(self) -> str:
        """
        str of object
        """
        return f"{self.name}, количество продуктов: {sum(map(lambda x: x.quantity, self.__products))} шт."  # Сумма по количеству в Product

    def add_product(self, product_obj: Product = None, is_object: bool = True, **kwargs) -> None:
        """
        Создаёт новый объект класса,
        :raises
            TypeError : if got not Product instance
        """
        if is_object:
            if isinstance(product_obj, Product):
                self.__products.append(product_obj)
                Category.product_count += 1
            else:
                raise TypeError(f"Expected Product instance. Got {type(product_obj)}")
        elif kwargs:
            try:
                product_obj = Product(**kwargs)
                self.__products.append(product_obj)
            except exceptions.ZeroQuantityError as e:
                print(e)
            finally:
                print("Обработка добавления товара завершена")

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

    @classmethod
    def add_categories(cls, raw_data: list[dict]) -> list:
        """
        Преобразует список словарей raw_data в список объектов Category.
        """
        if raw_data:
            return [
                cls(
                    name=category["name"],
                    description=category["description"],
                    products=[Product(**category_product) for category_product in category["products"]],
                )
                for category in raw_data
            ]
        return []

    def get_average(self):
        return round(sum([product.price for product in self.__products]) / len(self.__products), 2)


class CategoryIterator:
    """
    Итератор, возвращающий продукты в категории
    :raises:
        TypeError: если не является объектом Category
    """

    def __init__(self, category: Category):
        if isinstance(category, Category):
            self.category = category
        else:
            raise TypeError(f"Expected Category instance. Got {type(category)}")

    def __iter__(self):
        """
        Инициализация итератора
        """
        self.current = -1
        self.product_len = len(self.category.product_objects)
        return self

    def __next__(self):
        """
        Возвращает следующий продукт категории

        :raises:
            StopIteration: Если список продуктов кончился
        """
        self.current += 1
        if self.current < self.product_len:
            return self.category.product_objects[self.current]
        else:
            raise StopIteration


class Smartphone(Product):
    """
    Подкласс Product - Смартфоны
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Подкласс Product - Газонная трава
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
