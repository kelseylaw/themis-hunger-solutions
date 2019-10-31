class Order:

    def __init__(self):
        self.state = "greet"
        self.order = []
        self.greet()

    def input(self, input):
        if self.state == "greet":
            self.state = "menu_item"
        elif self.state == "menu_item":
            self.add_item_to_order(input)
        elif self.state == "additions":
            self.add_to_item(input)
        elif self.state == "removals":
            self.remove_from_item(input)
        elif self.state == "is that all":
            self.order_complete(input)
        else:
            self.get_manager


    def greet(self):
        self.say("Welcome to Themis-- Where customer success comes first. What can I get for you?")

    def prompt_for_menu_item(self):
        self.say("anything else for you today?")

    def prompt_for_addition(self):
        self.say("anything extra on that?")

    def prompt_for_addition(self):
        self.say("need anything removed from that?")

    def prompt_for_end_order(self):
        self.confirm_order()
        self.say("is that everything?")

    def farewell(self):
        self.say("Thank you for choosing Themis hunger solutions, stay fit and have fun")


    def add_item_to_order(self, input):
        if "burger" in input:
            state
            if "veggie" in input:
                self.order.append(VeggieBurger())
            if "chicken" in input:
                self.order.append(ChickenBurger())
            else:
                self.order.append(BeefBurger())
        elif "fries" in input:
            if "curly" in input:
                self.order.append(CurlyFries())
            if "yam" in input:
                self.order.append(YamFries())
            else:
                self.order.append(RegularFries())
        else:
            self.say("Let me get my manager to help you")


    def add_to_item(self, input):
        return

    def remove_from_item(self, input):
        return

    def order_complete(self, input):
        self.farewell()
        del self
        return

    def confirm_order(self):
        self.say(self.order_string)

    def order_string(self):
        return

    def get_manager(self):
        self.say("Let me get my manager to help you")

    def say(self, string):
        print(string)

order()
Order.input("hello")
Burger("small")