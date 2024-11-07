'''глобальные и локальные переменные!!'''


a = 3
print(f' Global a = {a}')


def get_var():
    a = 4
    print(f' Local a = {a}')

get_var()

print(f' Global a = {a}')