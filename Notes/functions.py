def subtract(a, b):
    return a-b

print(subtract(9,9))

# Default values

def add(a,b,c= 0):
    return(a+b+c)

print(add(1,2))

def multireturn(x,y):
    return x,y

a,b = multireturn(2,4)
print(a)
print(b)
