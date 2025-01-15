class CakeForm:
    def __init__(self, dough, form):
        self.dough = dough
        self.form = form
        print(f'печем пирог {self.form} формы из "{self.dough}" теста ')

    def __str__(self):
        return f'печем пирог из {self.dough}, {self.form} формы'

    def make_dough(self):
        return f'Замешиваем тесто'

    def make_form(self):
        return  f'Выкладываем тесто в  форму'

    def cook_cake(self, time = 40):
        if time > 80:
            return f' За {time} минут пирог сгорит'
        return f'мы выпекаем кекс'

cake_1 = CakeForm('дрожжи', 'круглая')
cake_2 = CakeForm('слоеное', 'квадратная')
print(cake_1)
print(cake_2)

# print(cake_1.make_dough())
# print(cake_1.make_form())
# print(cake_1.cook_cake())
#
# print(cake_2.make_dough())
# print(cake_2.make_form())
# print(cake_2.cook_cake(100))