""" Лямбда функции"""
four = lambda: 4
sqr = lambda x: x * x
deg = lambda x , y : x **y

# print(four())
# print(sqr(3))
# print(deg(2,8))

for a in range (-2, 5):
    print(f"Квадрат {a} равен {sqr(a)}")
    print(f"Число {a} в степени {four()} равно {deg(a, four())}")
