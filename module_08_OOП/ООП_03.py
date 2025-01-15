class CakeForm:
    def __init__(self, dough, form, *args):
        self.dough = dough
        self.form = form
        if not args:
            self.ingredients_list = []
        else:
            self.ingredients_list = list(args)


    def __str__(self):
        return f'печем пирог из {self.dough}, {self.form} формы'

    def make_dough(self):
        return f'Замешиваем тесто {self.dough} !'

    def make_form(self):
        return  f'Выкладываем тесто в  форму {self.form}'


    def add_ingredient(self, ingredient):
        self.ingredients_list.append(ingredient)
        return f'добавлен {ingredient}'

    def add_ingredients(self, *args):
        list_ingredient = list(args)
        self.ingredients_list.extend(list_ingredient)
        return f' добавлены {', '.join(list_ingredient)}'


    def cook_cake(self, time = 40):
        if self.ingredients_list:
            if time > 80:
                return f' За {time} минут пирог из теста {self.dough}  c ингредиентами {', '.join(self.ingredients_list)} форма {self.form} сгорит !!!'
            return f'мы выпекаем кекс из теста {self.dough} c ингредиентами {', '.join(self.ingredients_list)} форма {self.form} '
        else:
            if time > 80:
                return f' За {time} минут пирог из теста {self.dough} форма {self.form} сгорит !!!'
            return f'мы выпекаем кекс из теста {self.dough} без ингредиентов , форма {self.form}'

cake_1 = CakeForm('дрожжи', 'круглая', 'рома', 'марципан')
cake_2 = CakeForm('слоеное', 'квадратная')


print(cake_1.make_dough())
print(cake_1.make_form())
print(cake_1.add_ingredients('курага', 'изюм'))
print(cake_1.add_ingredient('оливки'))
print(cake_2.cook_cake())
print(cake_1.cook_cake(100))
#
# print(cake_2.make_dough())
# print(cake_2.make_form())
# print(cake_2.cook_cake(100))