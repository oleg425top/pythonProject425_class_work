"""Метод удаления из стека с обработкой пустого стека, через Raise"""
def push(stack, val):
    stack.append(val)

def pop():
    try:
        val = stack.pop()
    except IndexError as SISE:
        return f'{SISE}:Stack is empty'
    return val

stack = []
push(stack,3)
push(stack,2)
push(stack,1)

print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
