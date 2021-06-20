""" v01 get recipe name from user, checking that input doesn't
    contain numbers and isn't left blank.
    created by Wen-Qi Toh
    16/6/21"""

# main routine
recipe_name = (input("What is the name of your recipe?"))

# error message - if name is blank or has digits
error = "Your recipe is blank or has a number in it! Please try again."

# check each character in the recipe name for digits
contains_number = False
for letter in recipe_name:
    if letter.isdigit():
        contains_number = True

# print error message if recipe name has digits/blank
if not recipe_name or contains_number:
    print(error)

