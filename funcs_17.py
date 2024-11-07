'''Фибаначи через наследование классов'''


class Fib:
    def __init__(self, nn: 10):
        print("__init__")
        self.__nn = nn
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

class Class(Fib):
    def __init__(self, nn ):
        super().__init__(nn)

    def __iter__(self):
        print('Class iter')
        return self

my_fib_class = Class(10)
my_fib_class2 = Fib(10)

for i in my_fib_class:
    print(i)
for i in my_fib_class2:
    print(i)
