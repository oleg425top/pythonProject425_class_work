class Car:
    def __init__(self, country, year, model ):
        self.country = country
        self.year = year
        self.model = model
    def __str__(self):
        return f'машина {self.model} год выпуска {self.year} из {self.country}'

# class Gasoline(Car):
#     def __init__(self, ):

BMW = Car('USA', 2000, 'X5')
print(BMW)