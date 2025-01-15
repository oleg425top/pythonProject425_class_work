class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next.node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def insert_at_position(self, data, node_position):
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_begin(data)

        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def remove_node_index(self, rm_position):
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.net_node
            print(f'Удалили {removed_node.data}\n Теперь начало{self.head.data}')
            return removed_node.data
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is not None or current_node.next_node is None:
            return f'ничего не удалили\nНачало: {self.head.data}'
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f'удалили: {removed_node.data}\nНачало {self.head.data}'

    def removed_node_data(self, rm_data):
        if rm_data == self.head:
            removed_node = self.head
            self.head = self.head.next_node
            return removed_node.data
        current_node = self.head
        while current_node is not None and current_node.next_node is not None:
            if current_node.next_node.data == rm_data:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                return removed_node.data
            current_node = current_node.next_node

        return f'ничего не удалили\nНачало: {self.head.data}'

    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end=' ')
            current_node = current_node.next_node
        return 'Информация выведена'

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

if __name__ == '__main__':

    my_cats_list = LinkedList()

    my_cats_list.insert_at_end('filix1')
    my_cats_list.insert_at_begin('persik')
    my_cats_list.insert_at_begin('barsik3')
    my_cats_list.insert_at_position('vasya', 3)

    print(my_cats_list.head.data)
    print(my_cats_list.head.next_node.data)
    print(my_cats_list.head.next_node.next_node.data)
    # print(my_cats_list.head.next_node.next_node.next_node.data)
    print(my_cats_list.print_ll())
