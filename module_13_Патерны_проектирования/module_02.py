class Sausage:
    def __init__(self):
        self.__energy = 1

    def give_energy(self):
        return self.__energy

class Chicken:
    def __init__(self):
        self.__energy = 2

    def give_energy(self):
        return self.__energy

class Food:
    def __init__(self, food: object):
        self.food = food



class CatSausage:
    def __init__(self, name, energy= 0):
        self.name = name
        self.energy =energy

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            return 'Кот играет'
        else:
            return 'Нужно поесть'

    def eat(self, obj):
        if isinstance(obj, Sausage):
            self.energy += obj.give_energy()
            return f'Кот получил {obj.give_energy()} энергии'
        else:
            return 'кот ест только сардельки'

sausage = Sausage
cat =CatSausage('Tom')
print(cat.play())
print(cat.play())
print(cat.eat(sausage))
print(cat.play())
print(cat.play())
print(cat.play())