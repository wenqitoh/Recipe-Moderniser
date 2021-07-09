"""Further version of ingredient splitter which splits the ingredients from one lin of input
into quantity, unit, and ingredient
version 3 - testing on full recipe
created by Wen-Qi Toh
7/7/21"""

import re   # this is the Regular Expression module

# ingredient has mixed fraction followed by unit and ingredient
full_recipe = [
    "1 1/2 ml flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 tablespoons white sugar",
    "1 3/4 cups flour",
    "1.5 tsp baking powder",
    "pinch of cinnamon"
    ]

# the regex format below is expecting: number <space> number
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
        amount = mixed_num.replace(" ","+")

        # changes the string into a float using python's evaluation method
        amount = eval(amount)

        # get unit and ingredient
        compile_regex = re.compile(mixed_regex)
        # compiles the regex into a string object - so we can search for patterns

        unit_ingredient = re.split(compile_regex, recipe_line)
        # produces the recipe line unit and amount as a list

        unit_ingredient = (unit_ingredient[1]).strip()
        # removes the extra white space before and after the unit
        # 2nd element in list, converting into a string

    else:
        # splits the line at the first space
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])    # convert amount to float if possible
        except NameError:
            amount = get_amount[0]

        unit_ingredient = get_amount[1]

# get unit and ingredient
# splits the string into a list containing just the unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)

    unit = get_unit[0]  # making the 1st item in the list 'unit'
    ingredient = get_unit[1]    # making the 2nd item in the list 'ingredient'

    # all 3 elements of original reciple line now broken into the 3 variables
    print("{} {} {}".format(amount, unit, ingredient))
