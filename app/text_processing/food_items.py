class Burger:
    type_options = ["Beef", "Chicken", "Veggie"]
    size_options = ["Single", "Double"]

    def __init__(self, size):
        self.name = "Burger"
        self.ingredients = []
        self.removals = []
        self.additions = []
        if size in self.size_options:
            self.size = size
        else:
            raise Exception("Oh no! '" + size + "' is not a valid size for this burger!")

    @classmethod
    def is_valid_type(size):
        return size in Burger.type_options

    @classmethod
    def is_valid_size(size):
        return size in Burger.size_options

    def add_addition(self, ingredient):
        if ingredient in self.additions:
            raise Exception("You've already added extra " + ingredient + " to the burger!")
        elif ingredient in self.ingredients:
            self.additions.append(ingredient)
        else:
            raise Exception("What the fries! I can't add extra " + ingredient + " to the burger!")

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

    def __init__(self, size):
        self.name = "Fries"
        self.size = size
        self.ingredients = []
        self.removals = []
        self.additions = []
        if size in self.size_options:
            self.size = size
        else:
            raise Exception("Oh no! '" + size + "' is not a valid size for the fries!")

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
            raise Exception("You've already added extra " + ingredient + " to the fries!")
        elif ingredient in self.ingredients:
            self.additions.append(ingredient)
        else:
            raise Exception("What the fries! I can't add extra " + ingredient + " to the fries!")


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