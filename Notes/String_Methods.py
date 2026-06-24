line = "Kartik is a programmer"

print(line.lower()) # All lower
print(line.upper()) # All Upper
print(line.title()) # First letter of each word upper
print(line.capitalize()) # Very first letter capital
print(line.swapcase()) # Upper <---> Lower

# Searching

print(line.startswith("Kartik"))
print(line.endswith("End"))

print(line.find("programmer"))
print(line.find("coder")) # -1 if not found

names = "Kartik,Roshan,Aarav,Manisha,Rahul"
names_sep = names.split(',') # Split by commas and store in a new list
print(names_sep)

names_joined = "-".join(names_sep)
print(names_joined)


name = "Kartik Choudhary"
new_name = name.replace("Kartik", "Aarav") # From, To
print(new_name)

# Structural Validation
print("123456".isdigit()) # Entirely Numbers
print("123456f".isdigit())
print("hello1".isalpha()) # Is just letters
print("hello".isalpha())
print("1hello".isalnum()) # Letters or numbers
print("low".islower()) # Is it all lowercase



