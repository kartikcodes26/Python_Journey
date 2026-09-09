# Syntax
sequence[start : stop : step]
# start → included
# stop  → excluded
# step  → jump size

s = "Python"

s[1:4]     # "yth"
s[:4]      # "Pyth"       → from beginning
s[2:]      # "thon"       → till end
s[:]       # "Python"     → copy
s[::2]     # "Pto"        → every 2nd
s[::-1]    # "nohtyP"     → reverse
s[-3:]     # "hon"        → last 3
s[:-2]     # "Pyth"       → exclude last 2

# Works on strings, lists, tuples, etc.
