# FUNCTION
def greet():
    print("Hello")                  # define a function

greet()                             # call the function


# PARAMETERS / ARGUMENTS
def greet(name):
    print(f"Hello {name}")          # parameter

greet("Kartik")                     # argument


# MULTIPLE PARAMETERS
def add(a, b):
    return a + b                    # return result

result = add(10, 20)                # 30


# RETURN
def square(x):
    return x * x                    # send value back to caller

ans = square(5)                     # 25


# DEFAULT ARGUMENT
def greet(name="User"):
    print(f"Hello {name}")          # default value

greet()                             # Hello User
greet("Kartik")                     # Hello Kartik


# KEYWORD ARGUMENTS
def student(name, age):
    print(name, age)

student(age=17, name="Kartik")      # specify by parameter name


# POSITIONAL ARGUMENTS
student("Kartik", 17)               # matched by position


# *args
def add_all(*numbers):
    return sum(numbers)             # accepts any number of arguments

add_all(1, 2, 3, 4)                 # 10


# **kwargs
def info(**data):
    print(data)                     # accepts keyword arguments

info(name="Kartik", age=17)
# {'name': 'Kartik', 'age': 17}


# SCOPE
x = 10

def test():
    x = 20                          # local variable
    print(x)

test()                              # 20
print(x)                            # 10


# GLOBAL
x = 10

def change():
    global x
    x = 20                          # modifies global x


# FUNCTION AS VARIABLE
def square(x):
    return x * x

f = square                          # store function
f(5)                                # 25


# MULTIPLE RETURN VALUES
def operations(a, b):
    return a + b, a - b             # returns tuple

add, sub = operations(10, 3)        # unpack results


# DOCSTRING
def square(x):
    """Return the square of x."""
    return x * x
