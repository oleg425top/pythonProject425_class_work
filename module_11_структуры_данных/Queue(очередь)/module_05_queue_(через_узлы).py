class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail


    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:                # 1 если очередь пуста и у нее нет головы
            self.head = new_node             # 2 то помещаемый элемент становится и головой ......
        else:                                # 4 если очередь не пуста,
            self.tail.next_node = new_node   # 5 то узел который следует за хвостом, будет нашим новый узлом
        self.tail = new_node                 # 3 ....... и хвостом (добавленный элемент теперь хвост)

    def dequeue(self):
        if self.head is None:
            return
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
            return dequeue_item.data


node_1 = Node('jlkjk')
node_2 = Node('ghjgjhjhkj', node_1)
my_queue = Queue(node_2, node_1)
# my_queue = Queue()
my_queue.enqueue('item1')
my_queue.enqueue('item2')
my_queue.enqueue('item3')
my_queue.enqueue('item4')

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

