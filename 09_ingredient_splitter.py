"""Initial version of an ingredient splitter which splits the ingredients from one lin of input
into quantity, unit, and ingredient
version 1
created by Wen-Qi Toh
6/7/21"""

import re   # this is the Regular Expression module

# ingredient has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 ml flour"  # change to input statement in due course

# the regex format below is expecting: number <space> number
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, /d{1,3} allows 1-3 digits, /s for space, \/ for divide

# testing to see if the recipe line matches the regular expression
if re.match(mixed_regex, recipe_line):
    print("true")
else:
    print("false")
