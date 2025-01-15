
class Classy:
    def __init__(self, name):
        self.name = name

if __name__ =='__main__':
    print(Classy.__module__)
    obj = Classy('Classy_object')
    print(obj.__module__)









print(Classy.__name__)

classy_object = Classy("ClassyObject")
print(type(classy_object))
print(type(classy_object).__name__)
