from abc import ABC, abstractmethod

class PrintMixin:
    def __init__(self, *args):
        print(repr(self))
    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"

class Category(PrintMixin):
    def __init__(self, title, descriptions, products):
        self.title = title
        self.descriptions = descriptions
        self.__products = products
    def __len__(self):
        return len(self.products)
    @property
    def products(self):
        return [(f"{product.title}, {product.pay} руб. Остаток: {product.quantity} шт.") for product in self.__products]

    def get_total_category(self):
        total = 0
        for product in self.__products:
            total += product.pay * product.quantity
        self.total_category = total
        return total

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            print("Нельзя добавить объект другого класса")
    def __str__(self):
        return f'Название категории, количество продуктов: {len(self)} шт.'

    def add_product(self, product):
        if isinstance(product, Product):
            if product.quantity == 0:
                raise ValueError("Товар с нулевым количеством не может быть добавлен")
            self.__products.append(product)
        else:
            print("Нельзя добавить объект другого класса")

    def calculate_average_price(self):
        total_price = 0
        total_quantity = 0

        for product in self.__products:
            total_price += product.pay * product.quantity
            total_quantity += product.quantity

        try:
            average_price = total_price / total_quantity
            return average_price
        except ZeroDivisionError:
            return 0

    class Abstract(ABC):

        @classmethod
        @abstractmethod
        def create_product(cls):
            pass

        @property
        @abstractmethod
        def pay(self):
            pass

        @pay.setter
        @abstractmethod
        def pay(self, new_pay):
            pass

class Product(PrintMixin, ABC):
    def __init__(self, title, descriptions, pay, quantity):
        self.title = title
        self.descriptions = descriptions
        self.pay = pay
        self.quantity = quantity

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, new_pay):
        if new_pay <= 0:
            print("Цена введена некорректная")
        else:
            self.__pay = new_pay

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        total_price_self = self.pay * self.quantity
        total_price_other = other.pay * other.quantity
        return total_price_self + total_price_other

    def get_total(self):
        return self.pay * self.quantity

    def update_quantity(self, update_quantity):
        self.quantity = update_quantity
        return self.quantity

    @classmethod
    def create_product(cls, title, descriptions, pay, quantity):
        return cls(title, descriptions, pay, quantity)

    def __str__(self):
        return f'{self.title}, {self.pay} руб. Остаток: {self.quantity} шт.'

class Smartphone(Product):
    def __init__(self, title, descriptions, pay, quantity, performance, model, memory, color):
        super().__init__(title, descriptions, pay, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

class Grass(Product):
    def __init__(self, title, descriptions, pay, quantity, country_of_origin, germination_period, color):
        super().__init__(title, descriptions, pay, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
