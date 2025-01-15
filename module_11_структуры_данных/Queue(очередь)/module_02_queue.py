"""Реализации очереди через список"""

queue = []


def enqueue(queue, data):
    if data == 'Очередь пуста':
        return
    else:
        queue.append(data)


def dequeue(queue):
    # if len(queue) == 0:
    if not queue:
        return 'Очередь пуста'
    return queue.pop(0)


def peek(queue):
    if not queue:
        return 'Очередь пуста'
    return queue[0]


def peek_last(queue):
    if not queue:
        return 'Очередь пуста'
    return queue[-1]


def size(queue):
    return len(queue)

queue_1 = []
queue_2 = []
enqueue(queue_1, 'data_1')
enqueue(queue_1, 'data_2')
enqueue(queue_1, 'data_3')
enqueue(queue_1, 'data_4')
print(queue_1)
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
print(queue_2)
print(peek(queue_2))
print(peek_last(queue_2))
print(size(queue_2))