print("Hello, World")
print("My age is",17) #Separator String is " " by default

print("Your name is", end=" ")
print("kartik")

print("Your name is", end="\n")
print("kartik")

print("Your name is", end="----->")
print("kartik")

print("kartik", "Aarav", "Roshan", sep="--->") #Manuplate the separator string

name = "VivoBook"
print(f"My laptop name is {name}")

pi = 3.1415
x = 0.00000098
loss = 0.0401398

print(f"pi = {pi:.2f}") #Upto 2 decimal points
print(f"g = {x:.2e}") #scientific notation
print(f"loss = {loss:.3%}") # Multiply by 100 and show till 3 decimal points

# Debugging tricks

print(f"{pi = }")
print(f"{pi + x = }")


