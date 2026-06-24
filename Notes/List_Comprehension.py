num = [1,2,3,4,5,6,7]
cube = []

for element in num:
    cube.append(element * element * element)
    
print(cube)

smart_cube = [x * x * x for x in num]
print(smart_cube)

even_cube = [x*x*x for x in num if x % 2 == 0]
print(even_cube)