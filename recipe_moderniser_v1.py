"""recipe moderniser - full program v1
Gets recipe name and source (component 1 + 2)
Version 1 - includes 'To Do' lists
created by Wen-Qi Toh
5/7/21"""

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


# get ingredients
# loop for each ingredient...
# get ingredient amount
# scale amount using scale factor
# get ingredient name and check it's not blank and does not contain numbers
# get unit
# convert to ml
# convert from ml to g
# add updated ingredients to list

# output modernised recipe

