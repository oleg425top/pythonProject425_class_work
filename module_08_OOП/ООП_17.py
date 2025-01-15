class ExampleClass:


    def __init__(self, first =1, second = 2):
        self.first = first
        self.second = second
        self.third = 5 '''только для объекта'''

    def set_second(self, second):
        self.second = second

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(3)
example_object_4 = ExampleClass(4)
example_object_5 = ExampleClass(5)

print(example_object_1, __dict__)
