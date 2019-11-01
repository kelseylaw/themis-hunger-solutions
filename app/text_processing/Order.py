from food_items import *
from word_bank import *
import sys

sys.path.insert(1, "app/audio_output")

import PlayMP3
import TextToSpeech
class Order:

    def __init__(self):
        self.speak = PlayMP3.PlayMP3()
        self.text_to_speech = TextToSpeech.TextToSpeech()
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
        self.speak.playMP3("greet")
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
        self.say(self.add_item_to_order(input))
        self.prompt_for_addition()

    def add_item_to_order(self, input):
        self.state = "additions"
        if "burger" in input:
            if "veggie" in input:
                self.order.append(VeggieBurger('single'))
                return "Veggie Burger"
            if "chicken" in input:
                self.order.append(ChickenBurger('single'))
                return "Chicken Burger"
            else:
                self.order.append(BeefBurger('single'))
                return "Beef Burger"
        elif "fries" in input:
            if "curly" in input:
                self.order.append(CurlyFries('small'))
                return "curly fries"
            if "yam" in input:
                self.order.append(YamFries('small'))
                return "yam"
            else:
                self.order.append(RegularFries('small'))
                return "fries"
        else:
            self.state = "menu_items"
            # self.say("Let me get my manager to help you")
            self.speak.playMP3("get_manager")

    def add_to_item(self, input):
        if search_negative(input):
            self.state = "removals"
            self.prompt_for_removal()
            return
        item = self.order[-1]
        additional_item = False
        for ingredient in item.possible_ingredients:
            if ingredient in input:
                item.add_addition(ingredient)
                additional_item = True
        # self.say("anything else?")
        if additional_item:
            self.speak.playMP3("anything_else") ## KELSEY & JULIEN
        return

    def remove_from_item(self, input):
        if search_negative(input):
            self.state = "is that all"
            self.prompt_for_end_order()
            return
        item = self.order[-1]
        removed_item = False
        for ingredient in item.possible_ingredients:
            if ingredient in input:
                item.add_removal(ingredient)
                removed_item = True
        if removed_item:
            self.speak.playMP3("anything_else")
        return

    def order_complete(self, input):
        if search_affirmative(input):
            for order in self.order:
                order.print_order()
            self.farewell()
            del self
        return

    def confirm_order(self):
        order = ""
        for item in self.order:
            order += (" " + item.name)
            additions = 0
            for addition in item.additions:
                if additions == 0:
                    order += " with " + addition
                if additions > 0:
                    order += " and " + addition
                additions += 1
            removals = 0
            for removal in item.removals:
                if removals == 0:
                    order += " without " + removal
                if removals > 0:
                    order += " or " + removal
                removals += 1
        # self.say(order)
        self.text_to_speech.textToSpeech(order, "order")

    def order_string(self):
        return

    def get_manager(self):
        self.say("Let me get my manager to help you")

    def say(self, string):
        print(string)
