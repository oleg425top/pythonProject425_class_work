class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self, top = None):
        self.top = top

    def push(self, data):
        new_node = Node(data)          #назначили узел и он же вершина
        new_node.next_node = self.top  #для первого элемента след узел пока что None, далее следующим узлом становится предыдущий элемент
        self.top = new_node            # говорим новому элементу, что ты теперь стал вершиной

    def pop(self):
        remove_last = self.top           # назначаем вершиной удаляемый элемент
        self.top = self.top.next_node    # следующий узел за удаляемым элементом становится вершиной
        return  remove_last.data         # возвращаем значение удаляемого элемента


# if __name__ == '__main__':

    # node1 = Node('5_rub', None)
    # node2 = Node('7_rub', node1)
    # node3 = Node('10_rub', node2)
    #
    #
    # print(node1.data)
    # print(node2.data)
    # print(node2.next_node.data)
    # print(node2.next_node.next_node.data)

    # my_stack = Stack()
    # my_stack.push('data_3')
    # my_stack.push('data_2')
    # my_stack.push('data_1')
    # print(my_stack.top.data)
    # print(my_stack.top.next_node.data)
    # print(my_stack.top.next_node.next_node.data)
    #
    # stack_len = round(len(my_stack.top.data)/2)
    # print(stack_len)
    #
    # try:
    #     for i in range(stack_len):
    #         print(my_stack.pop())
    # except AttributeError:
    #     print('Sasdasds')
    # finally:
    #     print('Data Extr')


