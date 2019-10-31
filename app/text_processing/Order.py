from food_items import *
import sys

sys.path.insert(1, "app/audio_output")

import PlayMP3
class Order:

    def __init__(self):
        self.speak = PlayMP3.PlayMP3()
        self.state = "greet"
        self.order = []
        self.greet()


    def input(self, input):
        input = input.lower()
        if self.state == "greet":
            self.state = "menu_item"
        elif self.state == "menu_item":
            self.try_to_add_item(input)
        elif self.state == "additions":
            self.add_to_item(input)
        elif self.state == "removals":
            self.remove_from_item(input)
        elif self.state == "is that all":
            self.order_complete(input)
        else:
            self.get_manager


    def greet(self):

        # self.say("Welcome to Themis-- Where customer success comes first. What can I get for you?")
        self.speak.playMP3("prompt_for_menu_item")
        self.state = "menu_item"

    def prompt_for_menu_item(self):
        # self.say("anything else for you today?")
        self.speak.playMP3("prompt_for_menu_item")

    def prompt_for_addition(self):
        # self.say("anything extra on that?")
        self.speak.playMP3("prompt_for_addition")

    def prompt_for_removal(self):
        # self.say("need anything removed from that?")
        self.speak.playMP3("prompt_for_removal")

    def prompt_for_end_order(self):
        self.confirm_order()
        # self.say("is that everything?")
        self.speak.playMP3("prompt_for_end_order")

    def farewell(self):
        # self.say("Thank you for choosing Themis hunger solutions, stay fit and have fun")
        self.speak.playMP3("farewell")

    def try_to_add_item(self, input):
        self.state = "additions"
        self.say(self.add_item_to_order(input))
        if self.state == "additions":
            self.prompt_for_addition()

    def add_item_to_order(self, input):

        if "burger" in input:
            if "veggie" in input:
                self.order.append(VeggieBurger('Single'))
                return "Veggie Burger"
            if "chicken" in input:
                self.order.append(ChickenBurger('Single'))
                return "Chicken Burger"
            else:
                self.order.append(BeefBurger('Single'))
                return "Beef Burger"
        elif "fries" in input:
            if "curly" in input:
                self.order.append(CurlyFries('Small'))
                return "curly fries"
            if "yam" in input:
                self.order.append(YamFries('Small'))
                return "yam"
            else:
                self.order.append(RegularFries('Small'))
                return "fries"
        else:
            self.state = "menu_items"
            self.say("Let me get my manager to help you")

    def add_to_item(self, input):
        if "no" in input:
            self.state = "removals"
            self.prompt_for_removal()
            return
        item = self.order[-1]
        for ingredient in item.ingredients:
            if ingredient in input:
                item.add_addition(ingredient)
        self.say("anything else?")
        return

    def remove_from_item(self, input):
        if "no" in input:
            self.state = "is that all"
            self.prompt_for_end_order()
            return
        item = self.order[-1]
        for ingredient in item.ingredients:
            if ingredient in input:
                item.add_removal(ingredient)
        self.say("anything else?")
        return

    def order_complete(self, input):
        if "yes" in input:
            self.farewell()
            del self
        return

    def confirm_order(self):
        order = ""
        for item in self.order:
            order += (" " + item.name)
            for addition in item.additions:
                order += " with " + addition
            for removal in item.removals:
                order += " with " + removal
        self.say(order)

    def order_string(self):
        return

    def get_manager(self):
        self.say("Let me get my manager to help you")

    def say(self, string):
        print(string)

# order = Order()
# order.input("burger")
# order.input("cheese")
# order.input("no")
# order.input("no")
# order.input("yes")
