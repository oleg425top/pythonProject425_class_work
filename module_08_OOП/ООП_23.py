

#
# class ExampleClass:
#     atr = 1
#
# print(hasattr(ExampleClass, 'atr'))
# print(hasattr(ExampleClass,  'ewew'))


class ExampleClass:
    a = 1

    def __init__(self):
        self.b = 2

example_object = ExampleClass()

print(hasattr(example_object, 'a'))
print(hasattr(example_object, 'b'))
print(hasattr(ExampleClass, 'a'))
print(hasattr(ExampleClass, 'a'))
