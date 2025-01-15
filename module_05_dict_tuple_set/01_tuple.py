mytable_tuple = ([1, 2, 3],[4, 5, 6])
print(f'исходный кортеж{mytable_tuple}')

mytable_tuple[0][1] = 10
mytable_tuple[1].append(7)

print(f'измененный кортеж {mytable_tuple}')

my_list = [10, 20, 30, 50, 60]
my_tuple = (10, 20, 30, 50, 60)

print(my_tuple.__sizeof__())
print(my_list.__sizeof__())

my_dict = {
    ('a',1): 'value_1',
    ('b',2): 'value_2',
}
print(my_dict[('a',1)])
print(my_dict[('b',2)])

