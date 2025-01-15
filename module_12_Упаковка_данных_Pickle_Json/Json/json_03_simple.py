import json


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def to_json(obj):
        if isinstance(obj, MyCat):
            result = obj.__dict__
            result['ClassName'] = obj.__class__.__name__
            result['Methods'] = ['Many Methods']
            return result


my_cat = MyCat('Vaska', 3, 'men')

json_data = json.dumps(my_cat, default=MyCat.to_json, ensure_ascii=False, indent=2)

with open(r'my_cats.json', 'w', encoding='utf-8') as fh:
    json.dump(my_cat, fh, default=MyCat.to_json, ensure_ascii=False, indent=2)

with open(r'my_cats.json', 'r', encoding='utf-8') as fh:
    python_cats_from_file = json.load(fh)

print(json_data)

python_cats_from_string = json.loads(json_data)
print(python_cats_from_string)
print(python_cats_from_file)

