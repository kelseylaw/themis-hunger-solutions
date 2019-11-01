import random

food_items = [
    "Burger",
    "Chicken Burger",
    "Veggie Burger",
    "Fries",
]

positive_confirmation = [
    "absolutely",
    "great_choice",
    "okay",
    "sure",
]

response_negative = [
    "no",
    "nope",
    "nah",
    "negative",
]

response_affirmative = [
    "affirmative",
    "all right",
    "alright",
    "amen",
    "definitely",
    "certainly",
    "fine",
    "good",
    "nuh uh",
    "of course",
    "okay",
    "right",
    "true",
    "yes",
    "yeah",
    "yup",
    "yep"
]

response_hostile = [
    "bad",
    "darn",
    "horrible",
    "manager",
    "shut up",
    "supervisor"
    "oh my god",
    "terrible",
    "this isn't working",
    "what the heck",
]

response_with = [
    "add",
    "extra",
    "include",
    "including",
    "on",
    "over",
    "with",
]

response_without = [
    "no",
    "take out",
    "without",
]

def random_confirmation():
    num = random.randrange(len(positive_confirmation))
    return positive_confirmation[num]

def search_without(input):
    for without in response_without:
        if without in input:
            return True
    return False

def search_with(input):
    for with_word in response_with:
        if with_word in input:
            return True
    return False

def search_negative(input):
    for negative in response_negative:
        if negative in input:
            return True
    return False

def search_affirmative(input):
    for affirmative in response_affirmative:
        if affirmative in input:
            return True
    return False

def search_hostile(input):
    for affirmative in response_affirmative:
        if affirmative in input:
            return True
    return False

def search_food_item(input):
    for item in food_items:
        if item in input:
            return True
    return False


