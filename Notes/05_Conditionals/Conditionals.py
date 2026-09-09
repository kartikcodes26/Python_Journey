# Boolean
x = True
y = False

bool(x)                 # convert value to True/False

# Comparisons
x == y                  # equal?
x != y                  # not equal?
x > y                   # greater than?
x < y                   # less than?
x >= y                  # greater/equal?
x <= y                  # less/equal?

# Logical operators
x and y                # True only if BOTH are True
x or y                 # True if AT LEAST ONE is True
not x                  # reverses True ↔ False

# if
if condition:
    ...                 # execute if condition is True

# if / else
if condition:
    ...                 # True → this block
else:
    ...                 # False → this block

# if / elif / else
if condition1:
    ...                 # check first condition
elif condition2:
    ...                 # check if first was False
else:
    ...                 # if all conditions are False

# Nested conditions
if condition1:
    if condition2:
        ...             # if both conditions are True

# Membership
"x" in s               # check if x exists
"x" not in s           # check if x doesn't exist

# Identity
x is y                 # same object in memory?
x is not y             # different objects?

# Truthiness
bool(0)                # False
bool(1)                # True
bool("")               # False
bool("Hello")          # True
bool([])               # False
bool([1, 2])           # True
bool(None)             # False

# Common pattern
if value:
    ...                # runs if value is truthy

# Ternary / conditional expression
result = "Pass" if marks >= 40 else "Fail" # one-line if/else
