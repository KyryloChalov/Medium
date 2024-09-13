import time

def my_function():
    # # Ваш код тут
    # pass
    for i in range(1000):
        i += i


start_time = time.time()
my_function()
end_time = time.time()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")


import timeit

# def my_function():
#     # Ваш код тут
#     pass

execution_time = timeit.timeit(my_function, number=1000)
print(f"Час виконання: {execution_time} секунд")



from datetime import datetime

# def my_function():
#     # Ваш код тут
#     pass

start_time = datetime.now()
my_function()
end_time = datetime.now()

execution_time = (end_time - start_time).total_seconds()
print(f"Час виконання: {execution_time} секунд")



import cProfile

def my_function():
    # Ваш код тут
    pass

cProfile.run('my_function()')
