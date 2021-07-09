"""recipe moderniser - full program v3
incorporates ingredients list (component 4)
created by Wen-Qi Toh
8/7/21"""

# modules to be used
import csv


# FUNCTIONS
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

        if not response or number == True:  # Generate error for blank name or digit
            print(error)

        else:  # no error found
            return response  # return bypasses the need to set 'valid' to True

# number checking function
# gets the sale factor - which must be a number
def num_check(question):
    error = "You must enter a number more than 0"
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

def get_scale_factor():
    keep_scale_factor = False
    while not keep_scale_factor:
        # get serving size and checking it is a number
        serving_size = num_check("How many servings does the recipe make?")
        # get desired number of servings
        desired_size = num_check("How many servings needed?")
        # calculate scale factor
        scale_factor = desired_size / serving_size

        # warn user if scale factor >4 or <0.25
        if scale_factor <= 0.25:
            print("Scale factor is:{}".format(scale_factor))
            print("Warning: this scale factor is very small and you may"
                  " \nstruggle to accurately weigh the ingredients. Please consider using a larger \nscale factor"
                  "and freezing the left-overs.")
            change_scale_factor = input("Press <enter> to continue with this scale factor, "
                                        "or any other key + <enter> to change this scale factor.")
            if not change_scale_factor:
                keep_scale_factor = True
        elif scale_factor >= 4:
            print("Scale factor is:{}".format(scale_factor))
            print("Warning: this scale factor is quite large and you may have \ndifficulty with mixing bowl volumes and oven space."
                  " \nPlease consider using a smaller scale factor and making more than one batch.")
            change_scale_factor = input("Press <enter> to continue with this scale factor, "
                                        "or any other key + <enter> to change this scale factor.")
            if not change_scale_factor:
                keep_scale_factor = True
        else:
            keep_scale_factor = True

    return scale_factor


# Function to get (and check) amount, unit and ingredient
def get_all_ingredients():
    ingredients = []    # create blank ingredient list
    valid_list = False
    while not valid_list:
        # calls the not_blank function and provides the question
        ingredient_name = not_blank("\nEnter one ingredient - quantity, unit "
                                    "then name (or enter 'X' to exit): \n",
                                    "Ingredient can't be blank",
                                    True).title()    # Calls the not_blank function and provides the question
        if ingredient_name != "X":
            ingredients.append(ingredient_name) # if exit code not entered add ingredient to list
        else:
            if len(ingredients) < 2:    # check that list contains 2 items
                print("Please enter at least two ingredients")
            else:
                valid_list = True   # if list contains 2 items break out of loop
                return ingredients  # output list



# MAIN ROUTINE



# set up dictionaries


# set up list to hold 'modernised' ingredients


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
print(full_recipe)
# loop for each ingredient...
# get ingredient amount
# scale amount using scale factor
# get ingredient name and check it's not blank and does not contain numbers
# get unit
# convert to ml
# convert from ml to g
# add updated ingredients to list

# output modernised recipe

