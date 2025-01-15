# Создайте класс очереди для работы со строками значениями. Требуется создать реализации для операций
# над элементами:
# ■ IsEmpty — проверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение.
# ■ Enqueue — добавление элемента в очередь.
# ■ Dequeue — удаление элемента из очереди.
# ■ Show — отображение всех элементов очереди на экран.


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, max_len=6, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.max_len = max_len
        self.counter = 0

    def enqueue(self, data):
        if self.counter < self.max_len:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                self.tail.next_node = new_node
            self.tail = new_node
            self.counter += 1
            return 'ok'
        else:
            return 'queue is overflow'

    def dequeue(self):
        if self.head is None:
            return 'уже и так пусто'
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
            return dequeue_item.data

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def get_queue_len(self):
        items_counter = 0
        if self.head is None:
            return items_counter
        # while self.head:
        #     items_counter += 1
        #     self.head = self.head.next_node
        return self.counter

    def is_full(self):
        if self.max_len == self.get_queue_len():
            return True
        else:
            return False

    def show_queue(self):
        if not self.is_empty():
            temp_head = self.head
            while temp_head:
                print(temp_head.data, end=' ')
                temp_head = temp_head.next_node
            return '  :очередь перед вами'
        return 'пустота.....'

    def peek(self, item_number):
        counter = 1
        if  item_number <= self.get_queue_len():
            temp_head = self.head
            while temp_head:
                if counter == item_number:
                    return  temp_head.data
                temp_head = temp_head.next_node
                counter += 1
        return f'В очереди всего {self.get_queue_len()} элемента/ов'



my_node = Node('item_0')
my_queue = Queue(4, my_node, my_node)
print(my_queue.enqueue('item1'))
print(my_queue.enqueue('item2'))
print(my_queue.enqueue('item3'))
print(my_queue.enqueue('item4'))
print(my_queue.enqueue('item5'))
print(my_queue.enqueue('item6'))
print(my_queue.enqueue('item7'))
print(my_queue.peek(10))
# print(my_queue.is_empty())
# print(my_queue.is_full())
# print(my_queue.get_queue_len())
# print(my_queue.show_queue())
# print()
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.is_empty())
