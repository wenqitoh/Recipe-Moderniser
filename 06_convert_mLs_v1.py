"""06 v1 Get amount and unit for user then check if unit is in dictionary of units.
If it is, convert to mLs, otherwise leave as is.
Created by Wen-Qi Toh
1/7/21"""


# set up dictionary
unit_dict = {
    "tsp": 5,
    "tbsp": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

# ask use for amount
amount = eval(input("How much? "))

# ask user for unit
unit = input("Unit? ")

# check if unit is it dictionary
# if unit is in dictionary, convert to mL
# # if no unit given or unit is unknown, leave as is.
if unit in unit_dict:
    factor = unit_dict.get(unit)
    amount *= factor
    print("Amount in mL is: {}".format(amount))
else:
    print("{} is unchanged".format(amount))
