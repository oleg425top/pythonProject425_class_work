import json


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    @staticmethod
    def to_dict(obj):
        return obj.__dict__


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

class MyLLDataEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            'head': o.head.data,
            'tail': o.tail.data,
            'class_name': o.__class__.__name__
        }

cats_list = LinkedList()
cats_list.insert_at_head('Vasika_1')
cats_list.insert_at_head('Snezhok_0')
cats_list.insert_at_tail('Tom_2')

json_cats_list = json.dumps(cats_list, cls=MyLLDataEncoder, ensure_ascii=False, indent=3)
print(json_cats_list)
python_cats_data = json.loads(json_cats_list)
print(python_cats_data)

with open(r'my_cats_ll.json', 'w', encoding='utf-8') as fh:
    json.dump(cats_list, fh, cls=MyLLDataEncoder, ensure_ascii=False, indent=3)

with open(r'my_cats_ll.json', 'r', encoding='utf-8') as fh:
    python_cats_from_file = json.load(fh)
