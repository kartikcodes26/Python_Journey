import json

with open('toy.json', 'r') as f:
    data = json.load(f)

# print(type(data['student']))
print(data['student']['skills'][1])

del data['student']['age']
print(json.dumps(data, indent = 4))
