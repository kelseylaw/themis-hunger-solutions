import re
import random

food_items = [
    "cheeseburger",
    "chicken burger",
    "veggie burger",
    "yam fries"
    "curly fries"
    "fries",
]

positive_confirmation = [
    "absolutely",
    "great_choice",
    "okay",
    "sure",
]

food_ingredients = [
    "beef patty",
    "chicken patty",
    "veggie patty",
    "bacon",
    "cheese",
    "lettuce",
    "tomato",
    "ketchup",
    "mayo",
    "mustard",
    "pickles",
    "onions",
    "peppers",
    "salt",
    "gravy",
    "ketchup"
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
    "that's all",
    "that's fine",
    "that's it",
    "that's everything",
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
    " on",
    " over",
    "with",
]

response_without = [
    " no",
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
    for hostile in response_hostile:
        if hostile in input:
            return True
    return False

def search_food_item(input):
    for item in food_items:
        if item in input:
            return True
    return False

def all_food_items(input):
    results = []
    for item in food_items:
        for m in re.finditer(item, input):
            results.append(m)
    return results

def all_ingredients(input):
    results = []
    for ingredient in food_ingredients:
        for m in re.finditer(ingredient, input):
            results.append(m)
    return results

def all_with(input):
    results = []
    for item in response_with:
        for m in re.finditer(item, input):
            results.append(m)
    return results

def all_without(input):
    results = []
    for item in response_without:
        for m in re.finditer(item, input):
            results.append(m)
    return results

