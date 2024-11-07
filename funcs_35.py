'''Регулярные выражения!!!'''

import re

my_string = input('Введите ваш маил')
if re.search(r'.*@mail\.ru$', my_string):
    print('correct')
else:
    print('try again')


# my_patern = re.compile(r'.*@mail\.ru$')

# print(my_patern.search(my_string))