import json


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_data(self):
        return self.name, self.age, self.gender


class MyCatEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            "Name": o.name,
            "Age": o.age,
            "Gender": o.gender,
            "Methods": {
                "get_data": o.get_data()
            },
            "ClassName": o.__class__.__name__
        }


my_cat = MyCat('Vaska', 3, 'men')
json_data = json.dumps(my_cat, cls=MyCatEncoder, ensure_ascii=False, indent=3)
print(json_data)

python_cats = json.loads(json_data)
print(python_cats)

with open (f'my_cat_encoder.json', 'w', encoding='utf-8') as fh:
    json.dump(my_cat, fh, cls=MyCatEncoder, ensure_ascii=False, indent=2)

with open(f'my_cat_encoder.json', 'r', encoding='utf-8') as fh:
    python_cats_from_file = json.load(fh)

print(python_cats_from_file)
