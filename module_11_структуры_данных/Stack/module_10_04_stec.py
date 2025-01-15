class Stack:
    all_stacks_list = []

    def __init__(self):
        self.__stack_list = []
        Stack.all_stacks_list.append(self)

    def __str__(self):
        return f'{self.__stack_list}'

    def push(self, value):
        if value == 'Stack IS empty':
            return
        self.__stack_list.append(value)

    def pop(self):
        try:
            val = self.__stack_list.pop()
        except IndexError:
            return 'Stack IS empty'
        return val

    # def get_stack(self):
    #     return self.__stack_list


if __name__ == '__main__':

    stack_obj_1 = Stack()
    stack_obj_2 = Stack()
    stack_obj_1.push(3)
    stack_obj_1.push(2)
    stack_obj_1.push(1)
    print(stack_obj_1)
    stack_obj_2.push(stack_obj_1.pop())
    stack_obj_2.push(stack_obj_1.pop())
    stack_obj_2.push(stack_obj_1.pop())
    stack_obj_2.push(stack_obj_1.pop())
    print(stack_obj_2)
    print(Stack.all_stacks_list)
    print(stack_obj_2.pop())
    print(stack_obj_2.pop())
    print(stack_obj_2.pop())
    print(stack_obj_2.pop())
    print(stack_obj_2.pop())
    print(stack_obj_2.pop())
