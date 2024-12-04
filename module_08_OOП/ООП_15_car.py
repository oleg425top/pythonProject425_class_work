class Wheels:
    def __init__(self, brand_w, diameter):
        self.__brand_w = brand_w
        self.__diameter = diameter

    def diameter(self):
        return self.__diameter

    def set_brand_w(self, new_diameter):
        self.__diameter = new_diameter

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

    def get_count(self):
        return self.__count


