# get the nth fibonacci
# 0: 0
# 1: 1
# 2: 0+1=1
# 3: 1+1=2
# 4: 1+2=3
# 5: 2+3=5

fibonacci_hash = {}
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibonacci_hash:
        return fibonacci_hash[n]
    else:
        fib_n_2 = fibonacci_hash[n-2] if n-2 in fibonacci_hash else fibonacci(n-2)
        fib_n_1 = fibonacci_hash[n-1] if n-1 in fibonacci_hash else fibonacci(n-1)
        fib_n = fib_n_1 + fib_n_2
        fibonacci_hash[n] = fib_n
        return fib_n

def fibonacci_iterative(n):
    if n < 0: return -1
    if n == 0: return 0
    if n == 1: return 1
    previous_2_values = []
    previous_2_values.append(0)
    previous_2_values.append(1)
    for i in range(2,n+1):
        current_fib = previous_2_values[0] + previous_2_values[1]
        # previous_2_values.pop(0)
        # previous_2_values.append(current_fib)

        previous_2_values[0] = previous_2_values[1]
        previous_2_values[1] = current_fib
    return previous_2_values[1]

import time

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(5) == 5
assert fibonacci(10) == 55

assert fibonacci_iterative(0) == 0
assert fibonacci_iterative(1) == 1
assert fibonacci_iterative(2) == 1
assert fibonacci_iterative(5) == 5
assert fibonacci_iterative(10) == 55

import time
# start_time = time.time()
# #fibonacci(10000)
# print(time.time() - start_time)

start_time = time.time()
fibonacci_iterative(900000)
print(time.time() - start_time)