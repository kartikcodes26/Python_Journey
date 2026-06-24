# For-Loop

for i in range(1, 6): # excluding 6
    print(f"count = {i}")
    
for i in range(1, 10, 2): # Increment by 2 each time
    print(f"count = {i}")
    
kitchen = ["Knife", "Spoon", "Spatula", "Stove", "Exhaust"]
for element in kitchen:
    print(element, end = '\n')
    

#While-Loop
i = 0
while i <= 10:
    print(f"Count = {i}")
    i += 1

i = 0
while i <= 20:
    if i == 4:
        i += 1
        continue # Ignore everything below this
    if i == 15:
        break
    print(f"Count = {i}")
    i += 1