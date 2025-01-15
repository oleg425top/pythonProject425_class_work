class City:
    city_objects_list = []

    def __init__(self, name, region, country, population, post_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.post_code = post_code
        self.phone_code = phone_code
        self.city_objects_list.append(self)


    @staticmethod
    def get_count_of_cities():
        return len(City.city_objects_list)


    def __str__(self):
        return f'название города {self.name} регион: {self.region} население {self.population} код телефона {self.phone_code} почтовый код {self.post_code} '

    def set_population(self, new_population):
        self.population = new_population

    def set_phone_code(self, new_phone_code):
        self.phone_code = new_phone_code

    def set_post_code(self, new_post_code):
        self.post_code = new_post_code


Sterlitamak = City("Стерлитамак", 'Башкортостан', 'Россия', 250000, '453120', '83473')
Sterlitamak_1 =  City("Стерлитамак", 'Башкортостан', 'Россия', 250000, '453120', '83473')
Sterlitamak_2 =  City("Стерлитамак", 'Башкортостан', 'Россия', 250000, '453120', '83473')
print(City.get_count_of_cities())


# print(Sterlitamak)
# Sterlitamak.set_population(400000)
# Sterlitamak.set_post_code('453150')
# Sterlitamak.set_phone_code('83470')
# print(Sterlitamak)


