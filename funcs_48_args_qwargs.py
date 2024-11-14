data_list = [60,2]
data_tuple = (50,3)
def calculate(v, t):
    way = v*t
    return way

print(f'Распаkовка списка: {calculate(*data_list)}')
print(f'Распаkовка кортежа: {calculate(*data_tuple)}')
