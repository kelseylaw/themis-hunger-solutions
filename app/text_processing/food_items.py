class Burger:
    type_options = ["beef", "chicken", "veggie"]
    size_options = ["single", "double"]
    possible_ingredients = {
        "beef patty": 1.5,
        "chicken patty": 2,
        "veggie patty": 1.5,
        "bacon": 1,
        "cheese": 1,
        "lettuce": 0.5,
        "tomato": 0.5,
        "ketchup": 0.25,
        "mayo": 0.25,
        "mustard": 0.25,
        "pickles": 0.5,
        "onions": 0.5,
        "peppers": 0.5,
    }

    def __init__(self, size):
        self.name = "burger"
        self.prices = {}
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

    def upsell(self):
        if self.name == "veggie burger":
            return ("veggie patty", 1.5)
        elif "bacon" not in self.additions:
            return ("bacon", 1)
        elif "cheese" not in self.additions:
            return ("cheese", 1)
        else:
            return ("beef patty", 1.5)

    def get_name(self):
        return self.name

    def get_size(self):
        print(self.size)
        return self.size

    def set_price(self):
        price = self.prices.get(self.get_size(), 0)
        for ingredient in self.additions:
            price = price + self.get_additions_price(ingredient)
        self.price = price

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients

    def get_additions_price(self, addition):
        return self.possible_ingredients.get(addition, 0)

    def add_addition(self, ingredient):
        if ingredient in self.additions:
            print("You've already added that extra ingredient to the burger! Do you really need that much more?")
        elif ingredient in Burger.possible_ingredients.keys():
            self.additions.append(ingredient)
            self.set_price()
        else:
            print("What the fries! I can't add that to the burger!")

    def add_removal(self, ingredient):
        if ingredient in self.removals:
            print("Darn! You've already removed that from the burger!")
        elif ingredient in self.ingredients:
            self.removals.append(ingredient)
        else:
            print("What the fries! I can't remove that!")

    def print_order(self):
        print(self.size.upper() + " " + self.name.upper() + "\t\t\t$" + str(self.get_price()))
        for addition in self.additions:
            if addition in self.ingredients:
                print("\t - Extra " + addition.title() + "\t\t\t+$" + str(self.get_additions_price(addition)))
            else:
                print("\t - Add " + addition.title() + "\t\t\t+$" + str(self.get_additions_price(addition)))
        for removal in self.removals:
            print("\t - No " + removal.title())


class BeefBurger(Burger):
    def __init__(self, size):
        super().__init__(size)
        self.name = "beef burger"
        self.prices = { "single": 7.99, "double": 8.99 }
        self.ingredients = ["bun", "beef patty", "cheese", "lettuce", "tomato", "ketchup", "mustard", "pickles",  "onions"]
        self.set_price()


class ChickenBurger(Burger):
    def __init__(self, size):
        super().__init__(size)
        self.name = "chicken burger"
        self.prices = {"single": 8.99, "double": 9.99}
        self.ingredients = ["bun", "chicken patty", "lettuce", "tomato", "mayo", "pickles", "onions"]
        self.set_price()


class VeggieBurger(Burger):
    def __init__(self, size):
        super().__init__(size)
        self.name = "veggie burger"
        self.prices = {"single": 8.99, "double": 9.99}
        self.ingredients = ["bun", "veggie patty", "cheese", "lettuce", "tomato", "ketchup", "mustard", "pickles", "onions"]
        self.set_price()


class Fries:
    type_options = ["regular", "yam", "curly"]
    size_options = ["small", "medium", "large"]
    possible_ingredients = {
        "salt": 0,
        "gravy": 1,
        "cheese curds": 1,
        "ketchup": 0
    }

    def __init__(self, size):
        self.name = "fries"
        self.prices = {}
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

    def set_price(self):
        self.price = self.prices.get(self.get_size(), 0)

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients

    def get_additions_price(self, addition):
        return self.possible_ingredients.get(addition, 0)

    def add_addition(self, ingredient):
        if ingredient in self.additions:
            print("You've already added that extra ingredient to the fries! Do you really need that much more?")
        elif ingredient in Fries.possible_ingredients.keys():
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

    def print_order(self):
        print(self.size.upper() + " " + self.name.upper() + "\t\t\t$" + str(self.get_price()))
        for addition in self.additions:
            if addition in self.ingredients:
                print("\t - Extra " + addition.title() + "\t\t\t+$" + str(self.get_additions_price(addition)))
            else:
                print("\t - Add " + addition.title() + "\t\t\t+$" + str(self.get_additions_price(addition)))
        for removal in self.removals:
            print("\t - No " + removal.title())


class RegularFries(Fries):
    def __init__(self, size):
        super().__init__(size)
        self.name = "regular fries"
        self.prices = {"small": 3.49, "medium": 4.49, "large": 5.49}
        self.ingredients = ["potatoes", "salt"]
        self.set_price()

class YamFries(Fries):
    def __init__(self, size):
        super().__init__(size)
        self.name = "yam fries"
        self.prices = {"small": 6.49, "medium": 7.49, "large": 8.49}
        self.ingredients = ["yams", "salt"]
        self.set_price()


class CurlyFries(Fries):
    def __init__(self, size):
        super().__init__(size)
        self.name = "curly fries"
        self.prices = {"small": 4.49, "medium": 5.49, "large": 6.49}
        self.ingredients = ["potatoes", "salt"]
        self.set_price()