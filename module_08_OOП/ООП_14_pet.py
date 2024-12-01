class Employer:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'это {self.name} {self.surname} его возраст: {self.age}'
    def print_data(self):
       return f'{self.name} This is Employer class'

    def int(self):
        return f'возраст служащего {self.age}'

class President(Employer):
    def __str__(self):
        president_str = super().__str__()
        return f'{president_str} должность President'
    def print_data(self):
        data = super().print_data()
        return f'{data}\n is President'
    def int(self):
        return super().int()

class Manager(Employer):
    def __str__(self):
        manager_str = super().__str__()
        return f'{manager_str} должность Manager'
    def print_data(self):
        return f'{super().print_data()}\nis Manager'
    def int(self):
        return super().int()
class Worker(Employer):
    def __str__(self):
        worker_str = super().__str__()
        return f'{worker_str} должность President'
    def print_data(self):
        return f'{super().print_data()}\nis Worker'
    def int(self):
        return super().int()
man_1 = Employer('Coll', 'Ferguson', 35)
man_2 = President('Alex', 'Nicolas', 40)
man_3 = Worker('Peter', 'Jacson', 55)
print(man_1.print_data())
print(man_2.print_data())
print(man_3.print_data())
print(man_1)
print(man_2)
print(man_3)
print(man_1.int())
print(man_2.int())
print(man_3.int())