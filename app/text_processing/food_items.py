class Burger:
    type_options = ["Beef", "Chicken", "Veggie"]
    size_options = ["Single", "Double"]

    def __init__(self, size):
        self.size = size

    @classmethod
    def is_valid_type(size):
        return size in Burger.type_options

    @classmethod
    def is_valid_size(size):
        return size in Burger.size_options


class BeefBurger(Burger):
    def __init__(self, size):
        self.name = "Beef Burger"
        super().__init__(size)


class ChickenBurger(Burger):
    def __init__(self, size):
        self.name = "Chicken Burger"
        super().__init__(size)


class VeggieBurger(Burger):
    def __init__(self, size):
        self.name = "Veggie Burger"
        super().__init__(size)


class Fries:
    type_options = ["Regular", "Yam", "Curly"]
    size_options = ["Small", "Medium", "Large"]

    def __init__(self, size):
        self.size = size

    @classmethod
    def is_valid_type(size):
        return size in Fries.type_options

    @classmethod
    def is_valid_size(size):
        return size in Fries.size_options


class RegularFries(Fries):
    def __init__(self, size):
        self.name = "Regular Fries"
        super().__init__(size)


class YamFries(Fries):
    def __init__(self, size):
        self.name = "Yam Fries"
        super().__init__(size)


class CurlyFries(Fries):
    def __init__(self, size):
        self.name = "Curly Fries"
        super().__init__(size)