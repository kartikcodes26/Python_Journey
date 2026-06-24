def get_number():
    while True:
        try:
            a = int(input("Enter your number : "))
        except ValueError:
            print("Enter a valid number")
        except NameError:
            pass # Dont do anything, go back to try
        else:
            return a
            

# try, if try fails go to except, if try passes go to else

print(f"Your number is {get_number()}")