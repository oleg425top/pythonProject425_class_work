
def push(stack, val):
    stack.append(val)

def pop():
    val = stack.pop()
    return val

stack = []
'''Добавляем элементы в стек'''
push(stack,3)
push(stack,2)
push(stack, 1)
print(stack)
'''Удаляем элементы из стека'''
print(pop())
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)
'''Еще одно удаление вызывает ошибку'''
print(pop())

