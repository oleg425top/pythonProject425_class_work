# Создайте класс Human, который будет содержать информацию о человеке. Спомощью механизма наследования,
# реализуйте класс Builder (содержит информацию о строителе), класс Sailor (содержит информацию о моряке),
# класс Pilot (содержит информацию о летчике). Каждый из классов должен содержать необходимые для работы методы.


class Human:
    def __init__(self, name, city):
        self.__name = name
        self.__city = city

    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_data(self):
        return f'{self.get_name()}\n{self.get_city()}'


class Builder(Human):

    def __init__(self, name, city, rang):
        super().__init__(name, city)
        self.__rang = rang

    def get_rang(self):
        return self.__rang


    def get_data(self):
       data =  super().get_data()
       return f'{data}\n{self.get_rang()}'

human = Human('Oleg', 'Ufa')
builder = Builder('Николай', 'Салават', 'Прораб')

print(human.get_data())
print()
print(builder.get_data())

    