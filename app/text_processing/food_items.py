from abc import ABC, abstractmethod


class FoodItem(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def food_name(self):
        pass
    # aliases?

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def type_options(self):
        pass


class Burger(FoodItem):
    food_name = "Burger"
    type_options = ["Beef", "Chicken", "Veggie"]

    @property
    @abstractmethod
    def size(self):
        pass


class BeefBurger(Burger, ABC):
    food_name = "Beef Burger"
    stock = 10


class ChickenBurger(Burger, ABC):
    food_name = "Chicken Burger"
    stock = 10


class VeggieBurger(Burger, ABC):
    food_name = "Veggie Burger"
    stock = 10


class Fries(FoodItem, ABC):
    food_name = "Fries"
    type_options = ["Regular", "Yam", "Curly"]

    def stock(self):
        pass


class RegularFries(Fries, ABC):
    food_name = "Regular Fries"
    stock = 30


class YamFries(Fries, ABC):
    food_name = "Yam Fries"
    stock = 20


class CurlyFries(Fries, ABC):
    food_name = "Curly Fries"
    stock = 15
