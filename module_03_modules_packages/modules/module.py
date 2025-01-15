#!/usr/bin/env python3
'''файл модуль для того чтобы показать работу функционала if __name__ == "__main__"'''

__counter = 0
def sum_list(nums_list: list):
    '''функция для суммирования элементов списка'''
    global __counter
    __counter += 1
    new_sum = 0
    for num in nums_list:
        new_sum += num
    return new_sum

def product_list (nums_list:list):
    '''функция для произведения элементов списка'''
    global __counter
    __counter += 1
    product = 1
    for num in nums_list:
        product *= num
    return product
print(__name__)

if __name__ == '__main__':
    print("я предпочел бы быть модулем, но я могу  провести тесты")
    my_nums_list = [i for i in range(1,6)]
    print(sum_list((my_nums_list)))
    print(product_list(my_nums_list))
else:
    print("я модуль и мне это нравится")



