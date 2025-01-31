import json
import matplotlib.pyplot as plt
import numpy as np
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

records = [1000, 2000, 5000, 10000]
avrg_times = []

for count in records:
    subset = data[:count]
    time_taken = timeit.timeit(lambda: [size_42(i) for i in subset], number=100)
    average_time = time_taken / 100
    avrg_times.append(average_time)
    print(f"Average time for {count} records: {average_time:.6f} seconds")

slope, intercept = np.polyfit(records, avrg_times, 1)

plt.figure(figsize=(10, 10))
plt.scatter(records, avrg_times, color='blue', label='Average Processing Time')

linevalues = [slope * x + intercept for x in records]
plt.plot(records, linevalues, 'red', label=f'Regression Line')

plt.xlabel('Number of Records')
plt.ylabel('Average Processing Time')
plt.title('Linear Regression: Number of Records vs Processing Time')
plt.legend()

plt.savefig('output.3.2.png')