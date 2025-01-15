class Hero:
    aviable_classes = ['рейнджер', 'воин ', 'маг']
    ranger_skill_list = ['быстрая стрельба', 'скрытность']
    warior_skill_list = ['скорушительный удар', 'вой ']
    mape_skill_list = ['огненый шар','барьер']
    party_list = []

    def __init__(self, name ,hero_class):
        self.name = name
        if hero_class in self.aviable_classes:
            self.hero_class = hero_class
        else:
            self.hero_class = 'воин'
        self.level = 0
        self.exp = 0
        self.skill_list = []
        self.add_aviable_skill_list() = self.mape_skill_list[:]


    def add_aviable_skill_list(self):
        if self.hero_class == 'рейнджер':
            self.skill_list = self.ranger_skill_list.copy()
        elif self.hero_class == 'воин':
            self.skill_list = list(self.warior_skill_list)
        else:
            self.skill_list = self.mape_skill_list[:]
    def add_exp(self, exp):
        self.exp += exp
        if self.exp >= 1000:
            self.level = 3
        elif self.exp >= 500:
            self.level = 2
            self.add_skill()



    def add_skill(self):
        skill = input(f'вы повысили уровень, выберите навык {','.join(self.aviable_skills)}: ')
        while skill not in self.aviable_skills:

    def add_to_party(self):
        self.party_list.append(self)
        return f'{self.name} добавлен в команду'
    def remove_from_party(self):
        self.party_list.remove(self)
        return f' {self.name} исключен из команды'



'''дописать!!!!!!!!!!'''