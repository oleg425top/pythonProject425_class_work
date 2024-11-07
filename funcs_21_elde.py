def fis_gen (n):
    p = pp = 1
    for i in range(n):
        if i in [0,1]:
            yield f" {i} -e ч. фибаначи равно: {1} "
        else:
            n = p + pp
            pp, p = p , n
            yield f" {i} -e ч. фибаначи равно: {n} "

fib_list = list(fis_gen(10))
print(fib_list)
