"""Ask user for number of servings in recipe and
number of servings desired and then calculate the
scale factor
Created by Wen-Qi Toh
28/6/21"""


# get serving size
serving_size = float(input("How many servings does the recipe make?"))
# get desired number of servings
desired_size = float(input("How many servings needed?"))
# calculate scale factor
scale_factor = desired_size / serving_size

print("Scale factor is {}".format(scale_factor))
