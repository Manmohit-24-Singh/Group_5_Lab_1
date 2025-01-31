import json

def size_42(n):
    if type(n) == dict:
        for key, value in n.items():
            if key == "size":
                n[key] = 42
            else:
                size_42(value)
    elif type(n) == list:
        for i in n:
            size_42(i)

with open('large-file.json', 'r') as lrg_data:
        data = json.load(lrg_data)

for i in data:
        size_42(i)

rvrs_data = data[::-1]

with open('output.2.3.json', 'w') as lrg_data_updt:
        json.dump(rvrs_data, lrg_data_updt, indent = 2)