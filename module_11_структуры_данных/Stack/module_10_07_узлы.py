import copy

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self, stack_size = 5, top = Node):  # добавляем максимальный размер стека
        self.top = top
        self.stack_size = stack_size
        self.counter = 0

    def push(self, data):
        if self.counter < self.stack_size:
            new_node = Node(data) #назначаем узел
            new_node.next_node = self.top
            self.top = new_node
            self.counter += 1
        else:
            print('Stack overflow')
            return "Stack overflow"

    def pop(self):
        remove_last = self.top
        self.top = self.top.next_node
        self.counter -= 1
        return  remove_last.data

    @staticmethod
    def counter_int(stack):
        temp_stack = copy.deepcopy(stack)
        counter = 0
        while not temp_stack.is_stack_empty():
            if isinstance(temp_stack.top.data, int):
                counter +=1
            temp_stack.pop()
        return counter

    def is_stack_empty(self):
        if self.top is None:
            return True
        return False
        

# node1 = Node('5_rub', None)
# node2 = Node('7_rub', node1)
# node3 = Node('10_rub', node2)
#
#
# print(node1.data)
# print(node2.data)
# print(node2.next_node.data)
# print(node2.next_node.next_node.data)

my_stack = Stack()
my_stack.push('data_3')
my_stack.push('data_2')
my_stack.push('data_1')
print(my_stack.top.data)
print(my_stack.top.next_node.data)
print(my_stack.top.next_node.next_node.data)

stack_len = round(len(my_stack.top.data)/2)
print(stack_len)

try:
    for i in range(stack_len):
        print(my_stack.pop())
except AttributeError:
    print('Sasdasds')
finally:
    print('Data Extr')


