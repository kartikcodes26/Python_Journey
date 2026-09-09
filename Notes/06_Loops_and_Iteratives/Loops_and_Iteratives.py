# FOR LOOP
for i in range(5):
    print(i)                    # 0 1 2 3 4


# range()
range(5)                        # 0 → 4
range(2, 6)                     # 2 → 5
range(2, 10, 2)                 # 2 4 6 8
range(10, 0, -1)                # 10 9 8 ... 1


# Iterate over a sequence
nums = [10, 20, 30]

for x in nums:
    print(x)                    # each element

for i, x in enumerate(nums):
    print(i, x)                 # index + element


# WHILE LOOP
i = 0

while i < 5:
    print(i)                    # repeat while condition is True
    i += 1                      # update condition


# BREAK
for x in range(10):
    if x == 5:
        break                    # immediately exit loop


# CONTINUE
for x in range(5):
    if x == 2:
        continue                 # skip current iteration
    print(x)


# ELSE with loops
for x in range(5):
    print(x)
else:
    print("Finished")            # runs if loop wasn't broken


# Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)              # loop inside loop


# Reverse iteration
for i in range(5, 0, -1):
    print(i)                     # 5 4 3 2 1


# Iterate over string
s = "Python"

for ch in s:
    print(ch)                    # each character


# Iterate over dictionary
d = {"a": 1, "b": 2}

for key in d:
    print(key)                   # keys

for value in d.values():
    print(value)                 # values

for key, value in d.items():
    print(key, value)            # key + value


# Membership + loop
for ch in "hello":
    if ch in "aeiou":
        print(ch)                # vowels


# Common DSA pattern
for i in range(len(nums)):
    print(nums[i])               # index-based traversal


# Accumulation
total = 0

for x in nums:
    total += x                   # sum elements


# Infinite while loop
while True:
    ...
    # break needed to exit
