# Numbers
x = 10
y = 3

# Basic arithmetic
x + y              # addition
x - y              # subtraction
x * y              # multiplication
x / y              # normal division → float
x // y             # floor division → removes decimal
x % y              # remainder / modulo
x ** y             # exponent / power

# Order of operations
x + y * 2          # multiplication happens first
(x + y) * 2        # parentheses happen first

# Assignment operators
x += 1             # x = x + 1
x -= 1             # x = x - 1
x *= 2             # x = x * 2
x /= 2             # x = x / 2
x //= 2            # x = x // 2
x %= 2             # x = x % 2
x **= 2            # x = x ** 2

# Useful numeric functions
abs(-10)            # absolute value → 10
round(3.75)         # round to nearest integer
round(3.14159, 2)   # round to 2 decimal places

# Comparison operators
x == y              # equal?
x != y              # not equal?
x > y               # greater than?
x < y               # less than?
x >= y              # greater than or equal?
x <= y              # less than or equal?

# Type
type(x)             # check data type

# Type conversion / casting
int(3.14)           # float → integer
float(10)           # integer → float
int("100")           # string → integer
float("3.14")       # string → float
str(100)            # number → string

# Even / odd ⭐
x % 2 == 0          # even
x % 2 != 0          # odd

# Useful built-ins
abs(x)              # absolute value
round(x)            # rounding
pow(x, y)           # x raised to y
min(x, y)           # smaller value
max(x, y)           # larger value
