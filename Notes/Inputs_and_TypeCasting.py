# By default input is in a string
a = input("Enter your name : ")
print(type(a))

#In order to take inputs in other datatypes, We need to typecast it
age = int(input("Enter your age : "))
print(type(age))

#Handling boolean values
user_input  = input("Is Shop Open ? (yes/no) : ")

if user_input == "yes":
    is_open = True
else:
    is_open = False
    
print(f"{is_open = }")

#In one line

is_open = (user_input=="yes")
# if user_input is yes then shop is open, if anything else the shop is closed

