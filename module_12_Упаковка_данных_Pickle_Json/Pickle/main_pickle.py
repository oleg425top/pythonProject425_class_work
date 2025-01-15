from module_02_Pickle_DoubleLinked_list import LinkedList
from module_03_Pickler_Unpickler import MyUnPickler, MyPickler

if __name__ == '__main__':
    my_pickler_5 = MyPickler(5)
    my_pickler_4 = MyPickler(4)

    box_list = LinkedList()
    box_list.insert_at_tail('Barsik_4')
    box_list.insert_at_tail('Snow_3')
    box_list.insert_at_tail('Persik_2')

    box_list = my_pickler_5.pickle_data(box_list)
    box_list = MyUnPickler.unpickle_data(box_list)
    print(box_list)

    box_list.print_ll_from_head()
