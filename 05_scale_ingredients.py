"""04 get the scale factor, then the ingredient and amount required for each
then add the ingredients with their scaled amounts into a list to be printed
at the end.
Created by Wen-Qi Toh
30/06/21"""


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


# number checking function
def num_check(response):
    error = "You must enter a number more than 0"
    valid = False
    while not valid:
        try:
            if response <= 0:
                response = float(input("Please enter a number more than 0: "))
            else:
                return response
        except ValueError:
            print(error)


# Main Routine
# replace line below with component 3 (number checking function) in due course
scale_factor = float(input("Scale Factor: "))
ingredients = []    # create blank ingredient list
valid_list = False


while not valid_list:

    amount = input("Enter amount (or 'X' to exit): ")
    if amount.upper() != "X":
        if not amount or not amount.isdigit():  # won't allow blank or strings
            print("Please enter a valid number")
        else:
            amount = float(amount)  # converts amount to float
            scaled = num_check(amount) * scale_factor
            ingredient_name = not_blank("Enter ingredient name: ")\
                .title()    # calls the not_blank function and provides the question
            ingredients.append("{} units {}".format(scaled, ingredient_name))   # puts both elements on same line

    elif len(ingredients) > 1:
        valid_list = True   # if list contains at least 2 items break out of loop
        print("Here are your ingredients: ")
        for ingredient in ingredients:
            print(ingredient)   # output list
    else:
        print("Please enter at least 2 ingredients")
