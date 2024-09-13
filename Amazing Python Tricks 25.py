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





# 11. Missing Keys ?? defaultdict got you!!
## Kinda Bad
# from collections import defaultdict
text = "the quick brown fox jumps over the lazy dog"

word_count = {}
for word in text.split():
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

print(f"0. {word_count = }")


## Much Better
from collections import defaultdict

# word_count = {}
word_count = defaultdict(int)
print(f"1. {word_count = }")
for word in text.split():
      word_count[word] += 1

print(f"2. {word_count = }")

word_count = dict(word_count)
print(f"3. {word_count = }")



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


