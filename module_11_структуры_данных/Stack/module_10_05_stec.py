from module_10_04_stec import Stack


class AddingStack(Stack):
    """Способ без super"""

    # def __init__(self):
    #     Stack.__init__(self)
    #     self.__sum = 0
    #
    # def get_sum(self):
    #     return self.__sum
    #
    # def push(self, value):
    #     self.__sum += value
    #     Stack.push(self,value)
    #
    # def pop(self):
    #     value = Stack.pop(self)
    #     self.__sum -= value
    #     return value

    """способ через super()"""

    def __init__(self):
        super().__init__()
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, value):
        super().push(value)
        self.__sum += value
        if self.__sum >= 10:
            print('Stack overflow')
            return

    def pop(self):
        value = super().pop()
        self.__sum -= value
        return value


if __name__ == '__main__':
    stack_object = AddingStack()
    for i in range(5):
        stack_object.push(i)
        print(stack_object)
    print(stack_object.get_sum())
    for i in range(5):
        print(f'значение {stack_object.pop()}. Сумма внутри сетка {stack_object.get_sum()}')
        # print(stack_object.get_sum())
