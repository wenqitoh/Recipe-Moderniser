"""Get the ingredients required to make the recipe,
adding them to a list and printing the list at the end
Created by Wen-Qi Toh
30/6/21"""


# set up loop to add items until exit code 'X' is typed
# ask user for ingredient name
def not_blank(question):
    error = "Please enter an ingredient name (cannot be blank)"
    valid = False

    while not valid:
        response = input(question)

        if not response:    # checks if response has been entered
            print(error)
        else:   # where no error has been found
            return response


# Main Routine
ingredients = []    # create blank ingredient list
valid_list = False
while not valid_list:
    ingredient_name = not_blank("Enter ingredient name and enter 'X' to exit: ")\
        .title()    # Calls the not_blank function and provides the question
    if ingredient_name != "X":
        ingredients.append(ingredient_name) # if exit code not entered add ingredient to list
    else:
        if len(ingredients) < 2:    # check that list contains 2 items
            print("Please enter at least two ingredients")
        else:
            valid_list = True   # if list contains 2 items break out of loop
            print("Here are your ingredients:\n{}".format(ingredients))
