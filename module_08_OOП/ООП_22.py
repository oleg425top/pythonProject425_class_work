class ExampleClass:
    def __init__(self, value):
        if value  % 2 !=0:
            self.a = 1
        else:
            self.b = 1



example_object = ExampleClass(3)

if hasattr(example_object, 'a'):
    print(example_object.a)
elif hasattr(example_object, 'b'):
    print(example_object.b)
