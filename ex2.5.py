import json
import timeit

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

time_taken = timeit.timeit(lambda: [size_42(i) for i in data], number=10)

avrg_time = time_taken / 10
print(f"Average time to modify 'size' values: {avrg_time:.6f} seconds")

rvrs_data = data[::-1]
with open('output.2.3.json', 'w') as lrg_data_updt:
    json.dump(rvrs_data, lrg_data_updt, indent=2)