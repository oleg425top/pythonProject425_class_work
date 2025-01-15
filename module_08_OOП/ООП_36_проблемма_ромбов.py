class A:
    def __init__(self):
        print('class -A')
        super().__init__()
class B(A):
    def __init__(self):
        print('class - B from: ')
        super().__init__()
class C(A):
    def __init__(self):
        print('class - B from: ')
        super().__init__()

class D(C, A):
    def __init__(self):
        print('class -C from: ')
        super().__init__()

d = D()
