"""recipe moderniser - full program v9
changing format to meet PEP8 standards
created by Wen-Qi Toh
11/7/21"""

# modules to be used
import csv


# FUNCTIONS
import re


# FUNCTIONS
# function to round numbers appropriately
def round_amount(amount_to_round):
    if amount_to_round % 1 == 0:    # finds whole numbers
        amount_to_round = int(amount_to_round)  # and converts to integer
    elif amount_to_round * 10 % 1 == 0:  # finds numbers with 1dp eg. 0.5
        amount_to_round = "{:.1f}".format(amount_to_round)  # and rounds to 1dp
    else:
        amount_to_round = "{:.2f}".format(amount_to_round)
        # everything else rounded to 2dp

    return amount_to_round


def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False

    while not valid:
        number = False  # initial assumption - name contains no digits
        response = input(question)

        if not num_ok:  # set to False
            for letter in response:   # Check for digits in recipe name
                if letter.isdigit():  # Tests for True - by default
                    number = True  # sets true if any digit found

        if not response or number is True:  # error for blank name/digit
            print(error)

        else:  # no error found
            return response  # return bypasses the need to set 'valid' to True


# number checking function
# gets the sale factor - which must be a number
def num_check(question):
    valid = False
    error = "You must enter a number more than 0"
    while not valid:
        response = input(question)
        try:
            response = eval(response)
            response = float(response)
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)
        except NameError:
            print(error)
        except SyntaxError:
            print(error)


def get_scale_factor():
    keep_scale_factor = False
    # get serving size and checking it is a number
    serving_size = num_check("\nHow many servings does the recipe make? "
                             "Enter '1' if unsure: ")
    # get desired number of servings
    desired_size = num_check("How many servings needed? Enter '1' if unsure: ")
    # calculate scale factor
    factor = desired_size / serving_size

    while not keep_scale_factor:
        # warn user if scale factor >4 or <0.25
        if factor < 0.25:
            print("Scale factor is:{}".format(factor))
            print("Warning: this scale factor is very small and you may"
                  " \nstruggle to accurately weigh the ingredients. "
                  "Please consider using a larger \nscale factor"
                  "and freezing the left-overs.")
            change_scale_factor = input("Press <enter> to continue with this "
                                        "scale factor, or any other key + "
                                        "<enter> to change this scale factor.")
            if not change_scale_factor:
                break
            else:
                factor = get_scale_factor()
        elif factor > 4:
            print("Scale factor is:{}".format(factor))
            print("Warning: this scale factor is quite large and you may have "
                  "\ndifficulty with mixing bowl volumes and oven space."
                  " \nPlease consider using a smaller scale factor and making "
                  "more than one batch.")
            change_scale_factor = input("Press <enter> to continue with this "
                                        "scale factor, or any other key + "
                                        "<enter> to change this scale factor.")
            if not change_scale_factor:
                break
        else:
            factor = get_scale_factor()

    return factor


# Function to get (and check) amount, unit and ingredient
def get_all_ingredients():
    ingredients = []    # create blank ingredient list
    valid_list = False
    print("\nEnter ingredients on one line -  quantity, unit "
          "then name (or enter 'X' to exit): \n")
    line_number = 1     # to make entering ingredient easier to follow
    while not valid_list:
        # calls the not_blank function and provides the question
        ingredient_name = not_blank("\nIngredient line {}: "
                                    .format(line_number),
                                    "ingredient can't be blank",
                                    True).lower()
        if ingredient_name != "x":
            ingredients.append(ingredient_name)
            # if exit code not entered add ingredient to list
            # add line number
            line_number = line_number + 1
        else:
            if len(ingredients) < 2:    # check that list contains 2 items
                print("Please enter at least two ingredients")
            else:
                return ingredients  # output list


# converter 8 v2 added
def general_converter(amount2, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount2 *= float(factor) / conversion_factor
        converted = True
    else:
        converted = False

    return [amount2, converted]


def unit_checker(raw_unit):
    # ask user for unit
    unit_to_check = raw_unit

    # abbreviations list
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbsp", "Tablespoon", "T", "tbs"]
    ounce = ["oz", "fluid ounce", "fl oz", "ounce", "ounces", "oz."]
    cup = ["c", "cups", "cups"]
    pint = ["p", "pt", "fl pt", "pt.", "pint", "pints"]
    quart = ["q", "qt", "fl", "qt"]
    ml = ["milliliter", "millilitre", "cc", "ml"]
    litre = ["L", "litre", "liter"]
    decilitre = ["decilitre", "deciliter", "dL"]
    pound = ["lb", "lbs", "#", "pound", "pounds", "lb.", "lbs."]
    grams = ["g", "gram", "gms", "grams", "gm"]

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
    elif unit_to_check in grams:
        return "gm"
    else:
        return unit_to_check    # if the unit is not on list


# instructions for first time users - optional
def instructions():
    print("\n* * * * * * * * * * INSTRUCTIONS * * * * * * * * * *\n")
    print("This program converts recipe ingredients to mls / grams and "
          "also allows \nusers to upsize or downsize ingredients.\n")
    print("This program will ask for the source of the recipe - we recommend"
          "\ntyping in the URL where you found the recipe or the book where \n"
          "it is from so that you can refer back to the original if necessary")
    print()
    print("The program also asks for the number of servings. "
          "If you are not sure,\ntype '1'. Then when it asks you for servings "
          "required, you can increase\n or decrease the amount (eg. 2 or 1/2) "
          "and the program will scale the\n ingredient amounts for you.\n")
    print("Note that you can use fractions if needed. For example, write\n"
          "one half as 1/2 and one and three quarters as 1 3/4\n")
    print("Please only type in 1 ingredient per line, if a recipe says \n"
          "'butter or margarine', choose ONE ingredient, either butter \n"
          "or margarine.\n")
    print("Lastly, all lines should start with a number / fraction unless\n"
          "no number is given <eg: a pinch of salt.")
    print("\n* * * * * * * * * \n")


# MAIN ROUTINE
# main routine from converter 2
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
    "ml": 1,
    "gm": 1
}

# to check for errors in numeric entry of quantity
problem = False
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


# set up list to hold 'modernised' ingredients
modernised_recipe = []

# providing option for new user to get instructions
print("* * * * * * * * * * Welcome to the Great Recipe Moderniser * * * * *"
      " * * * * *\n")
get_instructions = input("Press <enter> to get instructions, or any other key "
                         "+ <enter>\n if you are familiar with this program: ")
if not get_instructions:
    instructions()
else:
    print()
# get recipe name and check it is not blank and contains no numbers
recipe_name = not_blank("What is the name of your recipe?",
                        "the recipe name can't be blank or contain numbers!",
                        False)
print("The recipe is for {}".format(recipe_name))
# get recipe source and check it's not blank - numbers OK
# customize error message eg. to include mention of numbers
source = not_blank("Where is your recipe from?",
                   "The recipe source can't be blank!",
                   True)  # 'False' to disallow numbers in name
print("The recipe is from {}".format(source))
# get serving sizes and desired number of servings
scale_factor = get_scale_factor()
# get ingredients
full_recipe = get_all_ingredients()

# split each line of the recipe into amount, unit and ingredient
# the regex format below is expecting: number <space> number
# need the r before docstring to make it a raw string rather
# than literal string (PEP8)
mixed_regex = r"\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, /d{1,3} allows 1-3 digits, /s for space, \/ for divide

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    # get amount
    if re.match(mixed_regex, recipe_line):  # checking for mixed fraction
        # get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()
        # .group returns the part of the string where there was a match

        # replace the space in the mixed number with '+' sign
        amount = mixed_num.replace(" ", "+")

        # changes the string into a float using python's evaluation method
        amount = eval(amount) * scale_factor

        # get unit and ingredient
        compile_regex = re.compile(mixed_regex)
        # compiles the regex into a string object-so we can search for patterns

        unit_ingredient = re.split(compile_regex, recipe_line)
        # produces the recipe line unit and amount as a list

        unit_ingredient = (unit_ingredient[1]).strip()
        # removes the extra white space before and after the unit
        # 2nd element in list, converting into a string

    else:
        # splits the line at the first space
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])  # convert amount to float if possible
            amount = amount * scale_factor

        except NameError:
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
        except SyntaxError:  # if amount unrecognised eg 1/ instead of 1/2
            problem = True
            modernised_recipe.append(recipe_line)
            continue
        unit_ingredient = get_amount[1]

# get unit and ingredient
# splits the string into a list containing just the unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)

    unit = get_unit[0]  # making the 1st item in the list 'unit'

    # count number of spaces in recipe line
    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:  # item has both unit and ingredient
        unit = get_unit[0]  # making the first item in the list 'unit'
        ingredient = get_unit[1]  # making the 2nd item in the list ingredient
        unit = unit_checker(unit)

        # if unit is already in grams, add to list
        if unit == "gms":
            modernised_recipe.append("{:.0f} gm {}".format(amount, ingredient))
            continue

        # convert to mls if possible: unit_dict gives amount in ml so-
        # conversion factor is 1
        amount = general_converter(amount, unit, unit_dict, 1)

        # if converted to mls is 'True', try convert to grams
        if amount[1]:   # food_dictionary gives gms for 250 ml so-
            # conversion factor = 250
            amount_2 = general_converter(amount[0], ingredient,
                                         food_dictionary, 250)
            if amount_2[1]:
                modernised_recipe.append("{:.0f} gm {}".format(amount_2[0],
                                                               ingredient))
                # if only 2 elements (no unit) then just 2 variables needed

            # if ingredient is not in food_dictionary, leave as ml
            else:
                modernised_recipe.append("{:.0f} ml {}".format(amount[0],
                                                               ingredient))

        # if unit is not in mls, leave line unchanged
        else:
            amount[0] = round_amount(amount[0])
            modernised_recipe.append("{} {} {}".format(amount[0], unit,
                                                       ingredient))
    # to cope with ingredients not requiring a unit value eg. "3 eggs"
    else:
        amount = round_amount(amount)
        ingredient = get_unit[0]
        modernised_recipe.append("{} {}".format(amount, ingredient))

# output modernised recipe
print("\n*************** {} ***************".format(recipe_name))
print("Source: {}\n".format(source))
print("**** Ingredients - scaled by factor of {} ****\n".format(scale_factor))
if problem:
    print("********** WARNING! **********")
    print("Some of the entries below may be incorrect as \n"
          "there were some problems processing some of your inputs.\n"
          "It is possible you may have typed a fraction incompletely.\n")
for item in modernised_recipe:
    print(item)
