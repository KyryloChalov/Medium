def my_function():
    for i in range(1000000):
        i += i


# 1 =======================================

import time

start_time = time.time()
my_function()
end_time = time.time()

execution_time = end_time - start_time
print(f"1. time.time()    - час виконання: {execution_time:.10f} секунд")


# 2 =======================================

import timeit

execution_time = timeit.timeit(my_function, number=1)
print(f"2. timeit.timeit  - час виконання: {execution_time:.10f} секунд")


# 3 =======================================

from datetime import datetime

start_time_ = datetime.now()
my_function()
end_time_ = datetime.now()

execution_time = (end_time_ - start_time_).total_seconds()
print(f"3. datetime.now() - час виконання: {execution_time:.10f} секунд")


# 4 =======================================

import cProfile

print("4. cProfile")
cProfile.run("my_function()")
