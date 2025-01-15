"""Реализации очереди через список"""

queue = []


def enqueue(data):
    queue.append(data)


def dequeue():
    # if len(queue) == 0:
    if not queue:
        return 'Очередь пуста'
    return queue.pop(0)


def peek():
    if not queue:
        return 'Очередь пуста'
    return queue[0]


def peek_last():
    if not queue:
        return 'Очередь пуста'
    return queue[-1]


def size():
    return len(queue)


queue.append('data_1')
queue.append('data_2')
queue.append('data_3')
queue.append('data_4')
print(peek())
print(peek_last())
print(size())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
