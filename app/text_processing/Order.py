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
        print("Welcome to Themis-- Where customer success comes first. What can I get for you today?")

    def prompt_for_menu_item(self):
        print("anything else for you today?")

    def prompt_for_addition(self):
        print("anything extra on that?")

    def prompt_for_addition(self):
        print("need anything removed from that?")

    def prompt_for_end_order(self):
        print("is that everything?")

    def farewell(self):
        print("Thank you for choosing Themis hunger solutions, stay fit and have fun")


    def add_item_to_order(self, input):
        return

    def add_to_item(self, input):
        return

    def remove_from_item(self, input):
        return

    def order_complete(self, input):

    def confirm_order(self):
        print(self.order_string)

    def order_string(self):
        return

    def get_manager(self):
        print("Let me get my manager to help you")

Order()
