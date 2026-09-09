# with open('example.txt', 'r') as f:
#     # print(f.read())
#     for line in f:
#         print(line, end = '')


# Read Files in Batches
# batch = 20

# with open('example.txt', 'r') as f:
#     line = f.read(batch)

#     while(len(line) > 0):
#         print(line, end = '')

#         # f.seek(0)
#         line = f.read(batch)

# Writing in a file
with open('output.txt', 'a') as f:
    f.write("Wow")
    f.seek(0)
    f.write('x')
