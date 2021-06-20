"""v02 get recipe name from user, checking that input doesn't
    contain numbers and isn't left blank.
    make into function
    created by Wen-Qi Toh
    17/6/21"""


# function name to get recipe name and check it contains no digits/blanks
def not_blank(question):
    error = "Your recipe name is blank or contains a digit."
    valid = False

    while not valid:
        number = False  # initial assumption - name contains no digits
        response = input(question)

        for letter in response:  # Check for digits in recipe name
            if letter.isdigit():  # Tests for True - by default
                number = True  # sets true if any digit found

        if not response or number == True:  # Generate error for blank name or digit
            print(error)

        else:  # no error found
            valid = True
            return response


# main routine
recipe_name = not_blank("What is the name of your recipe?")
print("you are making {}.".format(recipe_name))
