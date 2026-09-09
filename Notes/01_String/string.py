s = "  Hello, Python World! Hello 123  "

# Basic
i = 0
len(s)              # length of string
s[i]                # character at index i
s[a:b]              # substring from a to b-1
s[::-1]             # reverse string

# Case
s.upper()           # convert to uppercase
s.lower()           # convert to lowercase
s.title()           # first letter of each word uppercase
s.capitalize()      # first character uppercase

# Whitespace
s.strip()           # remove leading + trailing whitespace
s.lstrip()          # remove leading whitespace
s.rstrip()          # remove trailing whitespace

# Search
s.find("x")         # index of first occurrence, -1 if absent
s.count("x")        # count occurrences
s.startswith("x")   # check if starts with x
s.endswith("x")     # check if ends with x

# Modification
s.replace("x", "y") # replace x with y

# Split / Join
s.split()           # string → list of words
s.split(",")        # split using comma as separator
" ".join(list)      # list → string

# Character checks
s.isalpha()         # only letters?
s.isdigit()         # only digits?
s.isalnum()         # only letters/digits?
s.isspace()         # only whitespace?
s.islower()         # all lowercase?
s.isupper()         # all uppercase?

# Conversion
str(x)              # value → string
int(s)              # string → integer
float(s)            # string → float

# Iteration
for ch in s:        # iterate through characters
    ...

for i, ch in enumerate(s): # index + character
    ...

# Character ↔ ASCII/Unicode
ord('a')            # character → Unicode number
chr(97)             # Unicode number → character

# Built-ins
len(s)              # length
sorted(s)           # sorted characters → list
min(s)              # smallest character
max(s)              # largest character

# Membership
"x" in s            # check if x exists
"x" not in s        # check if x doesn't exist

# Formatting
f"Hello {name}"     # insert variables into string
