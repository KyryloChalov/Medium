def my_function():
    for i in range(1000):
        i += i

# 1 =======================================

import time

start_time = time.time()
my_function()
end_time = time.time()

execution_time = end_time - start_time
print(f"1. time.time()    - час виконання: {execution_time} секунд")


# 2 =======================================

import timeit

execution_time = timeit.timeit(my_function, number=1000)
print(f"2. timeit.timeit  - час виконання: {execution_time} секунд")


# 3 =======================================

from datetime import datetime

start_time = datetime.now()
my_function()
end_time = datetime.now()

execution_time = (end_time - start_time).total_seconds()
print(f"3. datetime.now() - час виконання: {execution_time} секунд")


# 4 =======================================

import cProfile

print("4. cProfile")
cProfile.run('my_function()')
