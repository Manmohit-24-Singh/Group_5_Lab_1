import timeit

# Function to compute the n-th power of 2
def pow2(n):
    return 2 ** n

# Timing the execution of 10000 instances of pow2(10000)
pow2_10000 = timeit.timeit(lambda: pow2(10000), number=10000)
print(f"Time for 10000 instances of pow2(10000): {pow2_10000:.6f} seconds")

def pow2_for():
    result = []
    for n in range(1001):
        result.append(2 ** n)
    return result

def pow2_list():
    return [2 ** n for n in range(1001)]

time_for = timeit.timeit(lambda: pow2_for(), number=1000)
time_list = timeit.timeit(lambda: pow2_list(), number=1000)

print(f"Time for 1000 instances of pow2_for: {time_for:.6f} seconds")
print(f"Time for 1000 instances of pow2_list: {time_list:.6f} seconds")