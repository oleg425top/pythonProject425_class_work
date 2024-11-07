""""Списковые выражения"""
"""Стандартная запись"""
# my_list = []
# for num in range(10):
#     my_list.append(1 if num % 2 == 0 else 0)
# print(my_list)
""" 1 вариант спискового выражения"""
# [my_list.append(1) for num in range(10) if num % 2 == 0 or my_list.append(3)]
# print(my_list)
""" 2 вариант спискового выражения"""
my_list_comprehension = [1 if num % 2 == 0 else 0 for num in range(10)]
print(my_list_comprehension)