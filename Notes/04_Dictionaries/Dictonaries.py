# Dictionary
student = {
    "name": "Kartik",
    "age": 17,
    "branch": "IT",
    "marks": 89
}

# Access
student["name"]                 # get value using key
student.get("name")             # get value safely
student.get("city", "Unknown")  # default if key doesn't exist

# Add / Update
student["city"] = "Mumbai"      # add new key-value pair
student["age"] = 18             # update existing value

# Remove
student.pop("age")              # remove key and return its value
student.popitem()               # remove last inserted key-value pair
del student["city"]             # delete key-value pair
student.clear()                 # remove everything

# Dictionary information
len(student)                    # number of key-value pairs
"name" in student               # check if key exists
"name" not in student           # check if key doesn't exist

# Keys / Values / Items
student.keys()                  # all keys
student.values()                # all values
student.items()                 # key-value pairs

# Iteration
for key in student:
    ...                         # iterate through keys

for value in student.values():
    ...                         # iterate through values

for key, value in student.items():
    ...                         # iterate through key + value

# Copy
new_student = student.copy()    # shallow copy

# Create dictionary
dict(name="Kartik", age=17)     # create using dict()

# Update multiple values
student.update({
    "age": 18,
    "marks": 92
})                              # add/update multiple pairs

# Set default
student.setdefault("city", "Mumbai") # add only if key doesn't exist


# Frequency counting
s = "banana"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# {'b': 1, 'a': 3, 'n': 2}
