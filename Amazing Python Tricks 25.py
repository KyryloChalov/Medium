# 25 Amazing Python Tricks That Will Instantly Improve Your Code


# # 1. Stop Wasting Time with x.append—x.extend provides a much faster and cleaner way of extending lists
# # When adding several items to a list, opt for the extend() method to efficiently append the entire iterable at once, instead of using append() repeatedly for each element.

# ## Bad 
# data = [1,2,3]
# data.append(4)
# data.append(5)
# data.append(6)

# print(f'1. {data = }')

# ## Good
# data = [1,2,3]
# data.extend((4,5,6))
# print(f'2. {data = }')



# # 2. Simplify Error Handling with suppress() Instead of depending on try/except for your whole life
# # Often you want to handle an exception and ignore it. You can do this with a try/exceptblock, using a single pass in the exceptblock, but there is a simpler and more concise way of using the suppress()method from contextlib .

# from contextlib import suppress
# def f():
#     ...
#     return

# ## Bad
# try: 
#     f() 
# except FileNotFoundError: 
#     pass

# ## Good
# with suppress(FileNotFoundError): 
#     f()



# # 3. Why Type More? Simplify Your Prints with Just print()
# ## Bad
# print("")

# ## Good

# print()




# # 4. Boost File Writing Efficiency: Use .writelines() Instead of Multiple .write() Calls
# ## Bad
# lines = ["line 1", "line 2", "line 3"] 
# with open("file", "w") as f: 
#     for line in lines: 
#         f.write(line + "\n")

# ## Good 
# lines = ["line ", "line 2", "line 3"]
# with open("file") as f: 
#  f.writelines(lines)



# # 5. When comparing a value to multiple options, use `in` instead of numerous `or` checks

# x = ''
# input(x)

# ## Bad
# if x == "abc" or x == "mno" or x == "xyz": 
#  pass

# ## Good
# if x in ("abc", "mno", "xyz"): 
#  pass


# # 6. When One-Liners Go Too Far
# # One-liners are good and showcase lots of logical skills. However, an overdose of one-liners in source code creates confusion and reduces readability.

# ## Bad
# names = sorted([emp['name'] for emp in employees if emp['salary'] > 50000], \
#                    key=lambda name: next(emp['salary'] \
#                    for emp in employees if emp['name'] == name
#                   ))

# ## Good
# # Step 1: Filter employees with salary > 50,000
# filtered_employees = [emp for emp in employees if emp['salary'] > 50000]

# # Step 2: Sort the filtered employees by salary
# sorted_employees = sorted(filtered_employees, key=lambda emp: emp['salary'])

# # Step 3: Extract the names of the sorted employees
# names = [emp['name'] for emp in sorted_employees]


# # 7. Shrink Your Memory Footprint with slots
# # Специальный атрибут __slots__ позволяет вам явно указать, какие атрибуты экземпляра вы ожидаете от экземпляров вашего объекта, с ожидаемыми результатами:
# # https://ru.stackoverflow.com/questions/1206730/%D0%9A%D0%B0%D0%BA%D0%BE%D0%B2%D0%B0-%D1%86%D0%B5%D0%BB%D1%8C-slots-%D0%B2-python
# ## Bad 
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# # Better
# class Point:
#     __slots__ = ['x', 'y']
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y




# #  8. Simplify Directory Traversal with os.walk

# # Let’s take the above example and try to access Duck1.png using os.walk

# ## Nahhh
# from datetime import datetime
# import os
# root_dir = 'c:\\'
# filename = 'm0nkrus.nfo'
# start_time = datetime.now()

# ## Yup!!!!!!!!
# for dirpath, _, filenames in os.walk(root_dir):
#     # print(f'{dirpath = }')
#     if filename in filenames:
#         file_path = os.path.join(dirpath, filename)
#         print("Using os.walk:", file_path)
#         break

# end_time = datetime.now()
# print(f"Час виконання: {end_time - start_time}")


# # 9.Manage Multiple Contexts Seamlessly with ExitStack
# # Rather than using nested with statements, creating a "pyramid of doom" that becomes hard to read and maintain, you should try using Contextlib.ExitStack() for dynamic management of context managers.

# ## Bad
# def process_files(file1, file2, file3):
#     with open(file1, 'r') as f1:
#         with open(file2, 'r') as f2:
#             with open(file3, 'r') as f3:
#                 # Process files
#                 pass

# ## Much Better
# from contextlib import ExitStack

# def process_files(file1, file2, file3):
#     with ExitStack() as stack:
#         f1 = stack.enter_context(open(file1, 'r'))
#         f2 = stack.enter_context(open(file2, 'r'))
#         f3 = stack.enter_context(open(file3, 'r'))
#         # Process files





# # 11. Missing Keys ?? defaultdict got you!!
# ## Kinda Bad
# # from collections import defaultdict
# text = "the quick brown fox jumps over the lazy dog"

# word_count = {}
# for word in text.split():
#     if word not in word_count:
#         word_count[word] = 0
#     word_count[word] += 1

# print(f"0. {word_count = }")


# ## Much Better
# from collections import defaultdict

# # word_count = {}
# word_count = defaultdict(int)
# print(f"1. {word_count = }")
# for word in text.split():
#       word_count[word] += 1

# print(f"2. {word_count = }")

# word_count = dict(word_count)
# print(f"3. {word_count = }")



# # 13. Ditch String Manipulation. Use .with_suffix() for Changing File Extensions
# from pathlib import Path

# filename = 'file.txt'
# new_ext = '.md'

# print(f"0. {filename = }")
# print(f"0. {Path(filename) = }")
# print(f"0. {str(Path(filename)) = }")
# print(f"0. {str(Path(filename))[:4] = }")

# ## Bad
# new_filepath = str(Path(filename))[:4] + new_ext
# print(f"1. {new_filepath = }")

# ## Good
# new_filepath = Path(filename).with_suffix(new_ext)
# print(f"2. {new_filepath = }")


# # 14. You can use Boolean Checks to determine if a container is empty or not
# ## Bad 
# items = []
# if len(items) == 0:
#     print("No items in the list")

# ## Good
# items = []
# if not items:
#     print("No items in the list")


# # 15. Simplify Inline if Statements with a Single or Expression
# x = 0
# y = 12

# # Bad
# z = x if x else y

# print(f"1. {z = }")

# ## Good
# z = x or y

# print(f"2. {z = }")



# # 16. Quick and Easy Key Checking in Dictionaries
# # If you only want to check if a key exists in a dictionary, you don’t need to call .keys()first, just use inon the dictionary itself.

# ## Bad
# d = {"key": "value"} if "key" in d.keys():

# ## Good
# d = {"key": "value"} if "key" in d:



# # 17. Avoiding the Pitfall of Useless Return Values
# # Not using meaningful return values from functions can hinder code understandability. It is important to design functions with return values that provide useful information and can be leveraged in other parts of the code when called.

# ## kinda Bad
# def calculate_sum_of_n_numbers(numbers):
#     total = sum(numbers)
#     print("Sum:", total)

# numbers_list = [11, 45, 32, 49, 56]
# calculate_sum_of_n_numbers(numbers_list)
# # In the above example, calculate_sum_of_n_numbers() the function computes the sum of a list but only prints the data without returning it. Instead of using print, it's better to return the value for a better code flow.

# ## Good
# def calculate_sum_of_n_numbers(numbers):
#     total = sum(numbers)
#     return total

# numbers_list = [1, 2, 3, 4, 5]
# result = calculate_sum_of_n_numbers(numbers_list)
# print("Sum:", result)



# # 18. Streamline Equality Checks with a Comparison Chain
# # When checking that multiple objects are equal to each other, don’t use an and expression. Use a comparison chain instead, for example.

# ## Bad
# if x == y and x == z: 
#  pass


# ## A Good one
# if x == y == z: 
#  pass



# # 19. A Code optimization Tip: Make use operator Instead of Lambdas
# # Don’t write lambdas/functions to wrap builtin operators, use the operatormodule instead.

# from functools import reduce 
# nums = [1, 2, 3, 4, 5, 44, 66] 

# ## Bad Example
# print(reduce(lambda x, y: x + y, nums)) # 6

# ## A Better One
# from operator import add 
# print(reduce(add, nums)) # 6


# # 20. A better way to manipulate tabs in strings
# # Instead of using replace("\\t", " " * 8), you can use the expandtabs() method. It is more succinct and descriptive. It also allows for an optional parameter to specify the tab width.

# ## Bad
# spaces_8 = "hello\\tworld".replace("\\t", " " * 8) 
# spaces_4 = "hello\\tworld".replace("\\t", " ")


# ## Good
# spaces_8 = "hello\\tworld".expandtabs() 
# spaces_4 = "hello\\tworld".expandtabs(4)



# # 22. You Don’t Always Need open to Write to Files
# # When you simply need to save some content to a file, using a with block might be more than necessary. Instead, you can streamline your code by using pathlib's write_text() function.

# ## Bad
# content = "Hello, world!"
# with open("example.txt", "w") as file:
#     file.write(content)

# ## Good
# from pathlib import Path
# # content = "Hello, world!"
# Path("example_.txt").write_text(content)


# # 23. Never leave your except block empty
# ## Bad
# try:
#     file = open("data.txt", "r")
#     # Perform some operations with the file
# except:
#     # Error handling
#     pass


# ## Good
# try:
#     file = open("data.txt", "r")
#     # Perform some operations with the file
#     # ...
#     file.close()
# except FileNotFoundError:
#     print("File not found!")
# except IOError as e:
#     print("Error occurred while handling the file:", str(e))



# # 24. A Better Way to Access Dictionary Values: Try get()
# # When accessing values in a dictionary, using the get() method can be safer and more concise than using standard indexing. The get() method allows you to provide a default value if the key is not found, avoiding potential KeyError exceptions.

# ## Not so Good
# data = {"name": "Alice", "age": 30}

# # Standard indexing, may raise KeyError if the key doesn't exist
# name = data["name"]  
# city = data["city"] if "city" in data else "Unknown"



# ## Good
# data = {"name": "Alice", "age": 30}

# # Using get() method to safely access dictionary values with a default
# name = data.get("name", "Unknown")
# city = data.get("city", "Unknown")


# # 25. Make use of Match and Case for better conditional statements
# ## Bad
# def describe_type(obj):
#     if isinstance(obj, str):
#         return "It's a string"
#     elif isinstance(obj, int):
#         return "It's an integer"
#     elif isinstance(obj, list):
#         return "It's a list"
#     else:
#         return "It's something else"


# ## A Kinda Good Way 
# def describe_type(obj):
#     match obj:
#         case str():
#             return "It's a string"
#         case int():
#             return "It's an integer"
#         case list():
#             return "It's a list"
#         case _:
#             return "It's something else"