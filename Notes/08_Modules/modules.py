# IMPORT A MODULE
import math                    # import entire module
math.sqrt(25)                  # access using module.method


# IMPORT SPECIFIC THING
from math import sqrt          # import only sqrt
sqrt(25)                       # use directly


# IMPORT WITH ALIAS
import math as m               # give module a shorter name
m.sqrt(25)


# SPECIFIC IMPORT WITH ALIAS
from math import sqrt as sq    # rename imported function
sq(25)


# MULTIPLE IMPORTS
import os, sys                 # import multiple modules


# COMMON STANDARD LIBRARY MODULES
import math                    # mathematical functions
import random                  # random values
import os                      # operating-system interaction
import sys                     # Python/system information
import datetime                # dates and times
import json                    # JSON data
import collections              # specialized containers
import itertools               # iterator tools
import re                      # regular expressions


# MATH MODULE
import math

math.sqrt(25)                  # square root
math.pow(2, 3)                 # 2^3
math.floor(3.9)                # round down
math.ceil(3.1)                 # round up
math.pi                        # π


# RANDOM MODULE
import random

random.randint(1, 10)          # random integer 1–10
random.choice([1, 2, 3])       # random element
random.shuffle(arr)            # shuffle list in-place


# OS MODULE
import os

os.getcwd()                     # current working directory
os.listdir()                    # files/folders in directory
os.path.exists("file.txt")     # check if path exists


# SYS MODULE
import sys

sys.version                     # Python version
sys.argv                        # command-line arguments
sys.path                        # places Python searches for modules


# YOUR OWN MODULE
# Suppose helper.py contains:
#
# def add(a, b):
#     return a + b

import helper

helper.add(2, 3)                # use function from helper.py


# __name__
if __name__ == "__main__":
    ...                         # runs only when file is executed directly


# HELP / INSPECTION
dir(math)                       # see names inside module
help(math.sqrt)                 # documentation for sqrt
