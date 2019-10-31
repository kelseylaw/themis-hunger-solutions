class Burger:
    type_options = ["Beef", "Chicken", "Veggie"]
    size_options = ["Single", "Double"]
    possible_ingredients = [
        "Bun",
        "Beef Patty",
        "Chicken Patty",
        "Veggie Patty",
        "Cheese",
        "Lettuce",
        "Tomato",
        "Ketchup",
        "Mayo",
        "Mustard",
        "Pickles",
        "Onions",
        "Peppers",
    ]

    def __init__(self, size):
        self.name = "Burger"
        self.ingredients = []
        self.removals = []
        self.additions = []
        if size in self.size_options:
            self.size = size
        else:
            raise Exception("Oh no! That's not a valid size for this burger!")

    @classmethod
    def is_valid_type(size):
        return size in Burger.type_options

    @classmethod
    def is_valid_size(size):
        return size in Burger.size_options

    def add_addition(self, ingredient):
        if ingredient in self.additions:
            raise Exception("You've already added that extra ingredient to the burger! Do you really need that much more?")
        elif ingredient in Burger.possible_ingredients:
            self.additions.append(ingredient)
        else:
            raise Exception("What the fries! I can't add that to the burger!")

    def add_removal(self, ingredient):
        if ingredient in self.removals:
            raise Exception("Darn! You've already removed that from the burger!")
        elif ingredient in self.ingredients:
            self.removals.append(ingredient)
        else:
            raise Exception("What the fries! I can't remove that from the burger!")


class BeefBurger(Burger):
    def __init__(self, size):
        self.name = "Beef Burger"
        self.ingredients = ["Bun", "Beef Patty", "Cheese", "Lettuce", "Tomato", "Ketchup", "Mustard", "Pickles",  "Onions"]
        super().__init__(size)


class ChickenBurger(Burger):
    def __init__(self, size):
        self.name = "Chicken Burger"
        self.ingredients = ["Bun", "Chicken Patty", "Cheese", "Lettuce", "Tomato", "Mayo", "Pickles", "Onions"]
        super().__init__(size)


class VeggieBurger(Burger):
    def __init__(self, size):
        self.name = "Veggie Burger"
        self.ingredients = ["Bun", "Veggie Burger", "Cheese", "Lettuce", "Tomato", "Ketchup", "Mustard", "Pickles", "Onions"]
        super().__init__(size)


class Fries:
    type_options = ["Regular", "Yam", "Curly"]
    size_options = ["Small", "Medium", "Large"]
    possible_ingredients = [
        "Potatoes",
        "Yams",
        "Salt",
        "Curl"
    ]

    def __init__(self, size):
        self.name = "Fries"
        self.size = size
        self.ingredients = []
        self.removals = []
        self.additions = []
        if size in self.size_options:
            self.size = size
        else:
            raise Exception("Oh no! That's not a valid size for the fries!")

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

    def add_addition(self, ingredient):
        if ingredient in self.additions:
            raise Exception("You've already added that extra ingredient to the burger! Do you really need that much more?")
        elif ingredient in Fries.possible_ingredients:
            self.additions.append(ingredient)
        else:
            raise Exception("What the fries! I can't add that to your fries!")

    def add_removal(self, ingredient):
        if ingredient in self.removals:
            raise Exception("Darn! You've already removed that from the fries!")
        elif ingredient in self.ingredients:
            self.removals.append(ingredient)
        else:
            raise Exception("What the fries! I can't add that!")


class RegularFries(Fries):
    def __init__(self, size):
        self.name = "Regular Fries"
        self.ingredients = ["Potatoes", "Salt"]
        super().__init__(size)


class YamFries(Fries):
    def __init__(self, size):
        self.name = "Yam Fries"
        self.ingredients = ["Yams", "Salt"]
        super().__init__(size)


class CurlyFries(Fries):
    def __init__(self, size):
        self.name = "Curly Fries"
        self.ingredients = ["Potatoes", "Salt"]
        super().__init__(size)