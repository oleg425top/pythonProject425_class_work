from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius


    def length_of_circle(self):
        length = round(2 * pi * self.radius, 3)
        return f'длина окружности равна: {length} см'

    def square_of_circle(self):
        square_cir = round(pi * self.radius ** 2, 3)
        return f'площадь круга равна: {square_cir} см'

class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        perimeter = round(self.side * 4, 3)
        return f'периметр квадрата равен: {perimeter}'

    def square_of_square(self):
        square_sq = self.side ** 2
        return f'площадь квадрата равна: {square_sq}'



circle = Circle(15)
print(circle.length_of_circle())
print(circle.square_of_circle())
print()
square = Square(10)
print(square.square_of_square())
print(square.perimeter())