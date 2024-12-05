class Wheels:
    def __init__(self, brand_w, diameter):
        self.__brand_w = brand_w
        self.__diameter = diameter

    def get_diameter(self):
        return self.__diameter

    def set_diameter(self, new_diameter):
        self.__diameter = new_diameter
        return f'вы поставили колеса другого диаметра {self.__diameter}'

    def get_brand_w(self):
        return self.__brand_w


class Engine:
    def __init__(self, brand_e, capacity):
        self.__brand_e = brand_e
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, new_capacity):
        self.__capacity = new_capacity
        return f'(вы заменили двигатель на двигатель объемом: {self.__capacity} литра) '

    def get_brand_e(self):
        return self.__brand_e


class Doors:
    def __init__(self, count: int, door_trim):
        self.__count = count
        self.__door_trim = door_trim

    def get_door_trim(self):
        return self.__door_trim

    def set_door_trim(self, new_door_trim):
        self.__door_trim = new_door_trim
        return f'вы заменили обивку дверей на: {self.__door_trim}'

    def get_count(self):
        return self.__count


class Car(Wheels, Engine, Doors):
    def __init__(self, brand_w, diameter, brand_e, capacity: int, count: int, door_trim, brand_car):
        super().__init__(brand_w, diameter)
        Engine.__init__(self, brand_e, capacity)
        Doors.__init__(self, count, door_trim)
        self.__brand_car = brand_car

    def get_brand_car(self):
        return self.__brand_car

    def __str__(self):
        return (f'это машина марки: {self.get_brand_car()}, c диаметром колес: {self.get_diameter()}'
                f', марка колес: {self.get_brand_w()}\nc двигателем марки: {self.get_brand_e()}\n'
                f'объемом: {self.get_capacity()} литра, c {self.get_count()} дверьми\n'
                f'материал обивки дверей: {self.get_door_trim()}')


car = Car('Yokohama', '17 дюймов', 'Toyota', 3, 4, 'кожа', "Nissan-GTR")
print(car)
print()
print(car.set_capacity(4))
print()
print(car)
print()
print(car.set_diameter(19))
print()
print(car)
print()
print(car.set_door_trim('эко кожа'))
print()
print(car)
