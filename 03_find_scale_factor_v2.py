"""Ask user for number of servings in recipe and
number of servings desired and then calculate the
scale factor
Version 2 - uses number checking function to ensure input is a number
Created by Wen-Qi Toh
28/6/21"""


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

# get serving size
serving_size = num_check("How many servings does the recipe make?")
# get desired number of servings
desired_size = num_check("How many servings needed?")
# calculate scale factor
scale_factor = desired_size / serving_size

print("Scale factor is {}".format(scale_factor))
