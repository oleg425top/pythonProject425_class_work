class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:
    ll_list_data = []

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node
        return f'Теперь голова {self.head.data}'

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f'Теперь в хвосте узел с данными {self.tail}'

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return removed_node

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.prev_node
        self.tail.next_node = None
        return removed_node

    def insert_at_position(self, data, node_position):
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)

        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node.prev_node = current_node
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def remove_node_index(self, index):
        """Удаление элемента, по указанному индексу"""
        if index == 1:
            removed_node = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            self.head.next_node.prev_node = self.head
            return f'{removed_node.data} - удаленный элемент'
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < index - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return f'Ничего не удалили!!!\nВ списке всего {self.len_ll()} элементов\nА вы выбрали {index} элемент'
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        current_node.next_node.prev_node = current_node
        return f'{removed_node.data} - удаленный элемент'

    def removed_node_data(self, rm_data):
        """Удаление элемента по данным узла, если узел с такими данными найден он удаляется;"""
        if rm_data == self.head:
            removed_node = self.head
            self.head = self.head.next_node
            return removed_node.data
        current_node = self.head
        while current_node is not None and current_node.next_node is not None:
            if current_node.next_node.data == rm_data:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                current_node.next_node.prev_node = current_node
                return removed_node.data
            current_node = current_node.next_node

        return f'ничего не удалили\nНачало: {self.head.data}'

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return 'Информация выведена'

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return 'Информация выведена c хвоста'

    def contains(self, data):
        current_node = self.head
        while current_node:
            if data == current_node.data:
                return True
            current_node = current_node.next_node
        return False

    def len_ll(self):
        items_count = 0
        current_node = self.head
        while current_node:
            items_count += 1
            current_node = current_node.next_node
        return items_count

    def get(self, node_position):
        if node_position > self.len_ll():
            return f'В списке нет такого количества элементов, их всего {self.len_ll()}'
        current_node_position = 1
        current_node = self.head
        while current_node_position <= node_position:
            if current_node_position == node_position:
                return current_node.data
            current_node_position += 1
            current_node = current_node.next_node


my_cats_list = LinkedList()

my_cats_list.insert_at_tail('filix1')
my_cats_list.insert_at_head('persik')
my_cats_list.insert_at_head('barsik3')
my_cats_list.insert_at_position('vasya', 2)

# print(my_cats_list.head.data)
# print(my_cats_list.head.next_node.data)
# print(my_cats_list.head.next_node.next_node.data)
# print(my_cats_list.head.next_node.next_node.next_node.data)
my_cats_list.print_ll_from_head()
print()
my_cats_list.print_ll_from_tail()
