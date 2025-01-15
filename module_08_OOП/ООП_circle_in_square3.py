from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius


    def length_of_circle(self):
        length = int(2 * pi * self.radius)
        return f'длина окружности равна: {length} см'

    def square_of_circle(self):
        square_cir = int(pi * self.radius ** 2)
        return square_cir

class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        perimeter = int(self.side * 4)
        return f'периметр квадрата равен: {perimeter}'

    def square_of_square(self):
        square_sq = self.side ** 2
        return square_sq

class CircleInSquare(Circle, Square):
    def __init__(self, square_of_circle, square_of_square):
        super().__init__()
        Square.__init__(self, square_of_square)


    def checked(self):
        if self.radius / self.side() == 4 / pi:
            return f' окружность можно считать вписанной в квадрат'
        else:
            return f'окружность не вписана в квадрат'



circle = Circle(10)
print(circle.length_of_circle())
print(circle.square_of_circle())
print()
square = Square(20)
print(square.square_of_square())
print(square.perimeter())

check_1 = CircleInSquare(circle.square_of_circle(), square.square_of_square())
print(check_1.checked())