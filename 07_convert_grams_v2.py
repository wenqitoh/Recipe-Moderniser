"""Take external csv file and convert amount in ml to g
version 2
created by Wen-Qi Toh
6/7/21"""

import csv

# open file using appropriately named variable
groceries = open('01_ingredients_ml_to_g.csv')

# read data from above into a list
csv_groceries = csv.reader(groceries)

# create a dictionary to hold the data
food_dictionary = {}

# add the data from the list into dictionary
# (first item in row is key, and next is definition)
for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

complete_list = False
while not complete_list:
    amount = eval(input("how much? "))

    # get ingredient and change it to match dictionary
    ingredient = input("Ingredient: ").lower()

    if ingredient in food_dictionary:
        factor = food_dictionary.get(ingredient)
        amount = amount * float(factor) / 250
        print("amount in g: {} \n".format(amount))
    else:
        print("{} is unchanged".format(amount))

    # # comment out loop for testing
    # another_item = input("\nPress <enter> to add another item \n"
    #                      "or any key + <enter> to end:\n")
    # if not another_item:
    #     continue
    # else:
    #     complete_list = True
