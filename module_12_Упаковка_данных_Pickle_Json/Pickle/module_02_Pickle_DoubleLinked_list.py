import pickle
from pickle import HIGHEST_PROTOCOL


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class LinkedList:

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


if __name__ == '__main__':
    box_list = LinkedList()
    box_list.insert_at_tail('Barsik_4')
    box_list.insert_at_tail('Snow_3')
    box_list.insert_at_tail('Persik_2')
    print(box_list)
    box_list.print_ll_from_head()

    box_list = pickle.dumps(box_list)
    print(box_list)
    box_list = pickle.loads(box_list)
    box_list.print_ll_from_head()
    print()
    box_list.insert_at_tail('Gosha_1')
    box_list.print_ll_from_tail()
    print(box_list.head.data,'////')
    print(box_list.head.next_node.data,'////')
    print(box_list.tail.data)
    print(box_list.tail.prev_node.data)
    print()
    with open('cats.cats', 'wb') as fp:
        pickle.dump(box_list, fp, protocol=HIGHEST_PROTOCOL)
    try:
        with open('cats.cats', 'rb') as fp:
            my_cats = pickle.load(fp)
    except FileNotFoundError:
        print('File not Found!!')
    finally:
        print('GoodBye!!')

    print(my_cats.print_ll_from_head())
    my_cats.insert_at_tail('oleg')
    print(my_cats.print_ll_from_head())


