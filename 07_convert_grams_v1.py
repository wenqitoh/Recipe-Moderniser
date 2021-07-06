"""Create a food dictionary from a csv file
version 1
created by Wen-Qi Toh
5/7/21"""

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

print(food_dictionary)
