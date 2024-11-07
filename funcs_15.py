'''Фибаначи через 1 класс'''
class Fib:
    def __init__(self, number: 10):
        print("__init__")
        self.__nn = number
        self.__i = 0
        self.__p1 = self.__p2 =1
    def __iter__(self):
        print('__iter__')
        return self
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
    def __str__(self):
        return f"{self.__i} число фибаначи равно "

my_fib = Fib(10)
for i in my_fib:
    print(f"{my_fib}:  {i}")
