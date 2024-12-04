class Wheels:
    def __init__(self, brand_w, diameter):
        self.__brand_w = brand_w
        self.__diameter = diameter

    def get_brand_w(self):
        return self.__brand_w

    def diameter(self):
        return self.__diameter


class Engine:
    def __init__(self, brand_e, capacity):
        self.__brand_e = brand_e
        self.__capacity = capacity

    def get_brand_e(self):
        return self.__brand_e

    def get_capacity(self):
        return self.__capacity


class Doors:
    def __init__(self, count: int, door_trim):
        self.__count = count
        self.__door_trim = door_trim

    def get_count(self):
        return self.__count

    def get_door_trim(self):
        return self.__door_trim
