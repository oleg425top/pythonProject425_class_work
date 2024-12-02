'''Создать базовый класс «Домашнее животное» и производные классы «Собака», «Кошка», «Попугай», «Хомяк». С помощью
конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого из классов методы:
get_sound — издает звук животного (пишем текстом в консоль);
get_name — отображает имя животного;
get_type — отображает название его подвида;
Поля у классов должны быть такие чтобы их можно корректно было передать в методы также поля должны быть
защищены'''


class Pet:
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return f'Это домашнее животное с именем {self.__name}'
    def get_name(self):
        return self.__name

class Dog(Pet):
    def __init__(self, name, sound, type):
        super().__init__(name)
        self.__sound = sound
        self.__type = type
    def get_name(self):
        name = super().get_name()
        return f'{name} это собака'
    def get_sound(self):
        return f'{self.get_name()} издает звук {self.__sound}'
    def get_type(self):
        return f'{self.get_name()} принадлежит подклассу: {self.__type} '

# class Cat(Pet):
#
#
# class Parrot(Pet):
#
#
# class Hamster(Pet):
pet = Pet('Бублик')
print(pet)
dog = Dog('Шарик','лай','волк')
print(dog)
print(dog.get_sound())
print(dog.get_type())
print(dog.get_name())
