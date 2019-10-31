class Burger:
    type_options = ["beef", "chicken", "veggie"]
    size_options = ["single", "double"]
    possible_ingredients = [
        "bun",
        "beef patty",
        "chicken patty",
        "veggie patty",
        "bacon",
        "cheese",
        "lettuce",
        "tomato",
        "ketchup",
        "mayo",
        "mustard",
        "pickles",
        "onions",
        "peppers",
    ]

    def __init__(self, size):
        self.name = "burger"
        self.price = 0
        self.ingredients = []
        self.removals = []
        self.additions = []
        if size in self.size_options:
            self.size = size
        else:
            print("Oh no! That's not a valid size for this burger!")

    @classmethod
    def is_valid_type(size):
        return size in Burger.type_options

    @classmethod
    def is_valid_size(size):
        return size in Burger.size_options

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.price

    def add_addition(self, ingredient):
        if ingredient in self.additions:
            print("You've already added that extra ingredient to the burger! Do you really need that much more?")
        elif ingredient in Burger.possible_ingredients:
            self.additions.append(ingredient)
        else:
            print("What the fries! I can't add that to the burger!")

    def add_removal(self, ingredient):
        if ingredient in self.removals:
            print("Darn! You've already removed that from the burger!")
        elif ingredient in self.ingredients:
            self.removals.append(ingredient)
        else:
            print("What the fries! I can't remove that!")


class BeefBurger(Burger):
    def __init__(self, size):
        super().__init__(size)
        self.name = "beef burger"
        self.price = 7.99
        self.ingredients = ["bun", "beef patty", "cheese", "lettuce", "tomato", "ketchup", "mustard", "pickles",  "onions"]


class ChickenBurger(Burger):
    def __init__(self, size):
        super().__init__(size)
        self.name = "chicken burger"
        self.price = 8.99
        self.ingredients = ["bun", "chicken patty", "lettuce", "tomato", "mayo", "pickles", "onions"]


class VeggieBurger(Burger):
    def __init__(self, size):
        super().__init__(size)
        self.name = "veggie burger"
        self.price = 8.99
        self.ingredients = ["bun", "veggie patty", "cheese", "lettuce", "tomato", "ketchup", "mustard", "pickles", "onions"]


class Fries:
    type_options = ["regular", "yam", "curly"]
    size_options = ["small", "medium", "large"]
    possible_ingredients = [
        "salt",
        "curl"
    ]

    def __init__(self, size):
        self.name = "fries"
        self.price = 0
        self.size = size
        self.ingredients = []
        self.removals = []
        self.additions = []
        if size in self.size_options:
            self.size = size
        else:
            print("Oh no! That's not a valid size for the fries!")

    @classmethod
    def is_valid_type(size):
        return size in Fries.type_options

    @classmethod
    def is_valid_size(size):
        return size in Fries.size_options

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.price

    def add_addition(self, ingredient):
        if ingredient in self.additions:
            print("You've already added that extra ingredient to the fries! Do you really need that much more?")
        elif ingredient in Fries.possible_ingredients:
            self.additions.append(ingredient)
        else:
            print("What the fries! I can't add that to your fries!")

    def add_removal(self, ingredient):
        if ingredient in self.removals:
            print("Darn! You've already removed that from the fries!")
        elif ingredient in self.ingredients:
            self.removals.append(ingredient)
        else:
            print("What the fries! I can't remove that!")


class RegularFries(Fries):
    def __init__(self, size):
        super().__init__(size)
        self.name = "regular fries"
        self.ingredients = ["potatoes", "salt"]

class YamFries(Fries):
    def __init__(self, size):
        super().__init__(size)
        self.name = "yam fries"
        self.ingredients = ["yams", "salt"]


class CurlyFries(Fries):
    def __init__(self, size):
        super().__init__(size)
        self.name = "curly fries"
        self.ingredients = ["potatoes", "salt"]