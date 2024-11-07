def func(n):
    for i in range(n):
        return i

print(func(10))

def func_1(n):
    for i in range(n):
        yield i
        # print(i)
print(func_1(10))
list_1 = []
for value in func_1(10):
    print(value)
    list_1.append(value)

# [list_1.append(value) for value in func_1(5)]
print(list_1)

def degres_of_2(n):
    degree = 1
    for i in range(n):
        yield degree
        degree *= 2
[print(value) for value in degres_of_2(5)]