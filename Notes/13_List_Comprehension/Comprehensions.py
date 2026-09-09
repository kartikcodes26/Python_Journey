nums = [1, 2,3,4, 5, 6,7, 9]

# I want the whole list copied as it is
new_nums = [n for n in nums]
print(new_nums)

# I want n * n for each n in nums
nums_squared = [n * n for n in nums]
print(nums_squared)

# I want only even items
nums_even = [n for n in nums if n % 2 == 0]
print(nums_even)

# Nested Loops
grades = [(letter, num) for letter in "abcd" for num in range(4)]
print(grades)

# Zip function
names = ["Asus", "Samsung", "Apple", "Microsoft"]
products = ['Vivobook', "Notebook", "Macbook", "Surface"]
print(list(zip(names, products)))

# Make a dictionary
my_map = {name : product for name, product in zip(names, products) if name != "Apple"}
print(my_map)

#set
marks = [1, 2, 3, 1, 1, 1, 1, 1]
nodup = set(m for m in marks)
print(nodup)

