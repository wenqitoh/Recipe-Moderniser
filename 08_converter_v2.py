"""08 v2 combined converter using a function.
coverts amount to mls and (if possible) coverts mls to gms
If it is, convert to mLs, otherwise leave as is.
version 2
Created by Wen-Qi Toh
9/7/21"""

import csv
def general_converter(amount, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount *= float(factor) / conversion_factor
        converted = "yes"
    else:
        converted = "no"

    return [amount, converted]

def unit_checker():
    # ask user for unit
    unit_to_check = input("Unit? ")

    # abbreviations list
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbsp", "Tablespoon", "T", "tbs"]
    ounce = ["oz", "fluid ounce", "fl oz"]
    cup = ["c", "cups", "cups"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl", "qt"]
    ml = ["milliliter", "millilitre", "cc", "ml"]
    litre = ["L", "litre", "liter"]
    decilitre = ["decilitre", "deciliter", "dL"]
    pound = ["lb", "lbs", "#"]

    if not unit_to_check:   # if left blank
        # no need to print but still need to return
        return unit_to_check
    elif unit_to_check in teaspoon:
        return "teaspoon"
    elif unit_to_check in tablespoon:
        return "tablespoon"
    elif unit_to_check in ounce:
        return "ounce"
    elif unit_to_check in cup:
        return "cup"
    elif unit_to_check in pint:
        return "pint"
    elif unit_to_check in quart:
        return "quart"
    elif unit_to_check in ml:
        return "ml"
    elif unit_to_check in litre:
        return "litre"
    elif unit_to_check in decilitre:
        return "decilitre"
    elif unit_to_check in pound:
        return "pound"
    else:
        return unit_to_check    # if the unit is not on list

# main routine
# set up dictionary
unit_dict = {
    "teaspoon": 5,
    "tablespoon": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "litre": 1000,
    "decilitre": 100,
    "pound": 454,
    "ml": 1
}

# set up dictionary of conversion factors for ingredients
# open file using appropriately named variable
groceries = open('01_ingredients_ml_to_g.csv')

# read data from above into a list
csv_groceries = csv.reader(groceries)

# create a dictionary to hold the data
food_dictionary = {}

# add the data from the list into dictionary
# (first item in row is key, and next is definition)
for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

    # get items
complete_list = False
while not complete_list:
    # ask use for amount
    amount = eval(input("How much? "))

    # get unit and change to match dictionary
    unit = unit_checker()
    # get ingredient and change to match dictionary
    ingredient = input("Ingredient: ").lower()
    # convert to mls if possible
    amount = general_converter(amount, unit, unit_dict, 1)

    # if converted to mls, try convert to gms
    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        # if ingredient is in list, convert to gms
        if amount_2[1] == "yes":
            print(round(amount_2[0], 1), "grams")
        # if ingredient is not in conversion dict, leave as ml
        else:
            print(round(amount[0], 1), "mls (ingredient not in conversion dictionary")
    else:
        print(round(amount[0], 1), unit, "(unable to convert to grams)")
