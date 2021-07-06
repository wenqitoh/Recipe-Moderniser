"""v02 get recipe name from user, checking that input doesn't
    contain numbers and isn't left blank, and allowing user to
    allow/disallow digits
    created by Wen-Qi Toh
    22/6/21"""


# function name to get recipe name and check it contains no digits/blanks
def not_blank(question, error_msg, num_ok ):
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


# main routine
source = not_blank("Where is your recipe from?",
                   "The recipe source can't be blank!",  # customize error message eg. to include mention of numbers
                   True)  # Can change this to 'False' to disallow numbers in URL - need to change error msg above too
print("The recipe is from {}.".format(source))
