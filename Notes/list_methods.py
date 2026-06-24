l = [4,5,1,2,0,0,8]

a = l.sort()
print(a)

b = sorted(l)
print(b)

b.sort(reverse = True)
print(b)

reversed(l)
print(l)

if 4 in l:
    print("Found it")
    
id = l.index(4)
print(id)

print(l.count(0))

scores = [15,20,25,30,35,40]
print(max(scores))
print(min(scores))
print(sum(scores))
print(f"average : {sum(scores) / len(scores)}")

names = ["karik", "Aarav", "Manisha", "Manisha", "Aarav"]
unique_names = set(names) # Only unique names
print(unique_names)

