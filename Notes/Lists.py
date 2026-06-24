a = [4, "Asus", 'z', False, 7.13]


for i in range(0, len(a)):
    print(type(a[i]))
    
for element in a:
    print(type(element))
    
    
print(a[1])
end = a.pop()
print(a)
print(end)

del a[2]
print(a)

print(len(a))

a.remove("Asus")

a.insert(2, "Laptop")
print(a)

a.append(True)
print(a)

sub_a = a[0:3]
print(sub_a)

print(sub_a[-3])

num = [2,4,5,6,9,0]
# reversed_nums = num[::-1] # Store reversed array
# print(reversed_nums)
# num[0:3] = [99,10,100] # Replace using ranges
# print(num)

for id, element in enumerate(num): # Hands you the tuple of index, element
    print(f"Index : {id}, {element}", end = "\n")
    

subjects = ["Physics", "Chemistry", "Mathematics"]
marks = [40,50,60]

for x,y in zip(subjects, marks):
    print(f"Subejct : {x}, Marks : {y}", end = "\n")
    
profit = 100
status = "Good" if profit > 200 else "Average"
print(status)