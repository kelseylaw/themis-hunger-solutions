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
            self.order_food(input)
        elif self.state == "is that all":
            self.order_complete(input)
        else:
            self.get_manager

    def greet(self):
        Burger.print_menu()
        print("\n")
        Fries.print_menu()
        self.speak.playMP3("greet")
        self.state = "menu_item"
        print("\nYOUR ORDER:\n")

    def prompt_for_menu_item(self):
        self.speak.playMP3("prompt_for_menu_item")

    def prompt_for_addition(self):
        self.speak.playMP3("prompt_for_addition")

    def prompt_for_removal(self):
        self.speak.playMP3("prompt_for_removal")

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

    def add_to_item(self, input):
        item = self.order[-1]
        additional_item = False
        for ingredient in item.possible_ingredients:
            if ingredient in input:
                item.add_addition(ingredient)
                additional_item = True
        return

    def remove_from_item(self, input):
        item = self.order[-1]
        removed_item = False
        for ingredient in item.possible_ingredients:
            if ingredient in input:
                item.add_removal(ingredient)
                removed_item = True
        if removed_item is False:
            self.speak.playMP3("anything_else")
        return

    def order_complete(self, input):
        if search_affirmative(input):
            self.farewell()
            sys.exit()
        elif search_negative(input):
            self.prompt_for_menu_item()
            self.state = "menu_item"
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

    def order_food(self, input):
        items = all_food_items(input)
        ingredients = all_ingredients(input)
        directors = all_with(input)
        directors.extend(all_without(input))
        print("REEEEEEE\n" + str(directors))
        directors_applied = self.directors_applied(directors, ingredients)
        if len(items) > 0:
            i = 1
            next_item = len(input)
            for item in items:
                if(i < len(items)):
                    next_item = items[i].start()
                self.try_to_add_item(item.group())
                j = 0
                while j < len(ingredients):
                    if item.start() < ingredients[j].start() < next_item:
                        print(directors_applied)
                        if search_without(self.director(directors_applied[j],directors)):
                            self.remove_from_item(ingredients[j].group(0))
                        else:
                            self.add_to_item(ingredients[j].group(0))
                    j += 1
                i += 1
        else:
            self.state = "is that all"
            self.confirm_order()
            return
        self.speak.playMP3("anything_else")

    def director(self, location, directors):
        for director in directors:
            if director.start() == location:
                print(director)
                return director.group(0)


    def locations(self,directors):
        if directors:
            result = []
            for d in directors:
                result.append(d.start())
            print("RESULT IS: " + str(result))
            return result
        else:
            return []

    def directors_applied(self, directors, ingredients):
        result = []
        director_locations = self.locations(directors)
        ingredient_locations = self.locations(ingredients)
        i = 0
        while i < len(ingredients):
            inner_result = []
            for location in director_locations:
                print("HERE THE DIRECTOR LOCATIONS ARE:" + str(director_locations))
                if ingredient_locations[i] > location:
                    inner_result.append(location)
            result.append(max(inner_result)) if len(inner_result) > 0 else result.append(0)
            i += 1
        print(str(result))
        return result

    def get_manager(self):
        self.speak.playMP3("get_manager")
        sys.exit()

    def say(self, string):
        print(string)
