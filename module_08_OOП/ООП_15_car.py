class Wheels:
    def __init__(self, brand_w , diameter):
        self.__brand_w = brand_w
        self.__diameter = diameter

class Engine:
    def __init__(self, brand_e , capacity):
        self.__brand_e = brand_e
        self.__capacity = capacity

class Doors:
    def __init__(self, count:int , door_trim ):
        self.__count = count
        self.__door_trim = door_trim