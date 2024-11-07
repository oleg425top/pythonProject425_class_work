
'''Генератор степеней числа'''
# from module_04_funcs.funcs_18_elde import value


def degres_of_2(n):
    degree = 1
    for i in range(n):
        yield degree
        degree *= 2
values = [value for value in degres_of_2(5)]
print(values)

values_list = list(degres_of_2(10))
print(values_list)

