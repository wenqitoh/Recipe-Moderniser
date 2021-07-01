"""04 v2 evaluates fractions for scale factor, rounds scaled amount,
and prevents entry of digits in ingredient name
Created by Wen-Qi Toh
30/06/21"""


# ask user for ingredient name
def not_blank(question):

    valid = False

    while not valid:
        response = input(question)

        if not response:    # checks if response has been entered
            print("Please enter an ingredient name (cannot be blank)")  # and if not, generates message(left)
        elif not response.isalpha():    # checks to ensure the ingredient name contains no digits
            print("The ingredient name can't contain digits.")
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
scale_factor = eval(input("Scale Factor: "))    # eval allows the scale factor to be entered as fraction eg. 1/3
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

            # remove decimal point for whole numbers
            if scaled % 1 == 0:
                scaled = int(scaled)
            elif scaled * 10 % 1 == 0:
                scaled = "{:.1f}".format(scaled)    # 1dp (removes 2nd dp if it is 0 eg. 50)
            else:
                scaled = "{:.2f}".format(scaled)    # 2dp

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
