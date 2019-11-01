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
        if search_hostile(input):
            self.get_manager()
        elif self.state == "greet":
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
        print("\n\n")
        Burger.print_menu()
        Fries.print_menu()
        self.speak.playMP3("greet")
        self.state = "menu_item"
        print("-----------------------------------\n")
        print("\nYOUR ORDER:\n")

    def prompt_for_menu_item(self):
        self.speak.playMP3("prompt_for_menu_item")

    def prompt_for_addition(self):
        self.speak.playMP3("prompt_for_addition")

    def prompt_for_additional_addition(self):
        self.speak.playMP3("prompt_for_additional_addition")

    def prompt_for_removal(self):
        self.speak.playMP3("prompt_for_removal")

    def prompt_for_additional_removal(self):
        self.speak.playMP3("prompt_for_additional_removal")

    def prompt_for_end_order(self):
        self.confirm_order()
        self.speak.playMP3("prompt_for_end_order")

    def farewell(self):
        self.speak.playMP3("farewell")

    def random_confirmation(self):
        self.speak.playMP3("{}".format(random_confirmation()))

    def try_to_add_item(self, input):
        self.add_item_to_order(input)
        self.prompt_for_addition()

    def add_item_to_order(self, input):
        self.state = "additions"
        if "burger" in input:
            if "veggie" in input:
                self.order.append(VeggieBurger('single'))
                self.random_confirmation()
                return "Veggie Burger"
            if "chicken" in input:
                self.order.append(ChickenBurger('single'))
                self.random_confirmation()
                return "Chicken Burger"
            else:
                self.order.append(BeefBurger('single'))
                self.random_confirmation()
                return "Beef Burger"
        elif "fries" in input:
            if "curly" in input:
                self.order.append(CurlyFries('small'))
                self.random_confirmation()
                return "curly fries"
            if "yam" in input:
                self.order.append(YamFries('small'))
                self.random_confirmation()
                return "yam"
            else:
                self.order.append(RegularFries('small'))
                self.random_confirmation()
                return "fries"
        else:
            self.state = "menu_items"
            self.get_manager

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
        if additional_item:
            self.random_confirmation()
            self.prompt_for_additional_addition()
        return

    def remove_from_item(self, input):
        if search_negative(input):
            self.state = "is that all"
            self.prompt_for_end_order()
            self.order[-1].print_order()
            return
        item = self.order[-1]
        removed_item = False
        for ingredient in item.possible_ingredients:
            if ingredient in input:
                item.add_removal(ingredient)
                removed_item = True
        if removed_item:
            self.random_confirmation()
            self.prompt_for_additional_removal()
        return

    def order_complete(self, input):
        if search_affirmative(input):
            self.print_order_total()
            self.farewell()
            sys.exit()
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
        self.text_to_speech.textToSpeech(order, "order")

    def order_string(self):
        return

    def get_manager(self):
        self.speak.playMP3("get_manager")
        sys.exit()

    def say(self, string):
        print(string)

    def print_order_total(self):
        sub_total = 0
        for order in self.order:
            sub_total += order.get_price()
        sub_total = round(sub_total, 2)
        tax = round(sub_total * 0.05, 2)
        total = sub_total + tax

        print("\n\t\t\t\t\t\tSUBTOTAL: $" + str(sub_total))
        print("\t\t\t\t\t\tTAX: $" + str(tax))
        print("\t\t\t\t\t\tTOTAL: $" + str(total))
