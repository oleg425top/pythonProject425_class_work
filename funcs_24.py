"""Генератор списков"""

my_list_comprehension = [1 if num % 2 == 0 else 0 for num in range(10)]
my_generator = (1 if num % 2 == 0 else 0 for num in range(10))
print(my_list_comprehension)
for value in my_generator:
    print(value, end=' ')
