# Создайте класс «Самолет». Наполните его необходимыми характеристиками и методами.
# Реализуйте упаковку и
# распаковку объектов класса «Самолет» с использованием
# модуля pickle

class Plane:

    def __init__(self, model, max_speed, capacity):
        self.model = model
        self.max_speed = max_speed
        self.capacity = capacity
        self.fly = False


    def fly(self):
        if self.fly:
            print('Самолет летит')
        else:
            print('самолет на посадке')

    def land(self):
        if self.fly:
            self.fly = False
            print(f"The {self.model} самолет посажен.")
        else:
            print("самолет уже на земле")




airplane = Plane(model="Boeing 747", max_speed=900, capacity=524)


