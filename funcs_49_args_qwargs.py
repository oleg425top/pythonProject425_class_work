data_dict = {
    'v':60,
    't':3,
}

def calculate(v, t):
    way = v*t
    return way

print(f'Распаkовка словаря: {calculate(**data_dict)}')
print(f'Распаkовка словаря: {calculate(v=60,t=3)}')
