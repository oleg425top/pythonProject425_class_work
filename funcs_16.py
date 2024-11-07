'''Фибаначи через переопределение класса'''

class Fib:
    def __init__(self, number: 10):
        print("__init__")
        self.__nn = number
        self.__i = 0
        self.__p1 = self.__p2 =1
    def __next__(self):
        print('__next__')
        self.__i += 1
        if self.__i > self.__nn:
            raise StopIteration
        if self.__i in [1,2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n ):
        self.__iter = Fib(n)

    def __iter__(self):
        print('Class iter')
        return self.__iter

my_fib_class = Class(10)

for i in my_fib_class:
    print(i)

