import json

my_dict = {
    'my_string': 'some_string',
    'my_integer': 1234,
    'my_tuple': (1, 2, 3),
    'my_bool': True,
    'my_none': None,
}
"""сразу же записываем словарь в файл, в формате json с правильными отступами"""
with open(r'my_json.json', 'w', encoding='utf-8') as fp:
    json.dump(my_dict, fp, ensure_ascii=False, indent=2)

"""сперва преобразуем словарь в формат json"""
my_json_string = json.dumps(my_dict)
print(my_json_string, 'формат Json')
print(type(my_json_string), 'формат Json')

"""потом записываем в файл (но тут все будет записано в одну строку!!!)"""
with open(r'my_json2.json', 'w', encoding='utf-8') as fp:
    fp.write(my_json_string)
#     json_string = fp.read()
#     python_data = json.loads(json_str)


"""считываем данные из json файла"""
with open(r'my_json.json') as fp:
    python_data = json.load(fp)

print(python_data, 'формат Python')

# my_js = json.dumps(my_dict)
# print(my_js)
my_dict_from_json = json.loads(my_json_string)
print(my_dict_from_json, 'формат Python')
print(type(my_dict_from_json), 'формат Python')
for key, value in my_dict_from_json.items():
    if 'tuple' in key:
        my_dict_from_json[key] = tuple(value)
print(my_dict_from_json, 'формат Python')
