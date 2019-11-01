import sys
sys.path.insert(1, "app/audio_output")
import PlayMP3

class Burger:
    type_options = ["cheeseburger", "chicken", "veggie"]
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
        self.speak = PlayMP3.PlayMP3()
        if size in self.size_options:
            self.size = size
        # else:
            # self.speak.playMP3("confirm_invalid_size")

    @classmethod
    def is_valid_type(size):
        return size in Burger.type_options

    @classmethod
    def is_valid_size(size):
        return size in Burger.size_options

    @classmethod
    def print_menu(cls):
        print("WELCOME TO THEMIS HUNGER SOLUTIONS! I'M HENRY, HERE'S YOUR MENU:\n")
        print("BURGERS:")
        print("\tCHEESEBURGER\t\t\t$7.99")
        print("\tCHICKEN BURGER\t\t\t$8.99")
        print("\tVEGGIE BURGER\t\t\t$8.99")
        print("ADD-ONS:")
        for addon in cls.possible_ingredients.keys():
            if "patty" in addon:
                print("\t" + addon.upper() + "\t\t\t$" + str(cls.possible_ingredients.get(addon)))
            else:
                print("\t" + addon.upper() + "\t\t\t\t$" + str(cls.possible_ingredients.get(addon)))

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
        # if ingredient in self.additions:
        #     self.speak.playMP3("confirm_already_added")
        if ingredient in Burger.possible_ingredients.keys() and ingredient not in self.additions:
            self.additions.append(ingredient)
            self.set_price()
        # else:
        #     self.speak.playMP3("confirm_not_valid")

    def add_removal(self, ingredient):
        # if ingredient in self.removals:
        #     self.speak.playMP3("confirm_already_removed")
        if ingredient in self.ingredients and ingredient not in self.removals:
            self.removals.append(ingredient)
        # else:
        #     self.speak.playMP3("confirm_not_valid")

    def print_order(self):
        print(self.size.upper() + " " + self.name.upper() + "\t\t\t$" + str(self.get_price()))
        for addition in self.additions:
            if addition in self.ingredients:
                title = "\t - Extra " + addition.title()
                if len(title) > 13:
                    print("\t - Extra " + addition.title() + "\t\t+$" + str(self.get_additions_price(addition)))
                else:
                    print("\t - Extra " + addition.title() + "\t\t\t+$" + str(self.get_additions_price(addition)))
            else:
                title = "\t - Add " + addition.title()
                if len(title) > 13:
                    print("\t - Add " + addition.title() + "\t\t+$" + str(self.get_additions_price(addition)))
                else:
                    print("\t - Add " + addition.title() + "\t\t\t+$" + str(self.get_additions_price(addition)))
        for removal in self.removals:
            print("\t - No " + removal.title())


class Cheeseburger(Burger):
    def __init__(self, size):
        super().__init__(size)
        self.name = "cheeseburger"
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
        "salt": 0.10,
        "gravy": 1,
        "cheese": 1,
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
        self.speak = PlayMP3.PlayMP3()
        if size in self.size_options:
            self.size = size
        # else:
        #     self.speak.playMP3("confirm_invalid_size")

    @classmethod
    def is_valid_type(size):
        return size in Fries.type_options

    @classmethod
    def is_valid_size(size):
        return size in Fries.size_options

    @classmethod
    def print_menu(cls):
        print("FRIES:")
        print("\tREGULAR FRIES\t\t\t$3.49")
        print("\tYAM FRIES\t\t\t$6.49")
        print("\tCURLY FRIES\t\t\t$4.49")
        print("ADD-ONS:")
        for addon in cls.possible_ingredients.keys():
            print("\t" + addon.upper() + "\t\t\t\t$" + str(cls.possible_ingredients.get(addon)))

    def upsell(self):
        if self.name == "regular fries" and ["cheese", "gravy"] not in self.additions:
            return ("poutine", 2)
        elif "gravy" not in self.additions:
            return ("cheese", 1)
        elif "cheese" not in self.additions:
            return ("gravy", 1)
        else:
            return ("ketchup", 0)


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
        # if ingredient in self.additions:
        #     self.speak.playMP3("confirm_already_added")
        if ingredient in Fries.possible_ingredients.keys() and ingredient not in self.additions:
            if ingredient == "gravy" and "cheese" in self.additions:
                self.additions.remove("cheese")
                self.additions.append("poutine")
            elif ingredient == "cheese" and "gravy" in self.additions:
                self.additions.remove("gravy")
                self.additions.append("poutine")
            else:
                self.additions.append(ingredient)
        # else:
        #     self.speak.playMP3("confirm_not_valid")

    def add_removal(self, ingredient):
        # if ingredient in self.removals:
        #     self.speak.playMP3("confirm_already_removed")
        if ingredient in self.ingredients and ingredient not in self.removals:
            self.removals.append(ingredient)
        # else:
        #     self.speak.playMP3("confirm_not_valid")

    def print_order(self):
        print(self.size.upper() + " " + self.name.upper() + "\t\t\t$" + str(self.get_price()))
        for addition in self.additions:
            if addition in self.ingredients:
                print("\t - Extra " + addition.title() + "\t\t\t+$" + str(self.get_additions_price(addition)))
            elif addition == "poutine":
                print("\t - Add " + addition.title() + "\t\t\t+$2")
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
