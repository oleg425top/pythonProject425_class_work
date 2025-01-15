class Man:
    def __init__(self, name):
        self.name = name

class OtherMan(Man):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __int__(self):
        return self.age

vasya = OtherMan('Vasya', 35)
petya = OtherMan('Petya', 50)

print(int(vasya) + int(petya))
