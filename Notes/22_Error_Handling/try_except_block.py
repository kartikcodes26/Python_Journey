try:
    f = open('ex1.txt')
    var = new_var
except FileNotFoundError:
    print("File Not Found, Sorry")
except NameError:
    print("The Syntax is wrong")
