"""Ask user for number of servings in recipe and
number of servings desired and then calculate the
scale factor
Version 3 - account for numbers out of boundary (scale factor too large/small)
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


# def scale_check(number):
#     small_warning = "Warning: this scale factor is very small and you may struggle " \
#               "\nto accurately weigh the ingredients. " \
#               "\nPlease consider using a larger scale factor and freezing the left-overs."
#     big_warning = "Warning: this scale factor is quite large and you may " \
#                   "\nhave difficulty with mixing bowl volumes and oven space. " \
#                   "\nPlease consider using a smaller scale factor and making more than one batch."
#     valid = False
#     while not valid:
#         if scale_factor <= 0.2:
#             print(small_warning)
#         elif scale_factor >= 4.25:
#             print(big_warning)
#         else:
#             return number


# main routine
keep_scale_factor = False
while not keep_scale_factor:
    # get serving size and checking it is a number
    serving_size = num_check("How many servings does the recipe make?")
    # get desired number of servings
    desired_size = num_check("How many servings needed?")
    # calculate scale factor
    scale_factor = desired_size / serving_size

    # warn user if scale factor >4 or <0.25
    if scale_factor <= 0.25:
        print("Scale factor is:{}".format(scale_factor))
        print("Warning: this scale factor is very small and you may"
              " struggle to accurately weigh the ingredients. Please consider using a larger scale factor"
              "and freezing the left-overs.")
        change_scale_factor = input("Press <enter> to continue with this scale factor, "
                                    "or any other key + <enter> to change this scale factor.")
        if not change_scale_factor:
            keep_scale_factor = True
    elif scale_factor >= 4:
        print("Scale factor is:{}".format(scale_factor))
        print("Warning: this scale factor is quite large and you may have difficulty with mixing bowl volumes and oven space."
              " Please consider using a smaller scale factor and making more than one batch.")
        change_scale_factor = input("Press <enter> to continue with this scale factor, "
                                    "or any other key + <enter> to change this scale factor.")
        if not change_scale_factor:
            keep_scale_factor = True
    else:
        keep_scale_factor = True
        print("Scale factor is:{}".format(scale_factor))
