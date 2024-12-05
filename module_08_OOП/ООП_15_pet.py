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
    def __init__(self, name, sound, type_dog):
        super().__init__(name)
        self.__sound = sound
        self.__type = type_dog

    def get_name(self):
        name = super().get_name()
        return f'Собака {name}'

    def get_sound(self):
        return f'{self.get_name()} издает звук {self.__sound}'

    def get_type(self):
        return f'{self.get_name()} принадлежит подклассу: {self.__type} '


class Cat(Pet):
    def __init__(self, name, sound, type_cat):
        super().__init__(name)
        self.__sound = sound
        self.__type = type_cat

    def get_name(self):
        name = super().get_name()
        return f'Кошка {name}'

    def get_sound(self):
        return f'{self.get_name()} издает звук {self.__sound}'

    def get_type(self):
        return f'{self.get_name()} принадлежит подклассу: {self.__type} '


class Parrot(Pet):
    def __init__(self, name, sound, type_parrot):
        super().__init__(name)
        self.__sound = sound
        self.__type = type_parrot

    def get_name(self):
        name = super().get_name()
        return f'Попугай {name}'

    def get_sound(self):
        return f'{self.get_name()} издает звук {self.__sound}'

    def get_type(self):
        return f'{self.get_name()} принадлежит подклассу: {self.__type} '


class Hamster(Pet):
    def __init__(self, name, sound, type_hamster):
        super().__init__(name)
        self.__sound = sound
        self.__type = type_hamster

    def get_name(self):
        name = super().get_name()
        return f'Хомяк {name}'

    def get_sound(self):
        return f'{self.get_name()} он с*** {self.__sound} и воняет!'

    def get_type(self):
        return f'{self.get_name()} принадлежит подклассу: {self.__type} '


pet = Pet('Бублик')
print(pet)
print()

dog = Dog('Шарик', 'лай', 'волк')
print(dog)
print(dog.get_name())
print(dog.get_sound())
print(dog.get_type())
print()

cat = Cat('Васька', 'мурр', 'дикая кошка')
print(cat)
print(cat.get_name())
print(cat.get_sound())
print(cat.get_type())
print()

parrot = Parrot('Яша', 'Разговаривает на Русском', 'дикие попугаи', )
print(parrot)
print(parrot.get_name())
print(parrot.get_sound())
print(parrot.get_type())
print()

hamster = Hamster('Жирный', 'Пищит', 'грызун', )
print(hamster)
print(hamster.get_name())
print(hamster.get_sound())
print(hamster.get_type())
print()
