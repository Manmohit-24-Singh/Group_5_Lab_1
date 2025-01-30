import json

def set_size_to_42(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "size":
                obj[key] = 42
            else:
                set_size_to_42(value)
    elif isinstance(obj, list):
        for item in obj:
            set_size_to_42(item)

with open('/Users/anhadwander/School/Winter 2025/ENSF 338/Lab 1/lab_data/large-file.json', 'r') as f:
        data = json.load(f)

for record in data:
        set_size_to_42(record)

data.reverse()

with open('/Users/anhadwander/School/Winter 2025/ENSF 338/Lab 1/output.2.3.json', 'w') as f:
        json.dump(data, f, indent=2)




