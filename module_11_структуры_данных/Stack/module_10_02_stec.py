"""Метод удаления из стека с обработкой пустого стека"""
def push(stack, val):
    stack.append(val)

def pop():
    if stack:
        val = stack.pop()
    else:
        return 'Stack empty'
    return val

stack = []
push(stack,3)
push(stack,2)
push(stack,1)
print(stack)

print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
