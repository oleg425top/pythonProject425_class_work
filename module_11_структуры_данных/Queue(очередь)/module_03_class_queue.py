class Queue:
    def __init__(self, queue = None):
        if queue is None:
            self.__queue = []
        else:
            self.__queue = queue

    def enqueue(self, data):
        if data == 'Очередь пуста':
            return
        self.__queue.append(data)

    def dequeue(self):
        if not self.__queue:
            return 'Очередь пуста'
        return self.__queue.pop(0)

    def peek_first(self):
        if not self.__queue:
            return 'Очередь пуста'
        else:
            return self.__queue[0]

    def peek_last(self):
        if not self.__queue:
            return 'Очередь пуста'
        else:
            return self.__queue[-1]

    def size_queue(self):
        return len(self.__queue)

if __name__ == '__main__':

    my_queue = Queue(['data_0'])
    my_queue.enqueue('data_1')
    my_queue.enqueue('data_2')
    my_queue.enqueue('data_3')
    my_queue.enqueue('data_4')
    my_queue.enqueue('data_5')
    print(my_queue.size_queue())
    print(my_queue.peek_first())
    print(my_queue.peek_last())
    print(my_queue.size_queue())
    print(my_queue.size_queue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())

