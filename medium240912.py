# 7. Shrink Your Memory Footprint with slots
## Bad 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Better
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y




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

# # 11. Missing Keys ?? defaultdict got you!!
# ## Kinda Bad
# # from collections import defaultdict
# text = "the quick brown fox jumps over the lazy dog"

# word_count = {}
# for word in text.split():
#     if word not in word_count:
#         word_count[word] = 0
#     word_count[word] += 1

# print(f"1.  {word_count = }")


# ## Much Better
# from collections import defaultdict

# # word_count = {}
# word_count = defaultdict(int)
# print(f"1.5 {word_count = }")
# for word in text.split():
#       word_count[word] += 1

# print(f"2.  {word_count = }")


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