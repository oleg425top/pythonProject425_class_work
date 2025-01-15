import json


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age =age
        self.gender = gender

my_cat = MyCat('Vaska', 3, 'men')
print(my_cat.__dict__)
json_data = json.dumps(my_cat.__dict__, default=lambda obj_cat: obj_cat.__dict__, ensure_ascii=False, indent=2)
print(json_data)

with open(r'cats_json.json', 'w', encoding='utf-8') as file:
    json.dump(my_cat, file, default= lambda obj_cat: obj_cat.__dict__, ensure_ascii=False, indent=2)

with open(r'cats_json.json', 'r', encoding= 'utf-8') as fh:
    python_cat = json.load(fh)
print(python_cat)
print(type(python_cat))
