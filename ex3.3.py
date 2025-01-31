import json
import matplotlib.pyplot as plt
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

data_1000 = data[:1000]

times = []
for i in range(1000):
    time_taken = timeit.timeit(lambda: [size_42(j) for j in data_1000], number=1)
    times.append(time_taken)

plt.figure(figsize=(10, 10))
plt.hist(times, color='blue')
plt.xlabel('Processing Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Processing Times for 1000 Records (1000 repetitions)')

plt.savefig('output.3.3.png')