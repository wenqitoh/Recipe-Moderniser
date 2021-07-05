"""06 v2 Get amount and unit for user then check if unit is in dictionary of units.
If it is, convert to mLs, otherwise leave as is.
version 3 - Builds on v2 by referencing abbreviations of units to dictionary
Created by Wen-Qi Toh
5/7/21"""


def unit_checker():
    # ask user for unit
    unit_to_check = input("Unit? ")

    # abbreviations list
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbsp", "Tablespoon", "T", "tbs"]
    ounce = ["oz", "fluid ounce", "fl oz"]
    cup = ["c"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl", "qt"]
    ml = ["milliliter", "millilitre", "cc", "mL"]
    litre = ["L", "litre", "liter"]
    decilitre = ["decilitre", "deciliter", "dL"]
    pound = ["lb", "lbs", "#"]

    if not unit_to_check:   # if left blank
        print("You chose no unit")
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
    "pound": 454
}
complete_list = False
while not complete_list:
    # ask use for amount
    amount = eval(input("How much? "))

    # ask user for unit
    unit = unit_checker()

    # check if unit is it dictionary
    # if unit is in dictionary, convert to mL
    # # if no unit given or unit is unknown, leave as is.
    if unit in unit_dict:
        factor = unit_dict.get(unit)
        amount *= factor
        print("Amount in mL is: {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

#     another_item = input("\nPress <enter> to add another item \n"
#                          "or any key + <enter> to end:\n")
#     if not another_item:
#         continue
# else:
#     complete_list = True
